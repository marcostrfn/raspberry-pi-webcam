#!/usr/bin/python

import subprocess
import time


while True:

  time.sleep(5) # delays for 5 seconds
  p = subprocess.Popen(["/home/pi/bin/timeline.foto.sh"], stdout=subprocess.PIPE)
  # print p.communicate()
  time.sleep(10)


