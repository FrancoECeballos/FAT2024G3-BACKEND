#!/bin/bash

# Define the cronjob line
CRON_JOB="11 1 * * * /home/user/Escritorio/FAT2024G3-BACKEND/auto.sh > /home/user/Escritorio/FAT2024G3-BACKEND/cron_logs.log 2>&1"

# Remove the cronjob if it exists
(crontab -l | grep -Fxv "$CRON_JOB") | crontab -
echo "Cronjob removed."
