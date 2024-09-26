#!/bin/bash

# Define the cronjob line
CRON_JOB="34 9 * * * /home/user/Escritorio/FAT2024G3-BACKEND/start_django.sh > /home/user/Escritorio/FAT2024G3-BACKEND/cron_logs.log 2>&1"

# Check if the cronjob already exists
(crontab -l | grep -Fxq "$CRON_JOB") || (
  # Add the cronjob to the crontab if it does not exist
  (crontab -l; echo "$CRON_JOB") | crontab -
  echo "Cronjob added."
)
