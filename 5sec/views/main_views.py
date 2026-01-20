from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello():
    return 'Hello world! bro'

@bp.route('/')
def index():
    return 'Pybo index'