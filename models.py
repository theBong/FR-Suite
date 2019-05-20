
import datetime as dt
from peewee import *
db = SqliteDatabase('crowd.db')

class Person(Model):
	'''Name, ID assigned, path to face,time of registration, history of person movement ,zones allowed'''
	name = TextField()
    identity = TextField(unique = True)
	path_to_face = TextField(unique = True)
	registration_time = DateField(default=dt.datetime.now)
    history

	class Meta:
		database = db


	
def initialize():
	db.connect()
	db.create_tables([People], safe = True)
	db.close()