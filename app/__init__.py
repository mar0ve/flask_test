from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:12345@localhost:3306/flask_db_test"
app.config['POSTS_PER_PAGE'] = 5
app.config['SECRET_KEY'] = '1234567890'
# MAIL REQUIRMENTS
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email_here'
app.config['MAIL_PASSWORD'] = 'your_password_here'
app.config['ADMINS'] = ['admin_email_here',]

db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = 'login'


from app import routes, models, errors