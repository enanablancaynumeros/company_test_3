from api.wsgi import app
from flask_script import Manager

from db_handlers.postgres_config import create_all_metadata, recreate_metadata

manager = Manager(app)


@manager.command
def db_recreate():
    recreate_metadata()


@manager.command
def db_create_all():
    create_all_metadata()


if __name__ == "__main__":
    manager.run()
