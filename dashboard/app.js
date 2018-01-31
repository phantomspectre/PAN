var express        = require('express')
  , bodyParser     = require('body-parser')
  , errorHandler   = require('errorhandler')
  , methodOverride = require('method-override')
  , morgan         = require('morgan')
  , http           = require('http')
  , path           = require('path')
  , db             = require('./models')
  , request        = require('request');

var app = express();
var dbOperations = require("./models/db.js");
//var logFmt = require("logfmt");

var urlencodedParser = bodyParser.urlencoded({ extended: false })

// all environments
app.set('port', process.env.PORT || 3000)
app.set('views', __dirname + '/views')
app.set('view engine', 'jade')
app.use(morgan('dev'))
app.use(bodyParser())
app.use(methodOverride())
app.use(express.static(path.join(__dirname, 'public')))
app.get('/' , function(req,res) {
    res.sendfile('public/index.html');
} );

app.get('/db/readRecords', function(req,res){
    dbOperations.getRecords(req,res);
});

app.get('/db/femRec', function(req,res){
    dbOperations.femRec(req,res);
});

app.get('/db/etaRec', function(req,res){
    dbOperations.etaRec(req,res);
});

app.get('/db/peopleRec/:imo', function(req,res){
//    console.log(req.params.imo)
    dbOperations.peopleRec(req,res);
});
// app.get('/db/weaponsRec/:imo', function(req,res){
//     dbOperations.weaponsRec(req,res);
// });
app.get('/db/person/:tdn', function(req,res){
    dbOperations.person(req,res);
});

app.post('/imo', function(req, res) {
    res.redirect('/db/peopleRec/'+req.body.imo)
});

app.post('/person', function(req, res) {
    res.redirect('/db/person/'+req.body.tdn)
});

// development only
if ('development' === app.get('env')) {
  app.use(errorHandler())
}

app.listen(app.get('port'), function () {
    console.log('Express server listening on port ' + app.get('port'));
});
