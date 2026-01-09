#!/bin/bash
set -e

# Configuration
PROJECT_DIR="/home/$USER/Learn_French"
VENV_PATH="/home/$USER/.virtualenvs/myenv"
LOG_FILE="/home/$USER/deploy.log"

echo "=== Deployment started at $(date) ===" > "$LOG_FILE"

# Navigate to project directory
cd "$PROJECT_DIR" || { echo "Error: Directory $PROJECT_DIR not found" >> "$LOG_FILE"; exit 1; }

echo "Git pull..." >> "$LOG_FILE"
git pull origin main >> "$LOG_FILE" 2>&1

echo "Activating virtualenv..." >> "$LOG_FILE"
if [ -d "$VENV_PATH" ]; then
    source "$VENV_PATH/bin/activate" >> "$LOG_FILE" 2>&1
else
    echo "Error: Virtualenv not found at $VENV_PATH" >> "$LOG_FILE"
    exit 1
fi

echo "Installing dependencies..." >> "$LOG_FILE"
pip install -r requirements.txt >> "$LOG_FILE" 2>&1

echo "Running migrations..." >> "$LOG_FILE"
python manage.py migrate >> "$LOG_FILE" 2>&1

echo "Collecting static files..." >> "$LOG_FILE"
python manage.py collectstatic --noinput >> "$LOG_FILE" 2>&1

echo "DEPLOYMENT_COMPLETE at $(date)" >> "$LOG_FILE"
