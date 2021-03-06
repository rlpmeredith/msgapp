import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	SQLALCHEMY_DATABASE_URI = 'mysql://rob:$DB_PASSWORD@127.0.0.1/msgdb'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
