import os
import logging
import configparser

CONFIG_FILEPATH = os.path.join('conf', 'myapp.ini')

logger = logging.getLogger(__name__)
config = configparser.ConfigParser()
config.read(CONFIG_FILEPATH)
