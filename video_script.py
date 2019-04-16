import os
import time

avcmd = "avconv -t 10 -i /dev/video0 "


mission_complete = datetime.now() + timedelta(hours=2)

def vidcap():
    now = datetime.now()
    if now < mission_complete:
        threading.Timer(10.0, vidcap).start()
        vidstr = "~/CS21proj/Videos/" + now.strftime("%m-%d.%H.%M.%S.avi")

        os.system(avcmd + vidstr)
        print("Video captured at " + now.strftime("%H:%M:%S.%f"))

    else:
        print("2 hours elapsed, mission complete.")

vidcap()