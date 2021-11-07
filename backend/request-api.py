from flask import Flask, jsonify, request
from flask_cors import CORS
import api

app = Flask(__name__)
CORS(app)


@app.route('/api/<user_name>', methods=['GET'])
def get(user_name):
    return jsonify(api.get_user(user_name))


@app.route('/post', methods=['POST'])
def post():
    return jsonify(api.get_user(request.get_json()['name']))


@app.route('/getRepo/<user_name>', methods=['GET'])
def ok(user_name):
    return jsonify(api.getUserRepoList(user_name))


@app.route('/post_data', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        data = request.json['key']
        api.get_repo(jsonify(data)[])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
