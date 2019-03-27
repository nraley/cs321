from gpiozero import Servo
from time import sleep

xGPIO=4
yGPIO=5

xServo = Servo(xGPIO)
yServo = Servo(yGPIO)

print("Using GPIO4 for xServo")
print("Using GPIO5 for yServo")
print("Using Gpiozero defaults for the servo class")

while True:
  xServo.mid()
  yServo.mid()
  print("Set to middle position")
  sleep(1)
  xServo.min()
  yServo.min()
  print("Set to minimum position")
  sleep(1)
  xServo.mid()
  yServo.mid()
  print("Set to middle position")
  sleep(1)
  xServo.max()
  yServo.max()
  print("Set to maximum position")
  sleep(1)