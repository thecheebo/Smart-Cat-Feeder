from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import io
import re
import time

import numpy as np
import picamera

from PIL import Image
from tflite_runtime.interpreter import Interpreter

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
DETECTION_THRESHOLD = 0.5
LABEL_PATH = "./tf_resources/coco_labels.txt"
MODEL_PATH = "./tf_resources/detect.tflite"

def load_labels(path):
  """Loads the labels file. Supports files with or without index numbers."""
  with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    labels = {}
    for row_number, content in enumerate(lines):
      pair = re.split(r'[:\s]+', content.strip(), maxsplit=1)
      if len(pair) == 2 and pair[0].strip().isdigit():
        labels[int(pair[0])] = pair[1].strip()
      else:
        labels[row_number] = pair[0].strip()
  return labels

def set_input_tensor(interpreter, image):
  """Sets the input tensor."""
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = image


def get_output_tensor(interpreter, index):
  """Returns the output tensor at the given index."""
  output_details = interpreter.get_output_details()[index]
  tensor = np.squeeze(interpreter.get_tensor(output_details['index']))
  return tensor


def detect_objects(interpreter, image, threshold, labels):
  """Returns a list of detection results, each a dictionary of object info."""
  set_input_tensor(interpreter, image)
  interpreter.invoke()

  # Get all output details
  classes = get_output_tensor(interpreter, 1)
  scores = get_output_tensor(interpreter, 2)
  count = int(get_output_tensor(interpreter, 3))
  results = []
  for i in range(count):
    class_id = classes[i]
    object_label = labels[class_id]
    if scores[i] >= threshold:
      result = {
          'label': object_label,
          'score': scores[i]
      }
      results.append(result)

  return results



def detect_cat(detection_threshold = DETECTION_THRESHOLD):
    labels = load_labels(LABEL_PATH)
    interpreter = Interpreter(MODEL_PATH)
    interpreter.allocate_tensors()
    _, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']

    with picamera.PiCamera(resolution=(CAMERA_WIDTH, CAMERA_HEIGHT), framerate=30) as camera:
        #camera.start_preview()
        try:
            stream = io.BytesIO()
            camera.capture(stream, format='jpeg')
            stream.seek(0)
            image = Image.open(stream).convert('RGB').resize((input_width, input_height), Image.ANTIALIAS)

            results = detect_objects(interpreter, image, detection_threshold, labels)
            #print("Detection from Pi camera", results)

            for detected_obj_data in results:
              if detected_obj_data["label"] in ['cat']:
                print (detected_obj_data["label"], "has been detected")
                return True
            stream.seek(0)
            stream.truncate()

        finally:
          camera.stop_preview()
    return False



# if __name__ == '__main__':
#   can_move()


