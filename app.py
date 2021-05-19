from flask import Flask

from config import Config


app = Flask(__name__)
app.config.from_object(Config)


# 注册蓝图
from routes.main import main as main_bp
app.register_blueprint(main_bp)
from routes.auth import auth as auth_bp
app.register_blueprint(auth_bp)
from routes.topic import topic as topic_bp
app.register_blueprint(topic_bp, url_prefix='/topic')
from routes.reply import reply as reply_bp
app.register_blueprint(reply_bp, url_prefix='/reply')
from routes.board import board as board_bp
app.register_blueprint(board_bp, url_prefix='/board')
from routes.admin import admin as admin_bp
app.register_blueprint(admin_bp, url_prefix='/admin')
from routes.message import message as message_bp
app.register_blueprint(message_bp, url_prefix='/message')


@app.context_processor
def make_template_context():
    from flask import session
    from models.user import User
    uid = session.get('user_id', '')
    u = User.find_by(id=uid)

    return dict(current_user=u)


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=5000,
    )

    app.run(**config)
