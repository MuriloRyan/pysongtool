#!bin/bash

echo "***PYSONGTOOL WORKSPACE SETUP STARTED***"

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

echo "***SETUP FINISHED***"