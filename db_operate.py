import models

def query_all(user):
	return user.todo_stuffs.all()

def query_user(username):
	user = models.User.query.filter_by(username = username).first()
	return user

def insert(stuff=None, time=None,user=None, username=None, password=None):
	if stuff and time and user:
		new = models.todo_stuff(stuff = stuff,time = time,user = user)
	elif username and password:
		new = models.User(password =password, username=username)
	try:
		models.db.session.add(new)
		models.db.session.commit()
	except Exception as e:
		models.db.session.rollback()
		raise e

def delete(stuff_id):
	stuff = models.todo_stuff.query.get(stuff_id)
	try:
		models.db.session.delete(stuff)
		models.db.session.commit()
	except Exception as e:
		models.db.session.rollback()
		raise e

def upgrade(stuff_id, new_stuff, new_time):
	pass