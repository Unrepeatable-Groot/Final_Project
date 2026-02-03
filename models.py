from ext import data_base, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class PC(data_base.Model):
    __tablename__ = "pc"

    id = data_base.Column(data_base.Integer(), primary_key=True)
    image = data_base.Column(data_base.String())
    motherboard = data_base.Column(data_base.String())
    processor = data_base.Column(data_base.String())
    ssd = data_base.Column(data_base.String())
    power_block = data_base.Column(data_base.String())
    cooler = data_base.Column(data_base.String())
    video_card = data_base.Column(data_base.String())
    ram = data_base.Column(data_base.String())
    case = data_base.Column(data_base.String())
    price = data_base.Column(data_base.Integer())
    user_id = data_base.Column(data_base.Integer())


class Laptop(data_base.Model):
    __tablename__ = "laptop"

    id = data_base.Column(data_base.Integer(), primary_key=True)
    brand = data_base.Column(data_base.String())
    image = data_base.Column(data_base.String())
    processor = data_base.Column(data_base.String())
    ssd = data_base.Column(data_base.String())
    video_card = data_base.Column(data_base.String())
    ram = data_base.Column(data_base.String())
    screenResolution = data_base.Column(data_base.String())
    screenHZ = data_base.Column(data_base.String())
    price = data_base.Column(data_base.Integer())
    user_id = data_base.Column(data_base.Integer())


class User(data_base.Model, UserMixin):
    __tablename__ = "user"

    id = data_base.Column(data_base.Integer(), primary_key=True)
    user_name = data_base.Column(data_base.String())
    surename = data_base.Column(data_base.String())
    age = data_base.Column(data_base.Integer())
    meil = data_base.Column(data_base.String())
    image = data_base.Column(data_base.String())
    password = data_base.Column(data_base.String())
    role = data_base.Column(data_base.String())

    def __init__(self, user_name, surename, age, meil, image, password, role):
        self.user_name = user_name
        self.surename = surename
        self.age = age
        self.meil = meil
        self.image = image
        self.password = generate_password_hash(password)
        self.role = role
        
    def check_password(self, password):
        return check_password_hash(self.password, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class PC_coments(data_base.Model):
    __tablename__ = "coments"

    id = data_base.Column(data_base.Integer(), primary_key=True)
    coment = data_base.Column(data_base.String())
    post_id = data_base.Column(data_base.Integer())
    user_id = data_base.Column(data_base.Integer())


class Laptop_coments(data_base.Model):
    __tablename__ = "laptop_coments"

    id = data_base.Column(data_base.Integer(), primary_key=True)
    coment = data_base.Column(data_base.String())
    post_id = data_base.Column(data_base.Integer())
    user_id = data_base.Column(data_base.Integer())