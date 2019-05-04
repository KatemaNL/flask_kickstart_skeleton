#!/usr/bin/env bash

cd ..
python3 -m venv venv &&
source venv/bin/activate &&
pip install flask pyyaml