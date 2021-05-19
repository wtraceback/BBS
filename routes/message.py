from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
)

from models.message import Message
from routes import current_user


message = Blueprint('message', __name__)


@message.route('/')
def index():
    u = current_user()
    if u is None:
        return redirect(url_for('auth.login'))

    send_msg = Message.find_all(sender_id=u.id)
    received_msg = Message.find_all(receiver_id=u.id)
    return render_template('message/index.html', sends=send_msg, receives=received_msg)


@message.route('/add', methods=['POST'])
def add():
    u = current_user()
    if u is not None:
        form = request.form
        msg = Message.new(form)
        msg.set_sender(u.id)
        return redirect(url_for('message.index'))

    return redirect(url_for('topic.index'))


@message.route('/view/<int:id>')
def view(id):
    u = current_user()
    msg = Message.get(id)

    if u.id == msg.receiver_id:
        msg.mark_read()

    if u.id in [msg.sender_id, msg.receiver_id]:
        return render_template('message/detail.html', message=msg)
    else:
        return redirect(url_for('message.index'))