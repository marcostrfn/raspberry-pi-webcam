#!/usr/bin/python

import subprocess
import time

while True:
  time.sleep(5)
  p = subprocess.Popen(["timeline.foto.sh"], stdout=subprocess.PIPE)  
  time.sleep(10)
