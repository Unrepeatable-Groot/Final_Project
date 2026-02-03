from flask import Flask, render_template, redirect, flash
from ext import app, data_base
from models import PC, Laptop, User, PC_coments, Laptop_coments
from form import Add_product, Register_form, Login_form, Edit_laptop, Edit_pc, PC_Coments, Laptop_Coments, Edit_user
from sqlalchemy import func
from flask_login import login_user, logout_user, current_user



@app.route("/")
def home():  
    pc = PC.query.order_by(func.random()).limit(4).all()
    laptop = Laptop.query.order_by(func.random()).limit(4).all()
    return render_template("index.html", pc=pc, laptops=laptop)



@app.route("/PC's")
def pc_page():
    pc = PC.query.all()
    return render_template("pc_page.html", pc=pc)



@app.route("/Laptops")
def laptops_page():
    laptops = Laptop.query.all()
    return render_template("laptop.html", laptops=laptops)



@app.route("/PC_Info/<int:product_id>", methods=["GET", "POST"])
def pc_info(product_id):
    if not current_user.is_authenticated:
        return redirect("/")
    pc = PC.query.get(product_id)
    random_pc = PC.query.order_by(func.random()).limit(4).all()
    form = PC_Coments()
    user = User.query.get(current_user.id)
    if form.validate_on_submit():
        new_comment = PC_coments(coment = form.comment.data, post_id = pc.id, user_id = current_user.id)
        data_base.session.add(new_comment)
        data_base.session.commit()
        form.comment.data = ""
        return redirect(f"/PC_Info/{pc.id}")
    comments = PC_coments.query.all()
    users = []
    for coment in comments:
        user = User.query.get(coment.user_id)
        users.append(user)

        count = 0
        for user in users:
            for second_user in users:
                if user.id == second_user.id:
                    count += 1 
            if count > 1:
                users.remove(user)
                print(users)
            count = 0
    return render_template("pc_info.html", pc=pc, random_pc=random_pc, form=form, comments=comments, users=users)


@app.route("/delate_pc_comment/<int:comment_id>")
def delete_PC_Comment(comment_id):
    if not current_user.is_authenticated:
        return redirect("/") 
    comment = PC_coments.query.get(comment_id)
    data_base.session.delete(comment)
    data_base.session.commit()

    return redirect(f"/PC_Info/{comment.post_id}")



@app.route("/Laptop_Info/<int:product_id>", methods=["GET", "POST"])
def laptop_info(product_id):
    if not current_user.is_authenticated:
        return redirect("/")
    laptop = Laptop.query.get(product_id)
    random_laptop = Laptop.query.order_by(func.random()).limit(4).all()
    form = Laptop_Coments()
    user = User.query.get(current_user.id)
    if form.validate_on_submit():
        new_comment = Laptop_coments(coment = form.comment.data, post_id = laptop.id, user_id = current_user.id)
        data_base.session.add(new_comment)
        data_base.session.commit()
        form.comment.data = ""
        return redirect(f"/Laptop_Info/{laptop.id}")
    comments = Laptop_coments.query.all()
    users = []
    for coment in comments:
        user = User.query.get(coment.user_id)
        users.append(user)

        count = 0
        for user in users:
            for second_user in users:
                if user.id == second_user.id:
                    count += 1 
            if count > 1:
                users.remove(user)
                print(users)
            count = 0
    return render_template("laptop_info.html", laptop=laptop, random_laptop=random_laptop, form=form, comments=comments, users=users)


@app.route("/delate_laptop_comment/<int:comment_id>")
def delete_Laptop_Comment(comment_id):
    if not current_user.is_authenticated:
        return redirect("/") 
    comment = Laptop_coments.query.get(comment_id)
    data_base.session.delete(comment)
    data_base.session.commit()

    return redirect(f"/Laptop_Info/{comment.post_id}")



@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if not current_user.is_authenticated:
        return redirect("/")
    form = Add_product()
    if form.validate_on_submit():
        if form.category.data == "PC":
            new_pc = PC(image = form.image.data, motherboard = form.motherboard.data, processor = form.processor.data, power_block = form.power_block.data, 
                        cooler = form.cooler.data, video_card = form.video_card.data, ram = form.ram.data, case = form.case.data, ssd = form.ssd.data,
                        price = form.price.data, user_id = current_user.id)
            data_base.session.add(new_pc)
            data_base.session.commit()
            return redirect ("/profile")
        elif form.category.data == "Laptop":
            new_laptop = Laptop(image = form.image.data, processor = form.processor.data, video_card = form.video_card.data, ram = form.ram.data, 
                                screenResolution = form.screenResolution.data, screenHZ = form.screenHZ.data, ssd = form.ssd.data, price = form.price.data, 
                                brand = form.brand.data, user_id = current_user.id)
            data_base.session.add(new_laptop)
            data_base.session.commit()
            return redirect ("/profile")
    return render_template("add_product.html", form=form)



