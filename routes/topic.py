from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
)
from routes import current_user
from models.topic import Topic
from models.board import Board


topic = Blueprint('topic', __name__)


@topic.route('/')
def index():
    board_id = int(request.args.get('board_id', -1))
    if board_id == -1:
        ts = Topic.all()
    else:
        ts = Topic.find_all(board_id=board_id)

    bs = Board.all()
    user = current_user()

    return render_template('topic/index.html', topics=ts, boards=bs, user=user)


@topic.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        form = request.form
        u = current_user()
        t = Topic.new(form, user_id=u.id)
        return redirect(url_for('topic.detail', id=t.id))

    bs = Board.all()
    return render_template('topic/add.html', boards=bs)


@topic.route('/<int:id>')
def detail(id):
    t = Topic.get(id)
    user = current_user()

    return render_template('topic/detail.html', topic=t, user=user)