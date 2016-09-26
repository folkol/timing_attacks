from base64 import urlsafe_b64encode
from hashlib import sha256
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

    digester = hmac.new(SECRET, digestmod=sha256)
    digester.update(header.encode('utf8'))
    digester.update('.'.encode('utf8'))
    digester.update(claims.encode('utf8'))
    digest = digester.digest()

    calculated = urlsafe_b64encode(digest).replace(b'=', b'')
    posted = bytes(signature, 'utf8')

    return calculated == posted


def unauthorized():
    response.status = 401
    return {'reason': 'Not authenticated!'}


run()
