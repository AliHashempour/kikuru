from flask import Flask, request, redirect
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


@app.route('/api/V1/<url_id>')
def shortened_url_handler(url_id):
    _id = url_id
    actual_url = utils.db_select(url_id=_id)
    if 'https://' in actual_url:
        return redirect(actual_url)
    else:
        return redirect(f"https://{actual_url}")
