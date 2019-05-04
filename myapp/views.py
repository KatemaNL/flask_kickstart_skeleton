import logging

from flask import Blueprint

myapp = Blueprint('app', __name__, template_folder='templates')
logger = logging.getLogger(__name__)


@myapp.route('/')
def hello():
    logger.info('Hello!')
    return 'Hello World!'
