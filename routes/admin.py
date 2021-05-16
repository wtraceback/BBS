from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
    render_template,
)

from models.about import About


admin = Blueprint('admin', __name__)


@admin.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        form = request.form
        a = About.get(1)
        if a is None:
            a = About.new(form)
        else:
            a.content = form.get('content', '')
            a.save()

        return redirect(url_for('topic.about'))

    return render_template('admin/settings.html')