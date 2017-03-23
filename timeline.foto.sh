#!/bin/bash
# fswebcam -r 1280x720 --no-banner /home/pi/webcam/$DATE.jpg

DATE=$(date +"%Y-%m-%d_%H%M%S")
fswebcam /var/www/html/3d/$DATE.jpg

