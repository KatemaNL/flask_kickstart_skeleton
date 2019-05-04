import os
import datetime
import logging
from flask import Flask
from myapp.logconfig import config_logging

LOGGING_CONFIG_FILE = os.path.join('conf', 'logging.yaml')

config_logging(LOGGING_CONFIG_FILE)
logger = logging.getLogger(__name__)
logger.info('Using logging config: {}'.format(os.path.abspath(LOGGING_CONFIG_FILE)))
logger.info('Working dir: {}'.format(os.getcwd()))
logger.info('Loading MyApp init')


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    logger.info('App created with ID: {}'.format(id(app)))

    app.permanent_session_lifetime = datetime.timedelta(days=36500)

    app.config.from_mapping(
        SECRET_KEY='9BS5AdX5YTjJTYf2ge4kVUAf5nxebnpY',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from myapp.views import myapp
    app.register_blueprint(myapp)

    return app
