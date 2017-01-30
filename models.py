from views import db

class todo_stuff(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	stuff = db.Column(db.String(80), unique = True)

	def __repr__(self):
		return '<Stuff: %s>' %self.stuff