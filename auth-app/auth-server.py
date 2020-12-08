from sanic import Sanic
from sanic.response import json as response_json
from settings import RESPONSE_HEADERS as HEADERS
from auth_api.RegistryRetriever import RegistryRetriever
from auth_api.AuthRetriever import AuthRetriever
from auth_api.UserRetriever import UserRetriever
from auth_database import Session
from sanic_jwt import Initialize, protected
from swagger_ui import sanic_api_doc

session = Session()


async def authenticate(request, *args, **kwargs):
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user_id = request.json.get('user_id', None)
    user = AuthRetriever(session).authenticate(username, password, user_id)
    return user


app = Sanic('auth-server')
sanic_api_doc(app, config_path='./swagger/swagger.yaml', url_prefix='/swagger', title='API doc', editor=True)

Initialize(
    app,
    authenticate=authenticate,
    url_prefix='/user',
    path_to_authenticate='/auth',
    path_to_retrieve_user='/retrieve-user',
    path_to_verify='/verify',
    path_to_refresh='/refresh',
)


@app.route("/user/registry/", methods=['POST'])
async def registry(request):
    registration = RegistryRetriever(session).register_user(request.json['username'], request.json['password'],
                                                            request.json['email'])
    return response_json({"result": registration}, headers=HEADERS, status=registration['status'])


@app.route("/user/list/", methods=['POST'])
@protected()
async def get_users(request):
    users = UserRetriever(session).list_users()
    return response_json({'user_data': users}, headers=HEADERS)


@app.route("/user/<user_id>/", methods=['GET'])
@protected()
async def get_user(request, user_id):
    user = UserRetriever(session).user_data(user_id)
    return response_json({'response': user}, headers=HEADERS, status=user['status'])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
