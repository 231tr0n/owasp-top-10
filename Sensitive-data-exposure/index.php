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
					$count = 0;
					$locker = 1;
					$locker1 = 0;
					if(isset($_POST['username']) && isset($_POST['password'])) {
						$con = mysqli_connect('localhost', 'root', '', 'test');
						if (mysqli_connect_errno()) {
							exit('Failed to connect to MySQL: ' . mysqli_connect_error());
						}
						$username = $_POST['username'];
						$password = $_POST['password'];
						if ($stmt = $con->prepare('SELECT password, Lock_Username, Login_Count FROM accounts WHERE username = ?')) {
							$stmt->bind_param('s', $username);
							$stmt->execute();
							$stmt->store_result();
							if ($stmt->num_rows > 0) { /*Username:zeltron, Password:zeltronsrikar*/
								$stmt->bind_result($password1, $Username_Lock, $Login);
								$stmt->fetch();
								if ($Username_Lock === 0) {
									if ($Login === 5) {
										$datem = date("Y-m-d H:i:s");
										$datem = date('Y-m-d H:i:s',strtotime('+1 minutes',strtotime($datem)));
										$sql1 = "UPDATE accounts SET Lock_Username = '$locker', DTRow = '$datem' WHERE username = '$username'";
										mysqli_query($con, $sql1) or die(mysqli_error($con));
										printf("Your Account is Blocked for some Minutes");
									} else {
										if ($Username_Lock === 0) {
											$zeltron = hash('md5', $password);
											if ($zeltron === $password1) {
												printf("Username: %s",$_POST['username']);
												echo "<br>";
												printf("Password: %s",$_POST['password']);
												$count = 0;
												$sql = "UPDATE accounts SET Login_Count = '$count', Lock_Username = '$count' WHERE username = '$username'";
												mysqli_query($con, $sql) or die(mysqli_error($con));
											} else {
												printf("Wrong Username or Password");
												$sql = "SELECT Login_Count FROM accounts WHERE username = '$username'";
												$result = mysqli_query($con, $sql) or die(mysqli_error($con));
												$row = mysqli_fetch_array($result);
												$count = $row['Login_Count'];
												$count = $count + 1;
												$sql = "UPDATE accounts SET Login_Count = '$count' WHERE username = '$username'";
												mysqli_query($con, $sql) or die(mysqli_error($con));
											}
										} else {
											printf("Your Account is Blocked for some Minutes");
										}
									}
								} else {
									$sql = "SELECT DTRow FROM accounts WHERE username = '$username'";
									$result = mysqli_query($con, $sql) or die(mysqli_error($con));
									$row = mysqli_fetch_array($result);
									$datedi1 = $row['DTRow'];
									$datedi2 = date("Y-m-d H:i:s");
									if ($datedi2 >= $datedi1) {
										$datef = date("Y-m-d H:i:s");
										$sql = "UPDATE accounts SET Login_Count = '$locker1', Lock_Username = '$locker1', DTRow = '$datef' WHERE username = '$username'";
										mysqli_query($con, $sql) or die(mysqli_error($con));
										printf("Your Account is Unlocked, Try logging in again");
									} else {
										printf("Your Account is Blocked for some time");
									}
								}
							} else {
								printf("Wrong Username or Password");
							}
							$stmt->close();
						}
						$con->close();
					}
				?>
			</font>
		</center>
	</body>
</html>
