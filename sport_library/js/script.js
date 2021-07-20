var counter = 0; //создание счетчика
var photo = new Array(); //создание массива для хранения названия фотографии
var about = new Array(); //создание массива для хранения описания
var size = new Array(); //создание массива для хранения количества
var price = new Array(); //создание массива для хранения цены
var summa = 0; //создание переменной итоговой суммы

size[1]=0;
size[2]=0;
size[3]=0;
size[4]=0;
size[5]=0;
size[6]=0;
size[7]=0;
size[8]=0;
size[9]=0;

price[1]=0;
price[2]=0;
price[3]=0;
price[4]=0;
price[5]=0;
price[6]=0;
price[7]=0;
price[8]=0;
price[9]=0;

// функция использования карты для отображения картинки (корзины)
function Usecart() { 
    document.getElementById("container-cart").style.display="flex"
    document.getElementById("container-cart").style.backgroundColor="#000"
    document.getElementById("main-container").style.display="none"
    document.bgColor="#000"
    document.getElementById("input-sum").value=summa;
    if(size[1]>0){
    document.getElementById("1").style.display="flex";
    document.getElementById("size1").value=size[1];
    document.getElementById("price1").value=price[1];}
    if(size[2]>0){
    document.getElementById("2").style.display="flex";
    document.getElementById("size2").value=size[2];
    document.getElementById("price2").value=price[2];}
    if(size[3]>0){
    document.getElementById("3").style.display="flex";
    document.getElementById("size3").value=size[3];
    document.getElementById("price3").value=price[3];}
    if(size[4]>0){
    document.getElementById("4").style.display="flex";
    document.getElementById("size4").value=size[4];
    document.getElementById("price4").value=price[4];}
    if(size[5]>0){
    document.getElementById("5").style.display="flex";
    document.getElementById("size5").value=size[5];
    document.getElementById("price5").value=price[5];}
    if(size[6]>0){
    document.getElementById("6").style.display="flex";
    document.getElementById("size6").value=size[6];
    document.getElementById("price6").value=price[6];}
    if(size[7]>0){
    document.getElementById("7").style.display="flex";
    document.getElementById("size7").value=size[7];
    document.getElementById("price7").value=price[7];}
    if(size[8]>0){
    document.getElementById("8").style.display="flex";
    document.getElementById("size8").value=size[8];
    document.getElementById("price8").value=price[8];}
    if(size[9]>0){
    document.getElementById("9").style.display="flex";
    document.getElementById("size9").value=size[9];
    document.getElementById("price9").value=price[9];}
}

// функция добавления товара в корзину
function Putcart(OptNut) {
    counter++;
    document.getElementById("cart").style.display="block";
    document.getElementById("counter").value=counter;
    if (counter > 9) {
        document.getElementById("counter").style.width="25px";
        document.getElementById("count").style.width="30px";
        document.getElementById("count").style.height="30px";
    }

    switch (OptNut) {
        case 1:
            photo[OptNut] = "whey.jpg";
            about[OptNut] = "Протеин Optimum Nutrition 100% 2270 г";
            size[OptNut] +=1;
            price[OptNut] +=3990;
            summa+=3990;
            break;
            
        case 2:
            photo[OptNut] = "whey-max.jpg";
            about[OptNut] = "Протеин Maxler Matriza 5.0 2270 г";
            size[OptNut] +=1;
            price[OptNut] +=2499;
            summa+=2499;
            break;

        case 3:
            photo[OptNut] = "whey-rline.jpg";
            about[OptNut] = "Протеин Rline Light Whey 1000 г";
            price[OptNut] += 990;
            size[OptNut] +=1;
            summa+=990;
            break;

        case 4:
            photo[OptNut] = "ser-mas.jpg";
            about[OptNut] = "Гейнер Optimum Nutrition Serious Mass 2700 г Chocolate";
            price[OptNut] += 2945;
            size[OptNut] +=1;
            summa+=2945;
            break;

        case 5:
            photo[OptNut] = "mega-gein.jpg";
            about[OptNut] = "Гейнер Maxler Mega Gainer 1000 г";
            size[OptNut]+=1;
            price[OptNut] += 800;
            summa+=800;
            break;

        case 6:
            photo[OptNut] = "mutant.jpg";
            about[OptNut] = "Гейнер Mutant Mass 6800 г";
            size[OptNut]+=1;
            price[OptNut] += 4500;
            summa+=4500;
            break;

        case 7:
            photo[OptNut] = "max-creat.png";
            about[OptNut] = "Maxler Creatine 500 г без вкуса";
            size[OptNut]+=1;
            price[OptNut] += 749;
            summa+=749;
            break;

        case 8:
            photo[OptNut] = "perf-creat.jpg";
            about[OptNut] = "SAN Performance Creatine 300 г без вкуса";
            size[OptNut]+=1;
            price[OptNut] += 489;
            summa+=489;
            break;

        case 9:
            photo[OptNut] = "rline-creat.jpg";
            about[OptNut] = "Rline Creatine Caps 200 капсул без вкуса";
            size[OptNut]+=1;
            price[OptNut] += 500;
            summa+=500;
            break;
    }
    console.log(photo[OptNut],about[OptNut],size[OptNut],price[OptNut]);

}

