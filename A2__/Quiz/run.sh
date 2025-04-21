#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 filename"
    exit 1
fi

python3 MainRunner.py "$1"