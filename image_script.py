import picamera
from datetime import datetime, timedelta
import time
import threading


time.sleep(2)
mission_complete = datetime.now() + timedelta(hours=2)
test = datetime.now() + timedelta(seconds=5)

def photocap():
    now = datetime.now()
    if now < secs:
        threading.Timer(1.0, photocap).start()
        picstr = "/home/pi/CS21proj/Photos" + now.strftime("/%m-%d.%H.%M.%S.jpg")

        with picamera.PiCamera() as camera:
            camera.resolution = (1280, 720)
            camera.capture(picstr)
        print("Photo captured at" + picstr)

    else:
        print("2 hours elapsed, mission complete.")

photocap()

# for x in range(7260):
#     now = datetime.now()
#     picstr = "/home/pi/CS21proj/Photos" + now.strftime("/%m-%d.%H.%M.%S.jpg")
#
#     with picamera.PiCamera() as camera:
#         camera.resolution = (1280,720)
#         camera.capture(picstr)