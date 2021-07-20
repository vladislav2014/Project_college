<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>

<style>
    input {
        display: block;
        margin: 10px 0;
    }

    textarea {
        display: block;
        margin: 10px 0;
        resize: none;
    }

</style>
<?php

require_once "function/connect.php";
connectDB();

if (isset($_POST['id_product'])) {
    $name = $_POST['name_prod'];
    $about = $_POST['about'];
    $buy = $_POST['price_buy'];
    $sale = $_POST['price_sale'];
    $id_prod = $_POST['id_product'];
    $result = $mysqli->query("UPDATE product
                                SET name_prod = '$name' , about = '$about', price_buy = $buy, price_sale = $sale
                                where id_product = $id_prod");

}


if (isset($_GET['id_product'])) {
    $id = $_GET['id_product'];
    $result =
        $mysqli->query("select * from product where id_product=$id");
    $rows = resultToArray($result);
    $row = $rows[0];
}

echo
    " <div class=\"form_input\">
            <form action=\"update.php?id_product=$id\" enctype='multipart/form-data' method=post>
                <input class=\"text_input\" type=\"number\" name=\"id_product\"  value = " . $row['id_product'] . ">
                <textarea class=\"text_input\" type=\"text\" name=\"name_prod\"  required cols = 100 rows = 5>" . $row['name_prod'] . " </textarea>
                <textarea class=\"text_input\" type=\"text\" name=\"about\"  required cols = 100 rows = 15 >" . $row['about'] . " </textarea>
                <input class=\"text_input\" type=\"number\" name=\"price_buy\"  required value = " . $row['price_buy'] . ">
                <input class=\"text_input\" type=\"number\" name=\"price_sale\" required value = " . $row['price_sale'] . ">
                <input class=\"text_input\" type=\"submit\" value=\"Править\">
                <a href=\"index.php\">ДОМОЙ БЛЯТЬ</a>
            </form>
        </div>";


?>

</body>
</html>
