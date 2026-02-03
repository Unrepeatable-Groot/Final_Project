from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, RadioField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, equal_to

class Add_product(FlaskForm):
    category = RadioField("Select a type", choices=["PC","Laptop"], validators=[DataRequired()])
    image = StringField("Image", validators=[DataRequired()])
    motherboard = StringField("Motherboard")
    processor = StringField("Processor", validators=[DataRequired()])
    ssd = StringField("SSD", validators=[DataRequired()])
    power_block = StringField("Power Block")
    cooler = StringField("Cooling")
    video_card = StringField("Video Card", validators=[DataRequired()])
    ram = StringField("RAM", validators=[DataRequired()])
    screenResolution = StringField("Screen Resolution")
    screenHZ = StringField("Screen HZ")
    case = StringField("Case")
    brand = StringField("Brand")
    price = IntegerField("Price", validators=[DataRequired()])

    save = SubmitField("ატვირთვა")  


class Register_form(FlaskForm):
    user_name = StringField("შეიყვანეთ სახელი", validators=[DataRequired()])
    surename = StringField("შეიყვანეთ გვარი", validators=[DataRequired()])
    age = IntegerField("შეიყვანეთ ასაკი", validators=[DataRequired()])
    meil = StringField("შეიყვანეთ იმეილი", validators=[DataRequired()])
    image = StringField("შეიყვანეთ ფოტოს ლინკი", validators=[DataRequired()])
    password = PasswordField("შეიყვანეთ პაროლი", validators=[DataRequired(), Length(min=8, max=32)])
    repeat_password = PasswordField("გაიმეორეთ პაროლი", validators=[DataRequired(), equal_to("password", message="Passwords do not match")])

    save = SubmitField("დარეგისტრირება")

class Login_form(FlaskForm):
    meil = StringField("შეიყვანეთ იმეილი", validators=[DataRequired()])
    password = PasswordField("შეიყვანეთ პაროლი", validators=[DataRequired()])

    save = SubmitField("შესვლა")


class Edit_user(FlaskForm):
    user_name = StringField("შეიყვანეთ სახელი", validators=[DataRequired()])
    surename = StringField("შეიყვანეთ გვარი", validators=[DataRequired()])
    age = IntegerField("შეიყვანეთ ასაკი", validators=[DataRequired()])
    meil = StringField("შეიყვანეთ იმეილი", validators=[DataRequired()])
    image = StringField("შეიყვანეთ ფოტოს ლინკი", validators=[DataRequired()])
    password = PasswordField("შეიყვანეთ პაროლი", validators=[DataRequired(), Length(min=8, max=32)])
    repeat_password = PasswordField("გაიმეორეთ პაროლი", validators=[DataRequired(), equal_to("password", message="Passwords do not match")])

    save = SubmitField("შენახვა")



class Edit_pc(FlaskForm):
    image = StringField("Image", validators=[DataRequired()])
    motherboard = StringField("Motherboard", validators=[DataRequired()])
    processor = StringField("Processor", validators=[DataRequired()])
    ssd = StringField("SSD", validators=[DataRequired()])
    power_block = StringField("Power Block", validators=[DataRequired()])
    cooler = StringField("Cooling", validators=[DataRequired()])
    video_card = StringField("Video Card", validators=[DataRequired()])
    ram = StringField("RAM", validators=[DataRequired()])
    case = StringField("Case", validators=[DataRequired()])
    price = IntegerField("Price", validators=[DataRequired()])

    save = SubmitField("ატვირთვა") 


class Edit_laptop(FlaskForm):
    image = StringField("Image", validators=[DataRequired()])
    processor = StringField("Processor", validators=[DataRequired()])
    ssd = StringField("SSD", validators=[DataRequired()])
    video_card = StringField("Video Card", validators=[DataRequired()])
    ram = StringField("RAM", validators=[DataRequired()])
    screenResolution = StringField("Screen Resolution")
    screenHZ = StringField("Screen HZ", validators=[DataRequired()])
    brand = StringField("Brand", validators=[DataRequired()])
    price = IntegerField("Price", validators=[DataRequired()])

    save = SubmitField("ატვირთვა")  


class PC_Coments(FlaskForm):
    comment = TextAreaField(validators=[DataRequired()])
    save = SubmitField()  


class Laptop_Coments(FlaskForm):
    comment = TextAreaField(validators=[DataRequired()])
    save = SubmitField()  
