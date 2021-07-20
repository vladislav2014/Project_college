
<?php
require_once "function/connect.php";
connectDB();
$id = $_GET['id_product'];

if (isset($id))
$mysqli->query("DELETE FROM product where id_product = $id");

closeDB();
?>



<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>

<?php

if ($_COOKIE['login']=='admin')
echo "
<a href=\"index.php\">Вернуться обратно</a>
";
else {
    echo "
<span style=\"color: red; display: block\">ОШИБКА УДАЛЕНИЯ, ОТСУТСВУЮТ ПРАВА ДОСТУПА</span>
<a href=\"index.php\">Вернуться обратно</a>
";
}
?>
</body>
</html>

