from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    url_for,
)

from models.board import Board


board = Blueprint('board', __name__)


@board.route('/manage')
def manage():
    bs = Board.all()
    return render_template('board/manage.html', boards=bs)


@board.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        form = request.form
        b = Board.new(form)
        return redirect(url_for('board.manage'))

    return render_template('board/add.html')


@board.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    b = Board.delete(id)
    return redirect(url_for('board.manage'))