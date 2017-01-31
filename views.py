import forms
from flask import Flask,render_template,redirect,flash, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.debug=True
db = SQLAlchemy(app)

import db_operate

@app.route('/', methods = ['GET','POST'])
def ToDo():
	form = forms.thing()
	stuffs = db_operate.query_all()
	if form.validate_on_submit():
		db_operate.insert(form.stuff.data +':\t'+ form.todo_time.data)
		return redirect('/')

	if request.form:
		f = request.form
		for stuff_id in f.keys():
			db_operate.delete(stuff_id)
		return redirect('/')
		
	return render_template('index.html',
		form = form,
		stuffs = stuffs)

if __name__ == '__main__':
	app.run()