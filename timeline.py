#!/usr/bin/python

import subprocess
import time
import os

# directorio donde se encuentra timeline.foto.sh
dir = os.path.join('tu directorio','timeline.foto.sh')

while True:  
  p = subprocess.Popen([dir], stdout=subprocess.PIPE)  
  time.sleep(10)
