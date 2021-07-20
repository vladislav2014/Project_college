<?php
if (isset($_POST['login']) && isset($_POST['password'])){
setcookie('login', $_POST['login'], time()+360000, "/");
setcookie('password', $_POST['password'], time()+360000, "/");}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <?php
    require_once "function/connect.php";
    $product = getPost(20);
    ?>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>Document</title>
</head>
<body>


<div class="main-container">
    <h1>product</h1>
    <hr>
        <?php

        if (isset($_COOKIE['login']) && $_COOKIE['login']=='admin') {
            echo "
<a href=\"login.php?access=exit\"><button>Выйти</button></a>
<table border='1'>
        <thead>
        <tr>
            <th colspan=\"7\" style=\"text-align: center; background-color: #8ac; font-size: 24px; padding: 10px\"><a
                        href=add.php> добавить позицию </a></th>
        </tr>
        <tr>
            <th>id_product</th>
            <th>name_prod</th>
            <th>about</th>
            <th>price_buy</th>
            <th>price_sale</th>
            <th colspan=\"2\"> Действия</th>
        </tr>
        </thead>";
            for ($i = 0; $i < count($product); $i++) {
                $id = $product[$i]["id_product"];
                echo "<tr> <td>" . $product[$i]["id_product"] . "</td> <td>" . $product[$i]["name_prod"] . "</td> <td style='width: 30em; text-align: justify;'>" . $product[$i]["about"] . " </td> <td>" . $product[$i]["price_buy"] . " </td> <td>" . $product[$i]["price_sale"] . " </td> 
	
	 <td ><a href = delete.php?id_product=$id> Удалить позицию </a></td> <td> <a href = update.php?id_product=$id> Обновить позицию </a> </td>
 
 </tr>  ";
            }
        }
		
	   if (isset($_COOKIE['login']) && $_COOKIE['login']=='user') {
            echo "
<a href=\"login.php?access=exit\"><button>Выйти</button></a>
<table border='1'>
        <thead>
        <tr>
            <th colspan=\"7\" style=\"text-align: center; background-color: #8ac; font-size: 24px; padding: 10px\">Ассортимент </th>
        </tr>
        <tr>
            <th>name_prod</th>
            <th>about</th>
            <th>price_sale</th>
        </tr>
        </thead>";
            for ($i = 0; $i < count($product); $i++) {
                $id = $product[$i]["id_product"];
                echo "
 <tr> <td>" . $product[$i]["name_prod"] . "</td> <td style='width: 30em; text-align: justify;'>" . $product[$i]["about"] . " </td>  <td>" . $product[$i]["price_sale"] . " </td> <td ><a href = delete.php?id_product=$id> Удалить позицию </a></td>
	
 
 </tr> ";
            }
        }
        ?>

</div>

</body>
</html>