import models

def query():
	return models.todo_stuff.query.all()

def insert(stuff):
	new_stuff = models.todo_stuff(stuff = stuff)
	try:
		models.db.session.add(new_stuff)
		models.db.session.commit()
	except Exception as e:
		models.db.session.rollback()
		raise e

def delete():
	pass

