#!/bin/bash
# cron_job.sh
# Script to run system_monitor.py and log the output

PYTHON_PATH="/usr/bin/python3"
PROJECT_PATH="/home/username/Projects"
SCRIPT_NAME="system_monitor.py"
LOG_FILE="$PROJECT_PATH/system_monitor.log"

$PYTHON_PATH $PROJECT_PATH/$SCRIPT_NAME >> $LOG_FILE 2>&1
