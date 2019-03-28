import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep

#Gyro data that will be provided by Data Correlation team:
#Yaw - Datatype is float. Measurements in Degrees of Angle. (-180 to 180 Degrees)
#Pitch - Datatype is float. Measurements in Degrees of Angle. (-90 to 90 Degrees)
#Roll - Datatype is float. Measurements in Degrees of Angle. (-180 to 180 Degrees)

xGPIO=4
yGPIO=17
Yaw = 0
Pitch = 45
Roll = 0

rotationServo = Servo(xGPIO)
pitchServo = Servo(yGPIO)

print("Using GPIO4 for xServo")
print("Using GPIO5 for yServo")
print("Using Gpiozero defaults for the servo class")

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(03, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    pwm.ChangeDutyCycle(0)

def ServoTest():
    while True:
        rotationServo.mid()
        pitchServo.mid()
        print("Set to middle position")
        sleep(1)
        rotationServo.min()
        pitchServo.min()
        print("Set to minimum position")
        sleep(1)
        rotationServo.mid()
        pitchServo.mid()
        print("Set to middle position")
        sleep(1)
        rotationServo.max()
        pitchServo.max()
        print("Set to maximum position")
        sleep(1)
        
ServoTest()

while True:
    #adjustment data goes here
    import fovFootprintGas 
    sleep(1)