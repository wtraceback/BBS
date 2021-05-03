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
    ts = Topic.all()
    return render_template('topic/index.html', topics=ts)


@topic.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        form = request.form
        u = current_user()
        t = Topic.new(form, user_id=u.id)
        return redirect(url_for('topic.detail', id=t.id))

    return render_template('topic/add.html')


@topic.route('/<int:id>')
def detail(id):
    t = Topic.get(id)
    return render_template('topic/detail.html', topic=t)