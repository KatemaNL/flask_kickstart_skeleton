import logging
import logging.config
import yaml


def config_logging(path_config_file):
    with open(path_config_file, 'r') as logging_conf_file:
        config = yaml.safe_load(logging_conf_file.read())
        logging.config.dictConfig(config)
