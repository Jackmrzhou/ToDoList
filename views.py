import forms
from flask import Flask,render_template,redirect,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object('config')
app.debug=True 
stuffs = []

@app.route('/', methods = ['GET','POST'])
def ToDo():
	global stuffs
	form = forms.thing()
	if not form.validate_on_submit():
		stuffs.append(form.stuff.data)
	return render_template('index.html',
		form = form,
		stuffs = stuffs)

if __name__ == '__main__':
	app.run()