@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect("/")
    form = Register_form()
    if form.validate_on_submit():
        existing_user = User.query.filter(User.meil == form.meil.data).first()
        if not existing_user:
            new_user = User(user_name = form.user_name.data, surename = form.surename.data, age = form.age.data, meil = form.meil.data,
                            image = form.image.data, password = form.password.data, role = "user")
            data_base.session.add(new_user)
            data_base.session.commit()
            login_user(new_user)
            return redirect("/")
        else:
            flash("Email is already in use")
    return render_template("register.html", form=form)



@app.route("/log_in", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/")
    form = Login_form()
    if form.validate_on_submit():
        user = User.query.filter(User.meil == form.meil.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        else:
            flash("The password is incorrect")
            print(user.check_password(form.password.data))
    return render_template("login.html", form=form)


@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if not current_user.is_authenticated:
        return redirect("/")
    user = User.query.get(user_id)
    form = Edit_user(user_name=user.user_name, surename=user.surename, age=user.age, meil=user.meil, image=user.image)
    if form.validate_on_submit():
        user.user_name = form.user_name.data
        user.surename = form.surename.data
        user.age = form.age.data
        user.meil = form.meil.data
        user.image = form.image.data
        user.password = form.password.data

        data_base.session.commit()
        return redirect("/profile")

    return render_template("edit_user.html", form=form)



@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")
    


@app.route("/profile")
def profile():
    if not current_user.is_authenticated:
        return redirect("/")
    laptops = Laptop.query.filter(Laptop.user_id == current_user.id)
    pc = PC.query.filter(PC.user_id == current_user.id)
    print(current_user.age)
    return render_template("profile.html", laptops = laptops, pc = pc)



@app.route("/remove_laptop/<int:laptop_id>")
def remove_laptop(laptop_id):
    if not current_user.is_authenticated:
        return redirect("/")
    laptop = Laptop.query.get(laptop_id)
    data_base.session.delete(laptop)
    data_base.session.commit()

    return redirect("/profile")


@app.route("/remove_pc/<int:pc_id>")
def remove_pc(pc_id):
    if not current_user.is_authenticated:
        return redirect("/")
    pc = PC.query.get(pc_id)
    data_base.session.delete(pc)
    data_base.session.commit()

    return redirect("/profile")



@app.route("/edit_laptop/<int:laptop_id>", methods=["GET", "POST"])
def edit_laptop(laptop_id):
    if not current_user.is_authenticated:
        return redirect("/")
    laptop = Laptop.query.get(laptop_id)
    form = Edit_laptop(brand = laptop.brand, image = laptop.image, processor = laptop.processor, ssd = laptop.ssd, video_card = laptop.video_card, ram = laptop.ram,
                       screenResolution = laptop.screenResolution, screenHZ = laptop.screenHZ, price = laptop.price)
    if form.validate_on_submit():
        laptop.brand = form.brand.data
        laptop.image = form.image.data
        laptop.processor = form.processor.data
        laptop.ssd = form.ssd.data
        laptop.video_card = form.video_card.data
        laptop.ram = form.ram.data
        laptop.screenResolution = form.screenResolution.data
        laptop.screenHZ = form.screenHZ.data
        laptop.price = form.price.data

        data_base.session.commit()
        return redirect("/profile")

    return render_template("edit_laptop.html", form=form)



@app.route("/edit_pc/<int:pc_id>", methods=["GET", "POST"])
def edit_pc(pc_id):
    if not current_user.is_authenticated:
        return redirect("/")
    pc = PC.query.get(pc_id)
    form = Edit_pc(image = pc.image, motherboard = pc.motherboard, processor = pc.processor, ssd = pc.ssd, power_block = pc.power_block, 
                       cooler = pc.cooler, video_card = pc.video_card, ram = pc.ram, case = pc.case, price = pc.price)
    if form.validate_on_submit():
        pc.image = form.image.data
        pc.motherboard = form.motherboard.data
        pc.processor = form.processor.data
        pc.ssd = form.ssd.data
        pc.power_block = form.cooler.data
        pc.cooler = form.power_block.data
        pc.video_card = form.video_card.data
        pc.ram = form.ram.data
        pc.case = form.case.data
        pc.price = form.price.data

        data_base.session.commit()
        return redirect("/profile")

    return render_template("edit_pc.html", form=form)