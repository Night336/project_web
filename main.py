import os

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, current_user, login_user, login_required, logout_user

from accessor import Accessor
from api_v1 import api_v1_bp
from forms.add_brand import BrandForm
from forms.add_category import CategoryForm
from forms.login import LoginForm
from forms.product_form import ProductForm
from forms.registration import RegistrationForm

app = Flask(__name__)
accessor = Accessor("sqlite:///db//my_database.db")
api_v1_bp.accessor = accessor
app.register_blueprint(api_v1_bp)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        user = accessor.get_user_by_email(form.email.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        return redirect(url_for('main'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = accessor.get_user_by_email(form.email.data)
        if not user:
            accessor.create_user(form.email.data, form.password.data)
            return redirect(url_for('login'))
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@login_manager.user_loader
def load_user(user_id):
    return accessor.get_user_by_id(user_id)


@app.route('/')
@app.route('/main')
def main():
    categories = accessor.get_all_categories()
    products = accessor.get_all_product()
    reviews = []
    posts = []
    return render_template("main.html", categories=categories, products=products, reviews=reviews, posts=posts,
                           title="Главная страница")


@app.route('/category/<int:id>')
def category(id):
    categories = accessor.get_all_categories()
    products = accessor.get_all_product_by_category(id)
    return render_template("category_page.html", categories=categories, products=products)


@app.route('/product/<int:id>')
def product(id):
    name = accessor.get_name_by_id(id)
    price = accessor.get_price_by_id(id)
    return ""  # render_template("productum.html", name=name, price=price)


@app.route('/products')
def pros():
    categories = accessor.get_all_categories()
    products = accessor.get_all_product()
    return render_template("all_products.html", categories=categories, products=products)


@app.route('/order')
def order():
    return render_template("orders.html")


@app.route('/add_to_cart', methods=["POST"])
def add_to_cart():
    accessor.create_orders(int(request.form.get('quantity')), current_user.id, int(request.form.get('product_id')))
    return redirect("/products")


@app.route('/product/add', methods=['GET', 'POST'])
@login_required
def add_product():
    if current_user.role != 1:
        return redirect(url_for('main'))
    form = ProductForm(accessor.get_all_brands(), accessor.get_all_categories())
    if form.validate_on_submit():
        image = request.files['image']

        print(request.form)
        product = accessor.create_product_from_form(request.form)
        path = os.path.join(app.static_folder, 'images', str(product.id) + ".jpg")
        image.save(path)
        path = 'images/' + str(product.id) + ".jpg"
        print(path)
        product.image = path
        accessor.session.commit()

        flash('Product added successfully!', 'success')
        return redirect(url_for('main'))
    return render_template('add_product.html', form=form)


@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('main'))


@app.route('/brand/add', methods=['GET', 'POST'])
@login_required
def add_brand():
    if current_user.role != 1:
        return redirect(url_for('main'))
    form = BrandForm()
    if form.validate_on_submit():
        accessor.create_brand(name=form.name.data)
        flash('Your brand has been added!', 'success')
        return redirect(url_for('add_brand'))
    return render_template('add_brand.html', title='Add Brand', form=form)


@app.route('/category/add', methods=['GET', 'POST'])
def add_category():
    if current_user.role != 1:
        return redirect(url_for('main'))
    form = CategoryForm()
    if form.validate_on_submit():
        accessor.create_category(name=form.name.data, description=form.description.data)
        return redirect(url_for('add_category'))
    return render_template('add_category.html', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

