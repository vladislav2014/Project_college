<!doctype html>
<html lang="ru">
<head>
    <?php
    require_once "function/connect.php";
    connectDB();
    if (isset($_POST['name_prod'])) {

        $name = $_POST['name_prod'];
        $about = $_POST['about'];
        $price_buy = $_POST['price_buy'];
        $price_sale = $_POST['price_sale'];

        $result = $mysqli->query("INSERT INTO `product` (`name_prod`, `about`, `price_buy`, `price_sale`)
 VALUES ('$name', '$about', '$price_buy', '$price_sale');
 ");

    }
closeDB();

    ?>
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
</style>

<div class="form_input">
    <form action="add.php" enctype='multipart/form-data' method=post>
        <input class="text_input" type="text" name="name_prod" placeholder="name_prod" required>
        <input class="text_input" type="text" name="about" placeholder="about" required>
        <input class="text_input" type="number" name="price_buy" placeholder="price_buy" required>
        <input class="text_input" type="number" name="price_sale" placeholder="price_sale" required>
        <input class="text_input" type="submit" value="Отправить">
    </form>
    <a href="index.php">Вернуться обратно</a>

</div>



</body>
</html>