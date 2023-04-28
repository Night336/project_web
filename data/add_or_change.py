from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

from data import Base


class AddOrChangeForm(Base):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    brand = StringField('Brand', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    submit = SubmitField('Submit')
