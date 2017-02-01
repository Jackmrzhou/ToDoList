from views import db

class todo_stuff(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	stuff = db.Column(db.String(100), unique = False)
	time = db.Column(db.String(40), unique = False)

	def __repr__(self):
		return self.stuff