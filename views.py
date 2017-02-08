import forms
from flask import Flask,render_template,redirect,flash, request,session
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.debug = True
db = SQLAlchemy(app)

import db_operate
import hash_password

global_user = None

def is_user(func):
	@wraps(func)
	def wrapper(*args, **kw):
		if 'username' not in session:
			return redirect('/login')
		return func(*args, **kw)
	return wrapper


@app.route('/', methods = ['GET','POST'])
@is_user
def index():
	now_user = db_operate.query_user(session['username'])
	form = forms.thing()
	stuffs = db_operate.query_all(user = now_user)

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
				user = now_user)
			return redirect('/')
		else:
			flash('Check Again!')

	return render_template('index.html',
		form = form,
		stuffs = stuffs,
		username = now_user.username)

@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = forms.RegisterForm()

	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		repeat_password = form.repeat_password.data
		#以后再将密码加密
		if password == repeat_password:
			db_operate.insert(username = username, password = password)
			session['username'] = username
			return redirect('/')
		else:
			flash('Check Again!')
	elif form.is_submitted():
		flash('Check Again!')

	return render_template('register.html',
		form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = forms.SigninForm()

	if request.form.get('register'):
		return redirect('/register')

	if form.is_submitted():
		if form.validate():
			user = db_operate.query_user(form.username.data)
			if user:
				if form.password.data == user.password:
					session['username'] = form.username.data
					return redirect('/')
				else:
					flash('Password is not correct!')
					return redirect('/login')
			else:
				flash('Username not found!')
				return redirect('/login')
		else:
			flash('Username and Password must between 6 and 20!')
			return redirect('/login')
	return render_template('login.html',
		form = form)

@app.route('/logout', methods =['GET'])
def logout():
	session.pop('username', None)
	return redirect('/login')

if __name__ == '__main__':
	app.run()