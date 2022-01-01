import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Rescaling

# Create a dataset.
dataset = keras.preprocessing.image_dataset_from_directory(
  'train')

