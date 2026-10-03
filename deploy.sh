#!/bin/bash

set -e

echo "Starting ZecPath deployment..."

cd /var/www/zecpath_admin

echo "Pulling latest code..."
git pull origin main

echo "Activating virtual environment..."
source /var/www/zecpath-venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Restarting Gunicorn..."
sudo systemctl restart zecpath

echo "Deployment completed successfully."