from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_ckeditor import CKEditor


bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
ck_editor = CKEditor()
mail = Mail()

