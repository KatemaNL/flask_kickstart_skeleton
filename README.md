# Flask Kickstart Skeleton

Skeleton Flask configuration for kickstarting your webapp
This repository is aimed at users who want to kickstart their webapp with a default Flask configuration.

# Disclaimer:
The repository is intended as a starting point for configuring Flask as a webserver in a development environment. 
It by no means is to be used as-is in a production environment.
The correct working of this configuration is not guaranteed in any way. Use entirely at your own risk. 
  

# Prerequisites
- Linux
- Python 3

# Install
1. Open a terminal and navigate to a directory you want to install this project in as a new directory. (f.i. ~)
2. Clone this Git repository into the current directory: `https://github.com/KatemaNL/flask_kickstart_skeleton.git`
3. Make sure you have to correct permissions on this new directory: `sudo chown -R <your_user>:<your_user> flask_kickstart_skeleton` **Note: Be aware you are running the webserver under your current user which is unsafe in a production environment.**
4. Create a virtual environment: `cd ../bin` and run the script: `./create_venv_dev.sh`


# Run
1. Run the application (from the `flask_kickstart_skeleton/bin` directory) : `./run_dev.sh`
2. Open a browser and navigate to: http://127.0.0.1:5000/
3. You can quit the webserver by pressing CTRL+C from the terminal.

# Example features:
## A page with text from a string
- Rendering a page from string: URL: http://127.0.0.1:5000/ Configured in the function `hello()` in `myapp/views.py`

Note: Find the `Hello!` log statement in `log/info.log`. It is triggered from the `hello()` function. Logging is already configured for you!
See the `conf/logging.yaml` file to find out more. Do you only want INFO messages? Change the root level to INFO instead of DEBUG at the end of the `logging.yaml` file.

## Static page  
- Rendering a static page from a (static) HTML template. URL: http://127.0.0.1:5000/ Configured in the function `static_page()` in `myapp/views.py`

## Dynamic page with table
- Rendering a dynamic page with python data transformed into HTML. URL: http://127.0.0.1:5000/dynamic_table_page

## Configuration
- The app can be configured from the conf/myapp.ini file. 
- The config can be used throughout the app by importing the config object: `from conf.config import config` and accessing its values: `config.getboolean(section='settings_group1', option='group1_option1')`
- The current settings can be viewed from: http://127.0.0.1:5000/config