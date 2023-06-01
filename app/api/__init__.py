from flask import Flask, request
from flask_cors import CORS
import app.api.utils as utils

app = Flask(__name__)
CORS(app)


@app.route('/api/V1/url_request', methods=['post'])
def handler():
    request_body = request.json
    return request_body
