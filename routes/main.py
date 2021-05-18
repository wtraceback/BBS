from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    current_app,
    send_from_directory,
)
from werkzeug.utils import secure_filename
import os

from routes import current_user
from utils import allowed_file


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    u = current_user()
    if u is None:
        return redirect(url_for('topic.index'))

    return render_template('profile.html', user=u)


@main.route('/addavatar', methods=['POST'])
def add_avatar():
    u = current_user()

    if u is None:
        return redirect(url_for('main.profile'))

    if 'file' not in request.files:
        return redirect(url_for('main.profile'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('main.profile'))

    if allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['AVATAR_UPLOAD_PATH'], filename))
        u.user_avatar = filename
        u.save()

    return redirect(url_for('main.profile'))


@main.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['AVATAR_UPLOAD_PATH'], filename)