from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
import os
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler

# 初始化数据库
db = SQLAlchemy()
# 初始化定时任务
scheduler = APScheduler()

def create_app():
    app = Flask(__name__)
    
    # 配置
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-key-mimotion'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///mimotion.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # 初始化数据库
    db.init_app(app)
    
    # 配置日志
    if not os.path.exists('app/logs'):
        os.mkdir('app/logs')
    file_handler = RotatingFileHandler('app/logs/mimotion.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('MiMotion Flask应用启动')
    
    # 注册蓝图
    from app.controllers.main import main_bp
    from app.controllers.auth import auth_bp
    from app.controllers.account import account_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(account_bp)
    
    # 初始化定时任务
    scheduler.init_app(app)
    scheduler.start()
    
    # 创建数据库表
    with app.app_context():
        db.create_all()
    
    return app 