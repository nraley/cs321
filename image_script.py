import picamera
from datetime import datetime
import time

time.sleep(2)

for x in range(7260):
    now = datetime.now()
    picstr = "/home/pi/CS21proj/Photos" + now.strftime("/%m-%d.%H.%M.%S.jpg")

    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.capture(picstr)