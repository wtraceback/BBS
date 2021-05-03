from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
)
from routes import current_user
from models.topic import Topic


topic = Blueprint('topic', __name__)


@topic.route('/')
def index():
    return render_template('topic/index.html')


@topic.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        form = request.form
        u = current_user()
        t = Topic.new(form, user_id=u.id)
        return redirect(url_for('topic.index'))

    return render_template('topic/add.html')