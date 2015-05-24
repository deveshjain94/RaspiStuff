import RPi.GPIO as GPIO
import picamera
from time import sleep

camera=picamera.PiCamera()

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
  GPIO.wait_for_edge(17,GPIO.FALLING)
  camera.start_preview()
  camera.start_recording('video.h264')
  try:
    GPIO.wait_for_edge(17,GPIO.RISING)
    camera.stop_recording()
  except KeyboardInterrupt:
    GPIO.cleanup()
except KeyboardInterrupt:
  GPIO.cleaup()
GPIO.cleanup()
