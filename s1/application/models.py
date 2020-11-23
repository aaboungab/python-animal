from application import db
class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    noise = db.Column(db.String(30), nullable=False)
