from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Offers(Base):
    __tablename__ = 'auth_services'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(String)
    user_id = Column(Integer)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return self
