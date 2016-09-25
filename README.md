# Timing attach on web server

- Flask/Python-server with timing vulnerability
- Node.js-client that tries to forge a valid JSWT-token.


## References:

- [`https://codahale.com/a-lesson-in-timing-attacks/`]()
- [`http://crypto.stanford.edu/~dabo/papers/ssl-timing.pdf`]()
- [`https://rdist.root.org/2009/05/28/timing-attack-in-google-keyczar-library/`]()
- [`http://saweis.net/crypto.html`]()
- [`https://nodejs.org/api/http.html#http_http_request_options_callback`]()
- [`https://tools.ietf.org/html/rfc7519`]()
- [`http://blog.apcelent.com/json-web-token-tutorial-example-python.html`]()
- [`https://en.wikipedia.org/wiki/Hash-based_message_authentication_code`]()
- [`http://flask.pocoo.org/docs/0.11/quickstart/`]()
- [`https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface`]()
- [`https://en.wikipedia.org/wiki/Digest_access_authentication`]()
- [`https://en.wikipedia.org/wiki/JSON_Web_Token`]()


### Constant time MessageDigest compare

- Python: ???
- Java: ???
- Node.js: ???



### Start server

    $ cd server
    $ python3 server.py # 3.4 or higher


### Curl example

    $ curl -XPOST http://localhost:5000/login -d '{"username":"admin", "password":"password"}'
    $ TOKEN=...
    $ curl -H"Authorization: Bearer $TOKEN" http://localhost:5000/comments -d '{"message":"Hello, World!"}'

### Start client

    $ cd client
    $ node 
