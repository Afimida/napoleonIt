from auth_database.model.Users import User
from sanic_jwt import exceptions


class AuthRetriever:
    session = None

    def __init__(self, session):
        self.session = session

    def authenticate(self, username, password, user_id):
        if not username or not password:
            raise exceptions.AuthenticationFailed("Missing username or password.")
        user = self.session.query(User).filter_by(name=username, id=user_id).first()
        user_data = user.to_json()
        if user is None:
            raise exceptions.AuthenticationFailed("User not found.")
        if password != user_data['password']:
            raise exceptions.AuthenticationFailed("Password is incorrect.")
        return user_data
