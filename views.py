import forms
from flask import Flask,render_template,redirect,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.debug=True
db = SQLAlchemy(app)

import db_operate

@app.route('/', methods = ['GET','POST'])
def ToDo():
	form = forms.thing()
	stuffs = db_operate.query()
	if form.validate_on_submit():
		db_operate.insert(form.stuff.data +':'+ form.todo_time.data)
		return redirect('/')
	return render_template('index.html',
		form = form,
		stuffs = stuffs)

if __name__ == '__main__':
	app.run()