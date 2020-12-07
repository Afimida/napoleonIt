class AuthRetriever:
    session = None

    def __init__(self, session):
        self.session = session

    def authorization(self, username, password):
        return username
