import RPi.GPIO as GPIO
import picamera
from time import sleep

camera=picamera.PiCamera()

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

camera.start_preview()
GPIO.output(17,True)

camera.start_recording('video1.h264')
raw_input("Press Key to stop recording")
camera.stop_recording()
GPIO.output(17,False)
GPIO.cleanup()
