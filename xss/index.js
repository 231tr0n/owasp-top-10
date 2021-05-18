const session = require('express-session');
const express = require('express');
const bp = require('body-parser');
const path = require('path');

var app = express();
app.set('view engine', 'ejs');

app.use(session({
    secret: 'o3D!=d8<K<uR6h?g4>R?x==x6SKU"#',
    resave: true,
    saveUninitialized: true
}));

app.use(bp.urlencoded({extended : true}));

app.use(bp.json());

var publicDir = require('path').join(__dirname,'/');
app.use(express.static(publicDir));

app.get('/', function(req, res) {
     res.sendFile(__dirname + '/homepage.html');
});

app.listen(8080);
