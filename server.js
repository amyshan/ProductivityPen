/* Practice tutorial for deploying a web server using Node.JS
* http://blog.modulus.io/build-your-first-http-server-in-nodejs
* */

// //Lets require/import the HTTP module
// var http = require('http');
//
// //Lets define a port we want to listen to
// const PORT=8080;
//
// //We need a function which handles requests and send response
// function handleRequest(request, response){
//     response.end('It Works!! Path Hit: ' + request.url);
// }
//
// //Create a server
// var server = http.createServer(handleRequest);
//
// //Lets start our server
// server.listen(PORT, function(){
//     //Callback triggered when server is successfully listening. Hurray!
//     console.log("Server listening on: http://localhost:%s", PORT);
// });

/* MEAN Machine Node Server Demo
*   this version doesn't use Express, just barebones Node
* */
// var http = require('http')
//     fs = require('fs');
//
// http.createServer(function (req, res) {
//     res.writeHead(200, {
//         'Content-Type': 'text/html',
//         'Access-Control-Allow-Origin' : '*'
//     });
//
//     var readStream = fs.createReadStream(__dirname + '/index.html');
//
//     readStream.pipe(res);
//
// }).listen(1337);
//
// console.log('Site hosted on localhost:1337');

/* MEAN Machine Node Server Demo
 *   using Express
 * */
var express = require('express')
    app     = express();

app.get('/', function (req, res) {
    res.sendfile(__dirname + '/index.html');
})

app.listen(1337);
console.log('localhost:1337');