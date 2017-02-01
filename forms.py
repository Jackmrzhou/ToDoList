from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length

class thing(FlaskForm):
	stuff = StringField('name of stuff', validators=[Length(min = 1,max = 20)])
	time=StringField('todo time', validators=[Length(min = 0,max = 20)])