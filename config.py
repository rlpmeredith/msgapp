import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SEECRET_KEY') or 'you-will-never-guess'
	SQLALCHEMY_DATABASE_URI = 'mysql://rob:harry5@127.0.0.1/msgdb'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
