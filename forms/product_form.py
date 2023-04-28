from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, SelectField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description')
    price = StringField('Price')
    image = FileField('Image', validators=[DataRequired()])
    brand = SelectField('Brand', choices=[], coerce=int)
    category = SelectField('Category', choices=[], coerce=int)
    submit = SubmitField('Submit')

    def __init__(self, brands_choices, categories_choices, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.brand.choices = [(brand.id, brand.name) for brand in brands_choices]
        self.category.choices = [(category.id, category.name) for category in categories_choices]
