const mysql = require("mysql");
const session = require("express-session");
const express = require("express");
const bp = require("body-parser");
const mailsender = require("nodemailer");
const path = require("path");
const fs = require("fs");

let capcha = 0;
let file_name_array = [];

var app = express();
app.set("view engine", "ejs");

function random_string(length) {
     var random_string = '';
     var characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
     var characters_string_length = characters.length;
     for (var i = 0; i < length; i ++) {
          random_string += characters.charAt(Math.floor(Math.random() * characters_string_length));
     }
     return random_string;
}

function random_number(length) {
     var random_number = '';
     var characters = '0123456789';
     var characters_number_length = characters.length;
     for (var i = 0; i < length; i ++) {
          random_number += characters.charAt(Math.floor(Math.random() * characters_number_length));
     }
     return random_number;
}

app.use(session({
    secret: 'skndcvksdnavkbasdvbasdkvisdavbsdbasdkbvidasncfiweubviasdv',
    resave: true,
    saveUninitialized: true
}));

app.use(bp.urlencoded({extended : true}));

app.use(bp.json());

var publicDir = require('path').join(__dirname, '/');
app.use(express.static(publicDir));

var connection = mysql.createConnection({host:'localhost', user:'root', password:'', database:'zeltron'});

app.get('/', function(req, res) {
     res.sendFile(path.join(__dirname + '/lgorsppage.html'));
});

app.post('/signin', function(req, res) {
     res.redirect('/signininfo');
});

app.post('/signup', function(req, res) {
     res.redirect('/signupinfo');
});

app.get('/signininfo', function(req, res) {
     if (!fs.existsSync("dumby")) {
          fs.mkdirSync("dumby");
     }
     if (file_name_array.length != 0) {
          file_name_array.forEach(function (item) {
               fs.unlinkSync("./dumby/" + item + ".png");
          });
     }
     let destination = "./dumby/";
     let origin = "./pictures/";
     let dumby_destination = "";
     let dumby_origin = "";
     let dummy = "";
     let remainder = 0;
     file_name_array.length = 0;
     let r = random_number(5);
     capcha = r;
     console.log("The Capcha Code is: " + r);
     while(r > 0) {
          remainder = r % 10;
          r = Math.floor(r / 10);
          dumby_origin = origin + remainder.toString() + ".png";
          dummy = random_string(5);
          file_name_array.push(dummy);
          dumby_destination = destination + dummy + ".png";
          fs.copyFileSync(dumby_origin, dumby_destination);
     }
     file_name_array.reverse();
     res.render(__dirname + '/loginpage.ejs', {zeltron : file_name_array});
});

app.post('/signininfocomplete', function(req, res) {
     let username1 = req.body.usernamel;
     let password1 = req.body.passwordl;
     let cap = req.body.cap;
     if (capcha == cap) {
          if (username1 && password1)
          {
               connection.query('SELECT * FROM users WHERE Username = ? AND Password = ?', [username1, password1], function (error, results, fields) {
                    if (results.length > 0)
                    {
                         req.session.loggedin = true;
                         req.session.username = username1;
                         if (file_name_array.length != 0) {
                              file_name_array.forEach(function (item) {
                                   fs.unlinkSync("./dumby/" + item + ".png");
                              });
                              file_name_array.length = 0;
                         }
                         if (results[0].Prime == 1) {
                              res.redirect('/homeadmin');
                         } else {
                              res.redirect('/home');
                         }
                    } else {
                         res.redirect('/hacker');
                    }
               });
          } else {
               res.redirect('/hacker');
          }
     } else {
          res.redirect('/hacker');
     }
});

app.get('/hackerty', function(req, res) {
     res.sendFile(path.join(__dirname + "/hacker.html"));
});

app.get('/home', function(req, res) {
     if (req.session.loggedin)
     {
          res.sendFile(path.join(__dirname + "/byheader.html"));
     }
     else
     {
          res.redirect('/');
     }
});

