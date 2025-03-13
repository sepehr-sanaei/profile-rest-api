#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/sepehr-sanaei/profile-rest-api.git'

PROJECT_BASE_PATH='/usr/local/apps/profiles-rest-api'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

# Install Python, SQLite, pip, build dependencies, and other necessary tools
echo "Installing dependencies..."
apt-get update
apt-get install -y python3.10 python3.10-venv python3.10-dev sqlite3 python3-pip supervisor nginx git build-essential libpcre3-dev libssl-dev

# Clone project repo and create virtual environment
mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

# Create Python 3.10 virtual environment
python3.10 -m venv $PROJECT_BASE_PATH/env

# Upgrade pip, setuptools, and wheel
$PROJECT_BASE_PATH/env/bin/pip install --upgrade pip setuptools wheel

# Install project dependencies
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt

# Install uwsgi (or gunicorn as a fallback)
# Option 1: Install a newer version of uwsgi
echo "Installing uwsgi..."
$PROJECT_BASE_PATH/env/bin/pip install uwsgi --upgrade

# Option 2: Install gunicorn if uwsgi installation fails (uncomment if you want to switch to gunicorn)
# $PROJECT_BASE_PATH/env/bin/pip install gunicorn

# Run Django migrations
$PROJECT_BASE_PATH/env/bin/python $PROJECT_BASE_PATH/manage.py migrate

# Setup Supervisor to run our uwsgi or gunicorn process.
cp $PROJECT_BASE_PATH/deploy/supervisor_profiles_api.conf /etc/supervisor/conf.d/profiles_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart profiles_api

# Setup nginx to make our application accessible.
cp $PROJECT_BASE_PATH/deploy/nginx_profiles_api.conf /etc/nginx/sites-available/profiles_api.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/profiles_api.conf /etc/nginx/sites-enabled/profiles_api.conf
systemctl restart nginx.service

echo "DONE! :)"
