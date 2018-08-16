"""Define the models to be used in this application."""

from peewee import *

import datetime


db = SqliteDatabase('my_database.db')

class BaseModel(Model):

    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()


class Item(BaseModel):
    user = ForeignKeyField(User, backref='items')
    create_date = DateTimeField(default=datetime.datetime.now())
    is_complete = BooleanField(default=False)
    description = TextField()
