from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
mail = Mail(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

tasks = [
    {
        'taskId': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'taskId': 2,
        'title': u'Learn Python',
        'description': u'Need to find good Python tutorial',
        'done': False
    }
]

posts = [
    {
        'author': {'username': 'Jane'},
        'body': 'Lean Chinese'
    },
    {
        'author': {'username': 'Thomas'},
        'body': 'Learn Flask-Python'
    }
]

from app import routes, models
