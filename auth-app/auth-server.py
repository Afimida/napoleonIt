from sanic import Sanic
from sanic.response import json as response_json
import logging
from settings import RESPONSE_HEADERS as HEADERS
from auth_api.RegistryRetriever import RegistryRetriever
from auth_api.AuthRetriever import AuthRetriever
from auth_api.UserRetriever import UserRetriever
from auth_database import Session

# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S', filename='/var/www/logs/auth-app.log', filemode='w')

app = Sanic('auth-server')
session = Session()


@app.route("/user/registry/", methods=['POST'])
async def registry(request):
    registration = RegistryRetriever(session).register_user(request.json['username'], request.json['password'],
                                                            request.json['email'])
    return response_json({"result": registration}, headers=HEADERS, status=registration['status'])


@app.route("/user/auth/", methods=['POST'])
async def auth(request, username, password):
    authorization = AuthRetriever(session).authorization(username, password)
    return response_json({'auth': authorization}, headers=HEADERS)


@app.route("/user/list/", methods=['POST'])
async def get_users(request):
    users = UserRetriever(session).list_users()
    return response_json({'user_data': users}, headers=HEADERS)


@app.route("/user/<user_id>/", methods=['GET'])
async def get_user(request, user_id):
    user = UserRetriever(session).user_data(user_id)
    return response_json({'response': user}, headers=HEADERS, status=user['status'])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
