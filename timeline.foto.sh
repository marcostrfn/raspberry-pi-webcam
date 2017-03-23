#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M%S")
# fswebcam -r 1280x720 --no-banner /home/pi/webcam/$DATE.jpg
fswebcam /var/www/html/3d/$DATE.jpg
