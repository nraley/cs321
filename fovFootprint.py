import math


print("FOV Footprint is")

alti = 100
xsensor = 39.6
ysensor = 26.99
xgimbal = 30
ygimbal = 30

def calcFOV(alti, xSensor, ySensor, xgimbal, ygimbal):
    distBot = distTop = distLeft = distRight = xfootprint = yfootprint = 1
    distBot = alti * math.tan(toRad(ygimbal - (0.5 * xSensor)))  # not sure if gimbal angle vars should be reversed
    distTop = alti * math.tan(toRad(ygimbal + (0.5 * xSensor)))
    distLeft = alti * math.tan(toRad(xgimbal - (0.5 * ySensor)))
    distRight = alti * math.tan(toRad(xgimbal + (0.5 * ySensor)))
    xfootprint = math.fabs(distTop - distBot)  # vals must be abs val of the diff, we're not sure which dist greater
    yfootprint = math.fabs(distLeft - distRight)
    print("The width of the camera FOV footprint is %.2f\n", xfootprint)
    print("The height of the camera FOV footprint is %.2f\n", yfootprint)

def toRad(degreeVal):
    pi = math.pi
    return degreeVal*(pi / 180)

calcFOV(alti, xsensor, ysensor, xgimbal, ygimbal)