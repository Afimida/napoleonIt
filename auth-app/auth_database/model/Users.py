from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return self

    def serialize(self, values_only=False):
        if values_only:
            return self.__dict__.values()
        return self.__dict__

    def to_json(self):
        return dict(id=self.id,
                    name=self.name,
                    email=self.email,
                    password=self.password)
