from flask import (
    Blueprint,
    render_template,
)


topic = Blueprint('topic', __name__)


@topic.route('/')
def index():
    return render_template('topic/index.html')
