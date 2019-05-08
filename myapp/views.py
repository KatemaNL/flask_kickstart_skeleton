import logging
import json

from flask import Blueprint, render_template

myapp = Blueprint('app', __name__, template_folder='templates')
logger = logging.getLogger(__name__)


@myapp.route('/')
def hello():
    logger.info('Hello!')
    render_text = 'Hello World!'
    return render_text


@myapp.route('/static_page')
def static_page():
    return render_template('static_page.html')


@myapp.route('/dynamic_table_page')
def dynamic_table_page():
    rows = [(1, 2), (3, 4), (5, 6)]
    return render_template('dynamic_table_page.html', rows=rows)
