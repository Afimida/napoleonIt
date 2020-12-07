from offers_database.Database import Database
from offers_database.config import DB_SETTINGS as DB_CFG
from sqlalchemy.orm import sessionmaker
from offers_database.model import Offers

db = Database(DB_CFG).connect()
Offers.Base.metadata.create_all(db)
Session = sessionmaker(bind=db)