// функция, реализующая "+" в корзине для увеличения количества одного товара
function PlusCart(Size){

    if (counter > 9) {
        document.getElementById("counter").style.width="25px";
        document.getElementById("count").style.width="30px";
        document.getElementById("count").style.height="30px";
    }

    switch(Size){
        case 1: 
            size[1]++;
            price[1]+=3990;
            summa+=3990;
            counter++;
            document.getElementById("size1").value=size[1];
            document.getElementById("price1").value=price[1];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;

            break;

        case 2: 
            size[2]++;
            price[2]+=2499;
            summa+=2499;
            counter++;
            document.getElementById("size2").value=size[2];
            document.getElementById("price2").value=price[2];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            break;

        case 3: 
            size[3]++;
            price[3]+=990;
            summa+=990;
            counter++;
            document.getElementById("size3").value=size[3];
            document.getElementById("price3").value=price[3];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            break;

        case 4: 
            size[4]++;
            price[4]+=2945;
            summa+=2945;
            counter++;
            document.getElementById("size4").value=size[4];
            document.getElementById("price4").value=price[4];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            break;

        case 5: 
            size[5]++;
            price[5]+=800;
            summa+=800;
            counter++;
            document.getElementById("size5").value=size[5];
            document.getElementById("price5").value=price[5];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            break;

        case 6: 
            size[6]++;
            price[6]+=4500;
            summa+=4500;
            counter++;
            document.getElementById("size6").value=size[6];
            document.getElementById("price6").value=price[6];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            break;

        case 7: 
            size[7]++;
            price[7]+=749;
            summa+=749;
            counter++;
            document.getElementById("size7").value=size[7];
            document.getElementById("price7").value=price[7];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            break;

        case 8: 
            size[8]++;
            price[8]+=489;
            summa+=489;
            counter++;
            document.getElementById("size8").value=size[8];
            document.getElementById("price8").value=price[8];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            break;

        case 9: 
            size[9]++;
            price[9]+=500;
            summa+=500;
            counter++;
            document.getElementById("size9").value=size[9];
            document.getElementById("price9").value=price[9];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            break;
    }
}

