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
var express = require('express'),
    app     = express();

// basic route for home page
app.get('/', function (req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.listen(1337);
console.log('localhost:1337');

var adminRouter = express.Router();

// route middleware through router.use()
// happens every request
// order of route vs middleware is important; place middleware before routes
// useful to check if user has logged in before letting them continue
adminRouter.use(function (req, res, next) {
    console.log(req.method, req.url);
    // lets Express know that function is complete and can proceed with next
    // middleware or continue routing
    next();
});

// applied routes to instance of router; specified root dir as admin
adminRouter.get('/', function (req, res) {
    res.send('I am the dashboard');
});

adminRouter.get('/users', function (req, res) {
    res.send('I show all the users');
});

adminRouter.get('/posts', function(req, res) {
    res.send('I show all the posts');
});

// middleware for routes with params
adminRouter.param('name', function (req, res, next, name) {
    //do validation and something
    console.log('doing name validations on ' + name);
    //save new item in the req once validation is done
    req.name = name;
    next();
})

// routes with params
adminRouter.get('/users/:name', function(req, res) {
    res.send('hello ' + req.params.name + "!");
});

app.use('/admin', adminRouter);

app.route('/login')
    .get(function (req, res) {
        res.send('this is the login form');
    })
    .post(function (req, res) {
        console.log('processing');
        res.send('processing the login form!');
    });

var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/test');