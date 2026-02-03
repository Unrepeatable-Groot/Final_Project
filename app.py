from ext import app

if __name__ == "__main__":
    from routing import home, pc_page, laptops_page, pc_info, laptop_info, add_product, register, login, profile, remove_laptop, remove_pc, edit_laptop, edit_pc
    app.run(debug=True)