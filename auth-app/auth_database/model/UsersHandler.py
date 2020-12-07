from sqlalchemy.exc import SQLAlchemyError
from auth_database.RowsToDict import RowsToDict
from auth_database.model.Users import User


class UsersHandler:

    def get_users_list(self, session):
        generator = RowsToDict()
        users = generator.generate_list(session.query(User).all())
        return users

    def get_user(self, session, user_id):
        generator = RowsToDict()
        user = generator.generate_list(session.query(User).filter_by(id=user_id).all())
        if not user:
            return None
        else:
            return user