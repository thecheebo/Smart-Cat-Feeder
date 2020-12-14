import RPi.GPIO as GPIO
import tf_image_detection as tf
from time import sleep
import paho.mqtt.publish as publish

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def motionSensor(channel):
    
    if GPIO.input(11):
        if tf.detect_cat():
            publish.single("Food", "hungry", hostname = "192.168.0.53")

def detect():
    GPIO.add_event_detect(11, GPIO.BOTH, callback=motionSensor, bouncetime = 150)

      
    try:
        while True:
            sleep(1)

    finally:
        GPIO.cleanup()
