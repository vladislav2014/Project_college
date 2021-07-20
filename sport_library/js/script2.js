// функция открытия окна описания товаров
function About(Number) {
    switch(Number) {
        case 1:
            document.getElementById("protein-1").style.display="block";
            document.getElementById("main-container").style.display="none";
            document.location.href = "mag.php#top";
            break;

        case 2:
            document.getElementById("protein-2").style.display="block";
            document.getElementById("main-container").style.display="none";
            document.location.href = "mag.php#top2";
            break;

        case 3:
            document.getElementById("protein-3").style.display="block";
            document.getElementById("main-container").style.display="none";
            document.location.href = "mag.php#top3";
            break;

        case 4:
            document.getElementById("geiner-1").style.display="block";
            document.getElementById("main-container").style.display="none";
            document.location.href = "mag.php#top4";
            break;

        case 5:
            document.getElementById("geiner-2").style.display="block";
            document.getElementById("main-container").style.display="none";
            document.location.href = "mag.php#top5";
            break;

        case 6:
            document.getElementById("geiner-3").style.display="block";
            document.getElementById("main-container").style.display="none";
            document.location.href = "mag.php#top6";
            break;

        case 7:
            document.getElementById("creatin-1").style.display="block";
            document.getElementById("main-container").style.display="none";
            document.location.href = "mag.php#top7";
            break;

        case 8:
            document.getElementById("creatin-2").style.display="block";
            document.getElementById("main-container").style.display="none";
            document.location.href = "mag.php#top8";
            break;

        case 9:
            document.getElementById("creatin-3").style.display="block";
            document.getElementById("main-container").style.display="none";
            document.location.href = "mag.php#top9";
            break;
    }
}

// функиця закрытия окна описания товаров
function CloseAbout(Close){
    switch(Close){
        case 1:
            document.getElementById("protein-1").style.display="none";
            document.getElementById("main-container").style.display="block";
            document.location.href = "mag.php#one";
            break;

        case 2:
            document.getElementById("protein-2").style.display="none";
            document.getElementById("main-container").style.display="block";
            document.location.href = "mag.php#one";
            break;

        case 3:
            document.getElementById("protein-3").style.display="none";
            document.getElementById("main-container").style.display="block";
            document.location.href = "mag.php#one";
            break;

        case 4:
            document.getElementById("geiner-1").style.display="none";
            document.getElementById("main-container").style.display="block";
            document.location.href = "mag.php#two";
            break;

        case 5:
            document.getElementById("geiner-2").style.display="none";
            document.getElementById("main-container").style.display="block";
            document.location.href = "mag.php#two";
            break;

        case 6:
            document.getElementById("geiner-3").style.display="none";
            document.getElementById("main-container").style.display="block";
            document.location.href = "mag.php#two";
            break;

        case 7:
            document.getElementById("creatin-1").style.display="none";
            document.getElementById("main-container").style.display="block";
            document.location.href = "mag.php#last";
            break;

        case 8:
            document.getElementById("creatin-2").style.display="none";
            document.getElementById("main-container").style.display="block";
            document.location.href = "mag.php#last";
            break;

        case 9:
            document.getElementById("creatin-3").style.display="none";
            document.getElementById("main-container").style.display="block";
            document.location.href = "mag.php#last";
            break;
    }
}
function CloseCart(){ // функция закрытия корзины
    document.getElementById("container-cart").style.display="none"
    document.getElementById("main-container").style.display="block"
    document.bgColor="#fff"
    document.location.href = "mag.php#one";
}