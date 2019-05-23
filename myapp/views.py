import logging

import flask

from conf.config import config

myapp = flask.Blueprint('app', __name__, template_folder='templates')
logger = logging.getLogger(__name__)


@myapp.route('/')
def hello():
    logger.info('Hello!')
    render_text = 'Hello World!'
    return render_text


@myapp.route('/static_page')
def static_page():
    return flask.render_template('static_page.html')


@myapp.route('/dynamic_table_page')
def dynamic_table_page():
    rows = [(1, 2), (3, 4), (5, 6)]
    return flask.render_template('dynamic_table_page.html', rows=rows)


@myapp.route('/config')
def conf():
    return flask.render_template('config.html',
                                 group1_option1=config.getboolean(section='settings_group1', option='group1_option1'),
                                 group1_option2=config.getfloat(section='settings_group1', option='group1_option2'),
                                 group2_option1=config.getint(section='settings_group2', option='group2_option1'),
                                 group2_option2=config.get(section='settings_group2', option='group2_option2'))
