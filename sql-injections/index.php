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
					<tr><td colspan = "2"><center><font size = "6" color = "gold">Login Form</font></center></td></tr>
					<tr>
						<td>
							<font size = "5" color = "green">Username:</font>
						</td>
						<td>
							<input type="text" class = "input2" name="username" placeholder="Username" id="username" required>
						</td>
					</tr>
					<tr>
						<td>
							<font size = "5" color = "green">Password:</font>
						</td>
						<td>
							<input type="password" class = "input2" name="password" placeholder="Password" id="password" required>
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
						$con = mysqli_connect('localhost', 'root', '', 'test');
						if (mysqli_connect_errno()) {
							exit('Failed to connect to MySQL: ' . mysqli_connect_error());
						}
						$username = $_POST['username'];
						$password = $_POST['password'];
						$sql="SELECT username, password FROM accounts WHERE username='$username' and password='$password'";
						$result=mysqli_query($con, $sql) or die(mysqli_error($con)) /*die(printf("Error"))*/;
						$row = mysqli_fetch_array($result);
						if(mysqli_num_rows($result) > 0) {
							printf("Username: %s",$row['username']);
							echo "<br>";
							printf("Password: %s",$row['password']);
						} else {
							printf("Wrong Username or Password");
						}
						$con->close();
						/*if ($stmt = $con->prepare('SELECT password FROM accounts WHERE username = ?')) {
							$stmt->bind_param('s', $username);
							$stmt->execute();
							$stmt->store_result();
							if ($stmt->num_rows > 0) {
								$stmt->bind_result($password1);
								$stmt->fetch();
								if ($password === $password1) {
									printf("Username: %s",$_POST['username']);
									echo "<br>";
									printf("Password: %s",$_POST['password']);
								} else {
									printf("Wrong Username or Password");
								}
							} else {
								printf("Wrong Username or Password");
							}
							$stmt->close();
						}*/
					}
				?>
			</font>
		</center>
	</body>
</html>
