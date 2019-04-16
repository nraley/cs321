import os
import time

avcmd = "avconv -t 10 -i /dev/video0 ~/CS21proj/Videos/vid.avi"
os.system(avcmd)

