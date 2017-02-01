import models

def query_all():
	return models.todo_stuff.query.all()

def insert(stuff, time):
	new_stuff = models.todo_stuff(stuff = stuff,time = time)
	try:
		models.db.session.add(new_stuff)
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

