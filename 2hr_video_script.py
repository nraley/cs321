import os
from datetime import datetime, timedelta
import threading
import time

avcmd = "avconv -t 7200 -i /dev/video0 "
mission_complete = datetime.now() + timedelta(minutes=10)

now = datetime.now()
vidstr = "~/CS21proj/Videos/" + now.strftime("%m-%d.%H.%M.%S.avi")
os.system(avcmd + vidstr)
print("Video captured at " + now.strftime("%H:%M:%S.%f"))