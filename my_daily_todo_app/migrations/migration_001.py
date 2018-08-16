from ..models import db, Item, User


db.connect()
db.create_tables([User, Item])
db.close()
