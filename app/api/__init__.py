from flask import Flask, request
from flask_cors import CORS
import app.api.utils as utils

app = Flask(__name__)
CORS(app)


@app.route('/api/V1/url_request', methods=['post'])
def handler():
    request_body = request.json
    requested_url = request_body['url']
    _id = utils.db_insert(request_url=requested_url)
    new_url = {"new_url": f"localhost:5000/api/V1/{_id}"}
    return new_url
