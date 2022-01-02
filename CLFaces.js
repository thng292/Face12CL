const video1 = document.getElementsByClassName('input_video1')[0];
const out1 = document.getElementsByClassName('output1')[0];
const controlsElement1 = document.getElementsByClassName('control1')[0];
const canvasCtx1 = out1.getContext('2d');
const fpsControl = new FPS();
const padd = 20;
canvasCtx1.font = "30px Cambria"

var h = prompt("Height", "480")
var w = prompt("Width", "480")
if (parseInt(h)==NaN) {
    h = 480;
} else {
    h = parseInt(h);
}
if (parseInt(w)==NaN) {
    w = 480;
} else {
    w = parseInt(w);
}

out1.setAttribute("width", w);
out1.setAttribute("height", h);

showed = 0;
function showControl() {
    if (showed) {
        controlsElement1.style.visibility = "hidden";
        showed = 0;
    } else {
        controlsElement1.style.visibility = "visible";
        showed = 1;
    }
}

function draw(bbox, text) {
    console.log(text)
    var x = bbox.xCenter * w - bbox.width * w / 2 - padd;
    var y = bbox.yCenter * h-bbox.height*h/2-padd
    canvasCtx1.beginPath();
    canvasCtx1.fillStyle = 'red';
    canvasCtx1.fillText(text, x, y-5);
    canvasCtx1.beginPath();
    canvasCtx1.fillStyle = '#00000000';
    canvasCtx1.fill();
    canvasCtx1.lineWidth = 4;
    canvasCtx1.strokeStyle = 'blue';
    canvasCtx1.rect(x,y, bbox.width*w+padd*2, bbox.height*h+padd*2);
    canvasCtx1.stroke();
}

function onResultsFace(results) {
    fpsControl.tick();
    canvasCtx1.save();
    canvasCtx1.clearRect(0, 0, out1.width, out1.height);
    canvasCtx1.drawImage(results.image, 0, 0, out1.width, out1.height);
    for (i = 0; i < results.detections.length; i++) {
        draw(results.detections[i].boundingBox,"unknown" + i);
    }
    canvasCtx1.restore();
    debugger;
}

const faceDetection = new FaceDetection({
    locateFile: (file) => {
        return `https://cdn.jsdelivr.net/npm/@mediapipe/face_detection@0.0/${file}`;
    }
});
faceDetection.onResults(onResultsFace);

const camera = new Camera(video1, {
    onFrame: async () => {
        await faceDetection.send({ image: video1 });
    },
    width: w,
    height: h
});
camera.start();

new ControlPanel(controlsElement1, {
    selfieMode: true,
    minDetectionConfidence: 0.5,
})
    .add([
        new StaticText({ title: 'Control Panel' }),
        fpsControl,
        new Toggle({ title: 'Selfie Mode', field: 'selfieMode' }),
        new Slider({
            title: 'Min Detection Confidence',
            field: 'minDetectionConfidence',
            range: [0, 1],
            step: 0.01
        }),
    ])
    .on(options => {
        video1.classList.toggle('selfie', options.selfieMode);
        faceDetection.setOptions(options);
    });