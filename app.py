from flask import Flask


app = Flask(__name__)


# 注册蓝图
from routes.main import main as main_bp
app.register_blueprint(main_bp)


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=5000,
    )

    app.run(**config)