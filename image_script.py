import picamera
from datetime import datetime, timedelta
import time
import threading


time.sleep(2)
sensor_readjust = datetime.now() + timedelta(minutes=10)
mission_complete = datetime.now() + timedelta(hours=2)
# test = datetime.now() + timedelta(seconds=30)

def photocap():
    global sensor_readjust
    now = datetime.now()
    if now > sensor_readjust:
        threading.Timer(3.0, photocap).start()
        print("Resting the sensor for 3 seconds to set light levels, photo capture will resume in \n3")
        # time.sleep(1)
        # print("2")
        # time.sleep(1)
        # print("1")
        sensor_readjust += timedelta(minutes=10)

    elif now < mission_complete:
        threading.Timer(1.0, photocap).start()
        picstr = "/home/pi/CS21proj/Photos" + now.strftime("/%m-%d.%H.%M.%S.jpg")

        with picamera.PiCamera() as camera:
            camera.resolution = (1280, 720)
            camera.capture(picstr)
        print("Photo captured at " + now.strftime("%H:%M:%S.%f"))

    else:
        print("2 hours elapsed, mission complete.")

photocap()