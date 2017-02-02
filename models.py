from views import db

class User(db.Model):
	
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique = True)
	password = db.Column(db.String(20), unique = False)
	todo_stuffs = db.relationship('todo_stuff', backref = 'user', lazy = 'dynamic')

	def __init__(self, password, username):
		self.password = password
		self.username = username

	def __repr__(self):
		return self.username

class todo_stuff(db.Model):
	
	id = db.Column(db.Integer, primary_key = True)
	stuff = db.Column(db.String(100), unique = False)
	time = db.Column(db.String(40), unique = False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	def __init__(self, stuff, time, user):
		self.stuff = stuff
		self.time = time
		self.user = user

	def __repr__(self):
		return self.stuff

