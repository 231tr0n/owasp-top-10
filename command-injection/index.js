const session = require('express-session');
const express = require('express');
const bp = require('body-parser');
const path = require('path');
const { exec } = require("child_process");

var app = express();
app.set("view engine", "ejs");

let item_id = "";
let item_stock = 0;
app.use(session({
	secret: 'o3D!=d8<K<uR6h?g4>R?x==x6SKU"#',
	resave: true,
	saveUninitialized: true
}));

app.use(bp.urlencoded({extended : true}));

app.use(bp.json());

var publicDir = require('path').join(__dirname, '/');
app.use(express.static(publicDir));

app.get('/', function(req, res) {
	console.log("Hello");
	res.render(path.join(__dirname + '/homepage.ejs'), {submitted:false, stock_number:0});
});

app.post('/get_items_stock', function(req, res) {
	item_id = req.body.items;
	exec("cat zeltron.txt | grep " + item_id, (error, stdout, stderr) => {
		if (error) {
			console.log(`error: ${error.message}`);
			return;
		}
		if (stderr) {
			console.log(`stderr: ${stderr}`);
			return;
		}
		arr = stdout.split(" ");
		item_stock = arr[1].slice(0, -1);
	});
	res.redirect("/information");
});

app.get('/information', function(req, res) {
	res.render(__dirname + "/homepage.ejs", {submitted:true, stock_number:item_stock});
});

app.listen(8080);
