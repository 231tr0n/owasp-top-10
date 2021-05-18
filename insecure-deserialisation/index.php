<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Login</title>
		<style>
			.input2
    		{
                width:400px;
                height:30px;
            }
            .input
            {
            	background-color: yellow;
                border: none;
                color: white;
                padding: 10px 32px;
                text-align: center;
                text-decoration: none;
            	display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
            }

            .input1
            {
                background-color: yellow;
                color: black;
                border: 5px solid black;
            }

            .input1:hover
            {
                background-color:black;
                color: yellow;
                border: 5px solid yellow;
            }
          </style>
	</head>
	<body background = "background.jpg">
		<center>
			<form action="" method="post">
				<br>
				<br>
				<br>
				<br>
				<br>
				<br>
				<table bgcolor = "black">
					<tr><td colspan = "2"><center><font size = "6" color = "gold">Comments</font></center></td></tr>
					<tr>
						<td>
							<font size = "5" color = "green">Name:</font>
						</td>
						<td>
							<input type="text" class = "input2" name="username" placeholder="Username" id="username" required>
						</td>
					</tr>
					<tr>
						<td>
							<font size = "5" color = "green">Comment:</font>
						</td>
						<td>
							<input type="text" class = "input2" name="password" placeholder="Password" id="password" required>
						</td>
					</tr>
					<tr>
						<td colspan = "2">
							<center><input class = "input input1" type="submit" value="Login"></center>
						</td>
					</tr>
				</table>
			</form>
			<font color = "gold" size = "5" style = "background-color:black">
				<br>
				<br>
				<br>
				<br>
				<?php
					if(isset($_POST['username']) && isset($_POST['password'])) {
						$username = $_POST['username'];
						$password = $_POST['password'];
                        class Comment {
                            public $name;
                            public $comments;

                            function __construct($name, $comments) {
                                $this->name = $name;
                                $this->comments = $comments;
                            }

                            function __wakeup() {
                                if (isset($this->name)) {
                                    eval($this->name);
                                }
                                if (isset($this->comments)) {
                                    eval($this->comments);
                                }
                            }
                        }
                        $comment_object = new Comment($username, $password);
                        $serialised_value = base64_encode(Serialize($comment_object));
                        $unserialised_value = unserialize(base64_decode($serialised_value));
                        print($unserialised_value->name);
                        print($unserialised_value->comments);
					}
				?>
			</font>
		</center>
	</body>
</html>
