#!/usr/bin/python
import time
import RPi.GPIO as GPIO
from hosted import device, node, config
config.restart_on_update()
device.gpio.monitor(config.pin)
for pin, state in device.gpio.poll_forever():
    node.send('/state:%d' % state)
relay_ch = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(relay_ch, GPIO.OUT)
GPIO.output(relay_ch, GPIO.LOW)
time.sleep(1)
GPIO.output(relay_ch, GPIO.HIGH)
GPIO.cleanup()