app.get('/homeadmin', function(req, res) {
     if (req.session.loggedin)
     {
          //res.sendFile(path.join(__dirname + "/byheaderadmin.html"));
          connection.query('SELECT * FROM users WHERE Username = ?', [req.session.username], function (error, results, fields) {
               if (results.length > 0)
               {
                    if (results[0].Prime == 1) {
                         res.sendFile(path.join(__dirname + "/byheaderadmin.html"));
                    } else {
                         res.redirect('/home');
                    }
               }
          });
     } else {
          res.redirect('/');
     }
});

app.get('/hacker', function(req, res) {
     res.sendFile(path.join(__dirname + "/loginfail.html"));
});

app.post('/loginfail', function(req, res) {
     res.redirect('/signininfo');
});

app.post('/passwordresetting', function(req, res) {
     res.redirect('/resetpage');
});

app.get('/resetpage', function(req, res) {
     res.sendFile(path.join(__dirname + "/passwordresetting.html"));
});

app.post('/ResetPassword', function(req, res) {
     let usernameuse = req.body.usernameh;
     if (usernameuse)
     {
          connection.query('SELECT * FROM users WHERE Username = ?', [usernameuse], function (error, results, fields) {
               if (results.length == 1)
               {
                    let emailpassword = results[0].Password;
                    let emailuse = results[0].Email;

                    var transporter = mailsender.createTransport({
                         service: 'gmail',
                         auth: {
                              user: 'gmail@gmail.com',
                              pass: 'emailpassword'
                         }
                    });

                    var mailOptions = {
                         from: 'gmail@gmail.com',
                         to: emailuse,
                         subject: 'Your Password',
                         text:'Your account password is "' + emailpassword + '". Please donot share it with anyone.',
                    };

                    transporter.sendMail(mailOptions, function(error, info){
                         if (error)
                         {
                              console.log(error);
                         }
                         else
                         {
                              console.log('Email sent: ' + info.response);
                         }
                    });
                    res.redirect('/passwordresettingdone');
               }
               else
               {
                    res.redirect('/hacker1');
               }
          });
     }
     else
     {
          res.redirect('/hacker1');
     }
});

app.post('/goback1', function(req, res) {
     res.redirect('/resetpage');
});

app.get('/passwordresettingdone', function(req, res) {
     res.sendFile(path.join(__dirname + '/passwordresetted.html'));
});

app.get('/hacker1', function(req, res) {
     res.sendFile(path.join(__dirname + '/usernamefail.html'));
});

app.post('/goback', function(req, res) {
     res.redirect('/signininfo');
});

app.get('/signupinfo', function(req, res) {
     res.sendFile(path.join(__dirname + '/signuppage.html'));
});

app.post('/signupinfocomplete', function(req, res) {
     let username2 = req.body.usernamee;
     let password2 = req.body.passworde;
     let passwordcomp = req.body.passwordconfirm;
     let email2 = req.body.emaile;
     if (username2 && password2)
     {
          if (password2 == passwordcomp)
          {
               if (password1.length > 8) {
                    if (/[^a-zA-Z0-9]/.test(password1)) {
                         let query = "INSERT INTO `users` (Username, Password, Email) VALUES ('" + username2 + "', '" + password2 + "', '" + email2 + "')";
                         connection.query(query, function (error, results, fields) {
                              res.redirect('/signininfo');
                         });
                    } else {
                         res.redirect('/hackerty');
                    }
               } else {
                    res.redirect('/hackerty');
               }
          }
          else
          {
               res.redirect('/hacking');
          }
     }
     else
     {
          res.redirect('/hacking');
     }
});

app.post('/logout', function(req, res) {
     res.redirect('/loggedout');
});

app.get('/loggedout', function(req, res) {
     req.session.loggedin = false;
     req.session.username = null;
     res.redirect('/');
});

app.get('/hacking', function(req, res) {
     res.sendFile(path.join(__dirname + '/signupfail.html'));
});

app.post('/submitls', function(req, res) {
     res.redirect('/signupinfo');
});

app.listen(8080);
console.log('Running on port: ' + '8080');
