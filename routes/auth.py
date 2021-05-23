from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
)

from models.user import User


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    result = ''

    if request.method == 'POST':
        form = request.form
        u = User.validate_login(form)
        if u is None:
            # 登录的用户不存在
            result = '登录失败，用户不存在或密码错误'
        else:
            session['user_id'] = u.id
            # 设置 cookie 的有效期，True 默认为 31 天
            session.permanent = True
            return redirect(url_for('main.index'))

    return render_template('auth/login.html', result=result)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    result = ''

    if request.method == 'POST':
        form = request.form
        u = User.register(form)

        if u is None:
            result = '注册失败，用户存在或者是输入格式不符合要求'
        else:
            return redirect(url_for('main.index'))

    return render_template('auth/register.html', result=result)