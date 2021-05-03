from flask import (
    Blueprint,
    render_template,
    request,
)


topic = Blueprint('topic', __name__)


@topic.route('/')
def index():
    return render_template('topic/index.html')


@topic.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        pass

    return render_template('topic/add.html')