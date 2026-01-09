#!/bin/bash
set -e

LOG_FILE="/home/$USER/deploy.log"
PROJECT_DIR="/home/$USER/Learn_French"
VENV_PATH="/home/$USER/.virtualenvs/myenv"

echo "=== Deployment started at $(date) ===" > "$LOG_FILE"
echo "User: $USER" >> "$LOG_FILE"
echo "PWD: $(pwd)" >> "$LOG_FILE"

if [ ! -d "$PROJECT_DIR" ]; then
  echo "ERROR: Project directory not found: $PROJECT_DIR" >> "$LOG_FILE"
  exit 1
fi

cd "$PROJECT_DIR" || { echo "ERROR: Cannot cd to $PROJECT_DIR" >> "$LOG_FILE"; exit 1; }
echo "Changed to: $(pwd)" >> "$LOG_FILE"

echo "Running git pull..." >> "$LOG_FILE"
git pull origin main >> "$LOG_FILE" 2>&1 || { echo "ERROR: Git pull failed" >> "$LOG_FILE"; exit 1; }

echo "Activating virtualenv..." >> "$LOG_FILE"
if [ -d "$VENV_PATH" ]; then
    source "$VENV_PATH/bin/activate" >> "$LOG_FILE" 2>&1
else
    echo "ERROR: Virtualenv not found at $VENV_PATH" >> "$LOG_FILE"
    exit 1
fi

echo "Installing dependencies..." >> "$LOG_FILE"
pip install -r requirements.txt >> "$LOG_FILE" 2>&1 || { echo "ERROR: Pip install failed" >> "$LOG_FILE"; exit 1; }

echo "Running migrations..." >> "$LOG_FILE"
python manage.py migrate >> "$LOG_FILE" 2>&1 || { echo "ERROR: Migrations failed" >> "$LOG_FILE"; exit 1; }

echo "Collecting static files..." >> "$LOG_FILE"
python manage.py collectstatic --noinput >> "$LOG_FILE" 2>&1 || { echo "ERROR: Collectstatic failed" >> "$LOG_FILE"; exit 1; }

echo "DEPLOYMENT_COMPLETE at $(date)" >> "$LOG_FILE"
