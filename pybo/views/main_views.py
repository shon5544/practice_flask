from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return '안녕하세요'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))
