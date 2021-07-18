from flask import Flask, render_template
import os

from settings import config
from blueprints.auth import auth_bp
from blueprints.admin import admin_bp
from blueprints.blog import blog_bp
from extensions import bootstrap, db, mail, moment, ck_editor


def creat_app(config_name=None):
	"""
	:param config_name:
	:return:
	"""
	if config_name is None:
		config_name = os.getenv("FLASK_CONFIG", "development")

	app = Flask('bluelog')
	app.config.from_object(config[config_name])

	register_logging(app)  # 注册日志处理器
	register_extensions(app)
	register_blueprints(app)
	register_commands(app)
	register_errors(app)
	register_shell_context(app)
	register_template_context(app)

	return app


def register_logging(app):
	pass


def register_extensions(app):
	bootstrap.init_app(app)
	db.init_app(app)
	moment.init_app(app)
	ck_editor.init_app(app)
	mail.init_app(app)


def register_blueprints(app):
	app.register_blueprint(blog_bp)
	app.register_blueprint(admin_bp, url_prefix='/admin')
	app.register_blueprint(auth_bp, url_prefix='/auth')


def register_shell_context(app):
	@app.shell_context_processor
	def make_shell_context():
		return dict(db=db)


def register_template_context(app):
	pass


def register_errors(app):
	@app.errorhandler(400)
	def bad_request(e):
		return render_template('errors/400.html'), 400


def register_commands(app):
	pass


