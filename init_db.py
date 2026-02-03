from ext import app, data_base
from models import PC, Laptop, User, PC_coments, Laptop_coments


with app.app_context():
    data_base.create_all()