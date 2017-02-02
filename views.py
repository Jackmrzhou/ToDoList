import forms
from flask import Flask,render_template,redirect,flash, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.debug=True
db = SQLAlchemy(app)

import db_operate
import hash_password

@app.route('/', methods = ['GET','POST'])
def index():
	form = forms.thing()
	stuffs = db_operate.query_all()

	if request.form:
		f = request.form.to_dict()
		for stuff_id in f:
			if f[stuff_id] == '删除':
				db_operate.delete(stuff_id)
				return redirect('/')
			else:
				pass

	if form.is_submitted():
		if form.validate():
			db_operate.insert(stuff= form.stuff.data,
				time= form.time.data,
				user = user)
			#把这个坑填完
			return redirect('/')
		else:
			flash('Check Again!')

	return render_template('index.html',
		form = form,
		stuffs = stuffs)

@app.route('/register_login', methods = ['GET', 'POST'])
def login():
	form = forms.SigninForm()

	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		#以后再将密码加密
		db_operate.insert(username = username, password = password)
		return redirect('/')
		#填坑
	else:
		flash('Check Again!')

	return render_template('register_login.html',
		form = form)


if __name__ == '__main__':
	app.run()