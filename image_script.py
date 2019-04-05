import picamera
import datetime

time=datetime.datetime.now()
current=str(time.day)+"-"+str(time.month)+"-"+str(time.year)+"_"+str(time.hour)+":"+str(time.minute)

with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture("Desktop/cookie/current.jpg")
