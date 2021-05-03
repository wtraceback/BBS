from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
)

from routes import current_user
from models.reply import Reply


reply = Blueprint('reply', __name__)


@reply.route('/add', methods=['POST'])
def add():
    form = request.form
    u = current_user()
    r = Reply.new(form, user_id=u.id)
    return redirect(url_for('topic.detail', id=r.topic_id))
