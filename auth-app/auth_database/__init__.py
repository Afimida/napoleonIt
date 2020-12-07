from auth_database.Database import Database
from auth_database.config import DB_SETTINGS as DB_CFG
from sqlalchemy.orm import sessionmaker
from auth_database.model import Users

db = Database(DB_CFG).connect()
Users.Base.metadata.create_all(db)
Session = sessionmaker(bind=db)
