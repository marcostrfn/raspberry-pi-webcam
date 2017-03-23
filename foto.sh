#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

# para tomar imagen con banner
# fswebcam -r 1280x720 --no-banner /home/pi/webcam/$DATE.jpg

fswebcam /var/www/html/webcam/$DATE.jpg
