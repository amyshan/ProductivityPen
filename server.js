/*
/!* MEAN Machine Node Server Demo
 *   using Express
 * *!/
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
mongoose.connect('mongodb://localhost/test');*/

// CALL THE PACKAGES
var express  = require('express'),
    app      = express(),
    bodyParser= require('body-parser'),
    morgan   = require('morgan'),
    mongoose = require('mongoose'),
    port     = process.env.PORT || 8080; // sets up localhost port

// APP CONFIGURATION
// bodyParser grabs info from POST requests
app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json());

// configure app to handle CORS requests
app.use(function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With, content-type, Authorization');
    next();
});

app.use(morgan('dev'));

// ROUTES FOR OUR API

// basic route for home page
app.get('/', function (req, res) {
    res.send('Welcome to the home page!');
});

// instance of Express router
var apiRouter = express.Router();

// test route at GET http://localhost:8080/api
apiRouter.get('/', function(req, res) {
    res.json({ message: 'hooray! welcome to our api!' });
});

// add more routes here in the future

// REGISTER OUR ROUTES
app.use('/api', apiRouter);

// START SERVER
app.listen(port);
console.log('Magic happens on port ' + port);

// START DATABASE
var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('pen.db');

db.serialize(function() {
    db.run("CREATE TABLE lorem (info TEXT)");

    var stmt = db.prepare("INSERT INTO lorem VALUES (?)");
    for (var i = 0; i < 10; i++) {
        stmt.run("Ipsum " + i);
    }
    stmt.finalize();

    db.each("SELECT rowid AS id, info FROM lorem", function(err, row) {
        console.log(row.id + ": " + row.info);
    });
});

db.close();
