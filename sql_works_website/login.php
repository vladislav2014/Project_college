<?php
if($_GET["access"]=="exit"){
    setcookie("password", "", "0", "/");
    setcookie("login","","0","/");
    header("Location: ./login.php");
}
?>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>

<style>
    label  {
        margin: 20px 0;
    }
</style>



<form action="/" method="post">

    <label style="display: block"> Введите логин: <input type="text" name="login" required> </label>
    <label style="display: block"> Введите пароль: <input type="password" name="password" required> </label>
    <input type="submit" value="войти" style="display: block">

</form>
</body>
</html>