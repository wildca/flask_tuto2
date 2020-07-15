from flask import Flask

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_object('config')

#       --- DATABASE ---
#engine = create_engine('mysql://test:test@localhost:3306/test', echo=False)
engine = create_engine('sqlite:///db.sqlite3')
'''
    sqlite:///:memory: (or, sqlite://)
    sqlite:///relative/path/to/file.db
    sqlite:////absolute/path/to/file.db
'''
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# TEST:
from app import db_test
db_test.test_db()

#       --- DATABASE ---



from views import index, ajax_1, ajax_2, path_params, session, db_address, db_user

from model import User



