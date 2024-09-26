#!/bin/bash

# Define the cronjob line
CRON_JOB="34 9 * * * /home/user/Escritorio/FAT2024G3-BACKEND/start_django.sh > /home/user/Escritorio/FAT2024G3-BACKEND/cron_logs.log 2>&1"

# Remove the cronjob if it exists
(crontab -l | grep -Fxv "$CRON_JOB") | crontab -
echo "Cronjob removed."
