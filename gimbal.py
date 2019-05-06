import RPi.GPIO as GPIO
from time import sleep

#Gyro data that will be provided by Data Correlation team:
#Yaw - Datatype is float. Measurements in Degrees of Angle. (-180 to 180 Degrees)
#Pitch - Datatype is float. Measurements in Degrees of Angle. (-90 to 90 Degrees)
#Roll - Datatype is float. Measurements in Degrees of Angle. (-180 to 180 Degrees)

xGPIO=19
yGPIO=26

Yaw = 0
Pitch = 45
Roll = 0

print("Using GPIO19 for xServo")
print("Using GPIO26 for yServo")
print("Using Gpiozero defaults for the servo class")

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
pwm=GPIO.PWM(19,50)
pwm.start(0)

def SetAngle(angle):
    #DutyCycle 2 is full right, and 11.85 is full left
    #DC 2-10.75 gives us a 180 degree arc
    #(10.75-2)/180 = 0.048611
    #With rotor facing down, 0 degrees is full counterclockwise, 180 is full clockwise
    duty = angle * 0.048611 + 2
    GPIO.output(19, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(19, False)
    pwm.ChangeDutyCycle(0)

# def FindTilt(pitch):
#     if
#
# def FindHorizon(yaw, pitch, roll):
#     if

SetAngle(90)
sleep(1)
SetAngle(0)
sleep(1)
SetAngle(90)
sleep(1)
SetAngle(180)
sleep(1)
SetAngle(90)
sleep(1)
pwm.stop()
GPIO.cleanup()
#ServoTest()