from auth_database.model.UsersHandler import UsersHandler
from auth_services.Offers import Offers


class UserRetriever:
    model_handler = None
    service_handler = None
    session = None

    def __init__(self, session):
        self.model_handler = UsersHandler()
        self.service_handler = Offers()
        self.session = session

    def list_users(self):
        data = self.model_handler.get_users_list(self.session)
        return data

    def user_data(self, user_id):
        try:
            user = self.model_handler.get_user(self.session, user_id)
            offers = self.service_handler.get_offer_by_user_id(user_id)
            status = 200
            if not user:
                status = 404
                user = "User not found"
            if not offers:
                offers = "This user has no offers."
            result = {'user_info': user,
                      'user_offers': offers,
                      'status': status}
            return result
        except NameError:
            status = 500
            user = None
            offers = None
            result = {'user_info': user,
                      'user_offers': offers,
                      'status': status}
            return result
