const mysql = require('mysql');
const session = require('express-session');
const express = require('express');
const bp = require('body-parser');
const mailsender = require('nodemailer');
const path = require('path');
const fs = require('fs');

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
     res.sendFile(path.join(__dirname + '/loginpage.html'));
});

app.post('/signininfocomplete', function(req, res) {
     let username1 = req.body.usernamel;
     let password1 = req.body.passwordl;
     if (username1 && password1)
     {
          connection.query('SELECT * FROM users WHERE Username = ? AND Password = ?', [username1, password1], function (error, results, fields) {
               if (results.length > 0)
               {
                    req.session.loggedin = true;
                    req.session.username = username1;
                    if (results[0].Prime == 1) {
                         res.redirect('/homeadmin');
                    } else {
                         res.redirect('/home');
                    }
               }
               else
               {
                    res.redirect('/hacker');
               }
          });

     }
     else
     {
          res.redirect('/hacker');
     }
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
          res.sendFile(path.join(__dirname + "/byheaderadmin.html"));
          /*connection.query('SELECT * FROM users WHERE Username = ?', [req.session.username], function (error, results, fields) {
               if (results.length > 0)
               {
                    if (results[0].Prime == 1) {
                         res.sendFile(path.join(__dirname + "/byheaderadmin.html"));
                    } else {
                         res.redirect('/home');
                    }
               }
          });*/
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
               let query = "INSERT INTO `users` (Username, Password, Email) VALUES ('" + username2 + "', '" + password2 + "', '" + email2 + "')";
               connection.query(query, function (error, results, fields) {
                    res.redirect('/signininfo');
               });
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
