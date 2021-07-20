<?php

$mysqli = false;
function connectDB()
{
    global $mysqli;
    if (!is_null($_COOKIE['login'])) {
        $mysqli = new mysqli("127.0.0.1", $_COOKIE['login'], $_COOKIE['password'], "shop");
        $mysqli->query("SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'");
    }
}


function closeDB()
{
    global $mysqli;
    $mysqli->close();

}



function getPost($limit)
{
    global $mysqli;
    connectDB();
    $result = $mysqli->query("SELECT * FROM `product` ORDER BY `id_product` LIMIT $limit");
    closeDB();
    return resultToArray($result);

}

function resultToArray($result){
$array = array();
while(($row = $result->fetch_assoc()) != false)
$array[] = $row;
return $array;
}

?>