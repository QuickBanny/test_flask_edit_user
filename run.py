# #!flask/bin/python

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import Config 

from app import app, db
from app.models import User

# app.config.from_object(Config)

migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()


@manager.command
def create_admin():
    """Creates the admin user."""
    db.session.add(User(
        email="ad@min.com",
        password="admin",
        admin=True,
        confirmed=True)
    )
    db.session.commit()

if __name__ == '__main__':
    manager.run()