// функция, реализующая "-" в корзине для уменьшения количества одного товара
function MinusCart(Size){

    switch(Size){
        case 1: 
            size[1]--;
            price[1]-=3990;
            summa-=3990;
            counter--;
            document.getElementById("size1").value=size[1];
            document.getElementById("price1").value=price[1];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            if (size[1]<1){
                document.getElementById("1").style.display="none";
            }
            if(document.getElementById("counter").value==0){
                document.getElementById("cart").style.display="none";
            }
            break;
            
        case 2: 
            size[2]--;
            price[2]-=2499;
            summa-=2499;
            counter--;
            document.getElementById("size2").value=size[2];
            document.getElementById("price2").value=price[2];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            if (size[2]<1){
                document.getElementById("2").style.display="none";
            }
            if(document.getElementById("counter").value==0){
                document.getElementById("cart").style.display="none";
            }
            break;

        case 3: 
            size[3]--;
            price[3]-=990;
            summa-=990;
            counter--;
            document.getElementById("size3").value=size[3];
            document.getElementById("price3").value=price[3];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            if (size[3]<1){
                document.getElementById("3").style.display="none";
            }
            if(document.getElementById("counter").value==0){
                document.getElementById("cart").style.display="none";
            }
            break;

        case 4: 
            size[4]--;
            price[4]-=2945;
            summa-=2945;
            counter--;
            document.getElementById("size4").value=size[4];
            document.getElementById("price4").value=price[4];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            if (size[4]<1){
                document.getElementById("4").style.display="none";
            }
            if(document.getElementById("counter").value==0){
                document.getElementById("cart").style.display="none";
            }
            break;

        case 5: 
            size[5]--;
            price[5]-=800;
            summa-=800;
            counter--;
            document.getElementById("size5").value=size[5];
            document.getElementById("price5").value=price[5];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            if (size[5]<1){
                document.getElementById("5").style.display="none";
            }
            if(document.getElementById("counter").value==0){
                document.getElementById("cart").style.display="none";
            }
            break;

        case 6: 
            size[6]--;
            price[6]-=4500;
            summa-=4500;
            counter--;
            document.getElementById("size6").value=size[6];
            document.getElementById("price6").value=price[6];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            if (size[6]<1){
                document.getElementById("6").style.display="none";
            }
            if(document.getElementById("counter").value==0){
                document.getElementById("cart").style.display="none";
            }
            break;

        case 7: 
            size[7]--;
            price[7]-=749;
            summa-=749;
            counter--;
            document.getElementById("size7").value=size[7];
            document.getElementById("price7").value=price[7];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            if (size[7]<1){
                document.getElementById("7").style.display="none";
            }
            if(document.getElementById("counter").value==0){
                document.getElementById("cart").style.display="none";
            }
            break;

        case 8: 
            size[8]--;
            price[8]-=489;
            summa-=489;
            counter--;
            document.getElementById("size8").value=size[8];
            document.getElementById("price8").value=price[8];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            if (size[8]<1){
                document.getElementById("8").style.display="none";
            }
            if(document.getElementById("counter").value==0){
                document.getElementById("cart").style.display="none";
            }
            break;

        case 9: 
            size[9]--;
            price[9]-=500;
            summa-=500;
            counter--;
            document.getElementById("size9").value=size[9];
            document.getElementById("price9").value=price[9];
            document.getElementById("input-sum").value=summa;
            document.getElementById("counter").value=counter;
            if (size[9]<1){
                document.getElementById("9").style.display="none";
            }
            if(document.getElementById("counter").value==0){
                document.getElementById("cart").style.display="none";
            }
            break;
    }
}

// функция отправки заказа
function Send(){
    for (var i = 1; i<=9; i++){
        size[i]=0;
        price[i]=0;
    }

    var text_input = document.getElementById("text-input").value;
    var email_input = document.getElementById("email-input").value;
    var tel_input = document.getElementById("tel-input").value;

    console.log(text_input);
    console.log(email_input);
    console.log(tel_input);

    if ((text_input!=0) && (email_input!="") && (tel_input!="")){
        var zakaz = "Заказ на сумму: ";
        var confirm = "р. успешно оформлен"
        console.log ("summa - ", summa)
        document.getElementById("container-cart").style.display="none";
        document.getElementById("cart").style.display="none";
        document.getElementById("main-container").style.display="block";
        document.getElementById("1").style.display="none";
        document.getElementById("2").style.display="none";
        document.getElementById("3").style.display="none";
        document.getElementById("4").style.display="none";
        document.getElementById("5").style.display="none";
        document.getElementById("6").style.display="none";
        document.getElementById("7").style.display="none";
        document.getElementById("8").style.display="none";
        document.getElementById("9").style.display="none";
        document.bgColor="#fff"
        alert(zakaz+summa+confirm);
        counter=0;
        summa=0;
        document.location.href = "mag.php";
    }

    else {
        alert ("Заполните все поля!");
    }
}