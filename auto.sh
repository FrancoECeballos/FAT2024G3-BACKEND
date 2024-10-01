#!/bin/bash

export PATH=$PATH:/home/user/.local/bin

cd /home/user/Escritorio/FAT2024G3-BACKEND/ProntaEntregaDjango
pipenv run python manage.py auto_vencimiento

