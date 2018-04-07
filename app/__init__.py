from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def app_create(config_name):
    app = Flask(__name__)
    # 可以直接把对象里面的配置数据转换到app.config里面
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.app_init(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # 路由和其他处理程序定义
    # 从当前目录下面的main子目录导入main
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # ...
    return app