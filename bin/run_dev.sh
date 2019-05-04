#!/usr/bin/env bash

cd .. &&
export FLASK_APP=myapp &&
export FLASK_ENV=development &&
source venv/bin/activate &&
flask run  &&
deactivate