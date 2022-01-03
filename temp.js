const video1 = document.getElementsByClassName('input_video1')[0];
const out1 = document.getElementsByClassName('output1')[0];
const control = document.getElementsByClassName('control1')[0];
const ctx1 = out1.getContext('2d');
const face = document.getElementById("cimg");
const ctx2 = face.getContext("2d");
const fps = new FPS();
const padd = 20;

var h = 480;
var w = 480;

function changeCanvas() {
    var he = prompt("Height", "480");
    var wi = prompt("Width", "480");
    if (parseInt(h) == NaN) {
        h = 480;
    } else {
        h = parseInt(he);
    }
    if (parseInt(w) == NaN) {
        w = 480;
    } else {
        w = parseInt(wi);
    }
    out1.setAttribute("width", w.toString() + "px");
    out1.setAttribute("height", h.toString() + "px");
}
showed = 0;
function showControl() {
    if (showed) {
        control.style.visibility = "hidden";
        showed = 0;
    } else {
        control.style.visibility = "visible";
        showed = 1;
    }
}
    
var model;
async function init(URL) {
    const modelURL = URL + "model.json";
    const metadataURL = URL + "metadata.json";
    model = await tmImage.load(modelURL, metadataURL);
    console.log("ok")
    console.log(model)
    maxPredictions = model.getTotalClasses();
}
init("https://teachablemachine.withgoogle.com/models/LqN_AW69L/");

ctx1.font = "30px Cambria";


async function predict() {
    prediction = await model.predictTopK(face, 1, 0);
    console.log("anwglgn");
    console.log(prediction);
    if (prediction[0].probability.toFixed(2) < 0.3) {
        return "unknown";
    }
    return prediction[0].className + ": " + prediction[0].probability.toFixed(2);
}

async function onResultsFace(results) {
    fps.tick();
    ctx1.save();
    ctx1.clearRect(0, 0, out1.width, out1.height);
    ctx1.drawImage(results.image, 0, 0, out1.width, out1.height);
    for (i = 0; i < results.detections.length; i++) {
        bbox = results.detections[i].boundingBox;
        var x = bbox.xCenter * w - bbox.width * w / 2;
        var y = bbox.yCenter * h - bbox.height * h / 2;
        ctx2.clearRect(0, 0, 200, 200);
        ctx2.drawImage(results.image, x, y, bbox.width*w, bbox.height*h, 0, 0, 200, 200);
        var prediction = await predict(bbox);
        draw(bbox, prediction);
    }
    ctx1.restore();
}

const faceDetection = new FaceDetection({
    locateFile: (file) => {
        return `https://cdn.jsdelivr.net/npm/@mediapipe/face_detection@0.0/${file}`;
    }
});
console.log("face");
console.log(faceDetection);
faceDetection.onResults(onResultsFace);

const camera = new Camera(video1, {
    onFrame: async () => {
        await faceDetection.send({ image: video1 });
    },
    width: w,
    height: h
});
camera.start();

new ControlPanel(control, {
    selfieMode: true,
    minDetectionConfidence: 0.5,
})
    .add([
        new StaticText({ title: 'Control Panel' }),
        fps,
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

