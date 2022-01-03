'''
Application Factory Module
'''
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import config
from app import api

from app.api.auth import auth as auth_bp
from app.api.bwai_v1 import bwai_v1 as bwai_v1_bp
from app.api.template import template as template_bp
from app.api.error_handler import error_handler as error_bp

jwt_manager = JWTManager()
cors = CORS()


def create_app(config_name):
    '''Applcation Object 생성 함수'''
    app = Flask(import_name=__name__,
                instance_relative_config=True,
                static_url_path="/",
                static_folder='client/',
                template_folder='client/')
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    jwt_manager.init_app(app)
    cors.init_app(app)
    api.init_app(app)

    app.register_blueprint(error_bp)
    app.register_blueprint(template_bp)
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(bwai_v1_bp, url_prefix='/api/bwai/v1')

    return app
