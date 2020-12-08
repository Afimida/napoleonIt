from auth_database.model.Users import User


class RegistryRetriever:
    session = None

    def __init__(self, session):
        self.session = session

    def register_user(self, username, password, email):
        user = User(name=username, email=email, password=password)
        self.session.add(user)
        self.session.commit()
        status = 200
        result = {'registry': user,
                  'status': status}
        return result
