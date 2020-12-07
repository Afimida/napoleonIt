from sanic import Sanic
from sanic.response import json as response_json
import logging
from settings import RESPONSE_HEADERS as HEADERS
from offers_api.CreateRetriever import CreateRetriever
from offers_database import Session

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S', filename='/var/www/logs/auth-app.log', filemode='w')

app = Sanic('offer-server')


@app.route("/offer/create/", methods=['POST'])
async def create(request):
    session = Session()
    return response_json({"result": 'create'}, headers=HEADERS, status=200)


@app.route("/offer/", methods=['GET'])
async def offer(request):
    session = Session()
    return response_json({'auth': 'offer'}, headers=HEADERS, status=200)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8001)
