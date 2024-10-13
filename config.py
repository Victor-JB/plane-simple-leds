import os
import random

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.getenv("SECRET_KEY") or "".join([chr(random.randint(65, 92)) for _ in range(50)])
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
