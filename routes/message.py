from flask import (
    Blueprint,
    render_template,
)


message = Blueprint('message', __name__)


@message.route('/')
def index():
    return render_template('message/index.html')