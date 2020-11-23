from application import db
from application.models import Animal

db.drop_all()
db.create_all()
