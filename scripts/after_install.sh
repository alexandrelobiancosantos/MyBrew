#!/usr/bin/env bash

# kill any servers that may be running in the background 
# sudo pkill -f runserver

# kill frontend servers if you are deploying any frontend
# sudo pkill -f tailwind
# sudo pkill -f node

cd /home/ubuntu/var/www/mybrew/

# activate virtual environment
source mybrew_venv/bin/activate

install requirements.txt
pip install -r /home/ubuntu/var/www/mybrew/requirements.txt

# run server
sudo python manage.py runserver 0.0.0.0:8000