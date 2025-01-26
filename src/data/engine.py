from sqlalchemy import create_engine
from data import models
import os

# create an engine
current_path = os.path.dirname(os.path.realpath(__file__))
database_url = f"sqlite+pysqlite:///{current_path}/database.db"
engine = create_engine(database_url, echo=True)


