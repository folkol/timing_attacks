var request = require('request');

var req = {
    url: 'http://localhost:8080/comments/',
    headers: {
        Authorization: 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsZWdpdGltYXRlIjoiSGVsbCB5ZWFoISJ9.8Rgu4e6-q_mbzELrNfPv_iTQWxFGe816hmoYALPPCDY'
    },
    json: {
        message: "World domination!"
    }
};
request.post(req, function (x) {
    console.log(x);
});
