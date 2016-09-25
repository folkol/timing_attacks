from bottle import route, run, template, request, post, abort, response
import jwt

passwords = {'admin': 'password'}
SECRET = 'Very secret indeed'


@post('/login')
def index():
    username, password = request.json['username'], request.json['password']

    if passwords[username] != password:
        response.status = 401
        return {'reason': 'Not authenticated!'}

    token = jwt.encode({'legitimate': 'Hell yeah!'}, SECRET)

    return {'token': token.decode()}


@post('/comments/')
def comment():
    pass


run()
