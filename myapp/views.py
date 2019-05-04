import logging

from flask import Blueprint, render_template

myapp = Blueprint('app', __name__, template_folder='templates')
logger = logging.getLogger(__name__)


@myapp.route('/')
def hello():
    logger.info('Hello!')
    render_text = 'Hello World!'
    return render_text

@myapp.route('/basic_template')
def basic_template():
    return render_template('basic_template.html', title='Home')
