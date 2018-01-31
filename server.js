var express = require('express');
var app = express();
var  os = require('os')
app.get('/', function (req, res) {
   res.send(`'Hello World '+${os.hostname()}`);
})

var server = app.listen(8081, function () {

  var host = server.address().address
  var port = server.address().port

  console.log("server running  on http://%s:%s", host, port)

})
