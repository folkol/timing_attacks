import hashlib
import hmac
from base64 import b64decode
from functools import wraps

import jwt
from flask import Flask, request, jsonify

passwords = {'admin': 'password'}
SECRET = 'Very secret indeed!'

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    credentials = request.get_json(force=True)
    username, password = credentials.get('username'), credentials.get('password')

    if passwords.get('admin') != password:
        return jsonify(reason='Unauthorized!'), 401

    claims = {
        'genuine': 'Hell yeah!'
    }
    token = jwt.encode(claims, SECRET)
    return jsonify(token=token.decode('UTF-8')), 201


def secured(f):
    @wraps(f)
    def check_auth(*args, **kwargs):
        authorization_ = request.headers['Authorization']
        token = authorization_.split()[1]
        token = token.split('_')[0]
        header, claims, signature = token.split('.')

        print(header, claims, signature)

        digester = hmac.new(bytearray(SECRET, 'utf8'), digestmod=hashlib.sha256)
        digester.update(b64decode(header))
        digester.update(b64decode(claims))

        decode = b64decode(signature)
        if digester.digest() != decode:
            return jsonify(reason='Unauthorized!'), 401

        return f(*args, **kwargs)

    return check_auth


@app.route('/comments', methods=['POST'])
@secured
def comment():
    print('Adding comment!')
    return jsonify(message='Success!'), 201

app.run()
