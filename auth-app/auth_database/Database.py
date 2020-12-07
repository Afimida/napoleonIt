from sqlalchemy import create_engine
from auth_database.MetaSingleton import MetaSingleton


class Database(metaclass=MetaSingleton):
    connection = None
    user = None
    password = None
    host = None
    port = None
    database_name = None

    def __init__(self, db_cfg):
        self.user = db_cfg['user']
        self.password = db_cfg['password']
        self.host = db_cfg['host']
        self.port = db_cfg['port']
        self.database_name = db_cfg['db_name']

    def connect(self):
        if self.connection is None:
            self.connection = create_engine(
                f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database_name}',
                echo=False)
        return self.connection
