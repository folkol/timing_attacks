import base64
import hashlib
from base64 import b64encode

from bottle import run, request, post, response
import hmac
import jwt

passwords = {'admin': 'password'}
SECRET = b'Very secret indeed'


@post('/login')
def index():
    username, password = request.json['username'], request.json['password']

    if passwords[username] != password:
        return unauthorized()

    token = jwt.encode({'legitimate': 'Hell yeah!'}, SECRET)

    return {'token': token.decode()}


@post('/comments/')
def comment():
    auth_header = request.headers['Authorization']

    if not validate_token(auth_header):
        return unauthorized()

    return {'message': 'Comment added!'}


def validate_token(auth_header):
    token = auth_header.split()[1]
    header, claims, signature = tuple(token.split('.'))


    # utils base64 encode
    # base64.urlsafe_b64encode(input).replace(b'=', b'')

    # base64_encode('')

    def encode(x):
        return base64.urlsafe_b64encode(x).replace(b'=', b'')

    alg = hashlib.sha256

    msg = header + '.' + claims
    digest = encode(hmac.new(SECRET, msg.encode('utf8'), digestmod=alg).digest())

    print(signature)
    # 'Nace+U3Az4OhN7tISqgs1vdLBHBEijWcBeCqL5xN9xg='

    return digest == bytes(signature, 'utf8')


def unauthorized():
    response.status = 401
    return {'reason': 'Not authenticated!'}


run()
