#!/bin/bash

VENV_DIR=".venv"

#Make sure they're sudo
if [[ $UID != 0 ]]; then
    echo "Please run this script with sudo:"
    echo "sudo $0 $*"
    exit 1
fi

if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv $VENV_DIR
fi

source $VENV_DIR/bin/activate

python3 -m pip install -r requirements.txt
sudo .venv/bin/python3 linuxDiscordUpdater.py