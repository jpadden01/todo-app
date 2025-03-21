from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "ENTER YOUR SECRET KEY"
db = SQLAlchemy()

from .views import views
app.register_blueprint(views)
from .auth import auth
app.register_blueprint(auth)

from .models import User

db.init_app(app)
with app.app_context():
    db.create_all()