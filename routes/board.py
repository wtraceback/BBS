from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    url_for,
)

from models.board import Board


board = Blueprint('board', __name__)


@board.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        form = request.form
        b = Board.new(form)
        return redirect(url_for('topic.index'))

    return render_template('board/index.html')