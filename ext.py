from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "dn3872309jdsaknjd0182s"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

data_base = SQLAlchemy(app)
login_manager = LoginManager(app)