from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from .views import views
app.register_blueprint(views)
from .auth import auth
app.register_blueprint(auth)