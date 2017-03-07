import os

from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

db_url = os.environ["DB_FULL_URL"]

Base = declarative_base()
engine = create_engine(db_url)
Postgres_DB_Session = orm.sessionmaker(bind=engine)

if not database_exists(engine.url):
    create_database(engine.url)


def recreate_metadata():
    Base.metadata.drop_all(engine)
    create_all_metadata()


def create_all_metadata():
    Base.metadata.create_all(engine)
