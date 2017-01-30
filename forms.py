from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class thing(FlaskForm):
	stuff = StringField('name of stuff', validators=[DataRequired()])