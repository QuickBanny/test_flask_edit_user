import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	CSRF_ENABLED = True
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

	@staticmethod
	def init_app(app):
		pass
