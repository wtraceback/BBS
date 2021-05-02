from flask import Flask

from config import Config


app = Flask(__name__)
app.config.from_object(Config)


# 注册蓝图
from routes.main import main as main_bp
app.register_blueprint(main_bp)
from routes.auth import auth as auth_bp
app.register_blueprint(auth_bp)


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=5000,
    )

    app.run(**config)