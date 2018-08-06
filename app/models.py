from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# from . import db, login_manager


class User(db.Model, UserMixin):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	password_hash = db.Column(db.String(128))
	email = db.Column(db.String(64), unique=True, index=True)
	confirmed = db.Column(db.Boolean, default=False)
	admin = db.Column(db.Boolean, nullable=False, default=False)

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')
	
	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def varify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def to_json(self):
		json_user = {
			'url': url_for('get_user', id=self.id),
			'email': self.email
		}
		return json_user

	def __repr__(self):
		return 'User %r' % self.email 
