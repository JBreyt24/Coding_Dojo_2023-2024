console.log("<| main system, engaging test mode |>")

var likes1 = 9;
var countElement1 = document.querySelector("#amt-liked1");

function addLike1() {
    likes1++;
    countElement1.innerText =  likes1 + " like(s)";
    console.log(likes1);
}

var likes2 = 12;
var countElement2 = document.querySelector("#amt-liked2");

function addLike2() {
    likes2++;
    countElement2.innerText =  likes2 + " like(s)";
    console.log(likes2);
}

var likes3 = 9;
var countElement3 = document.querySelector("#amt-liked3");

function addLike3() {
    likes3++;
    countElement3.innerText =  likes3 + " like(s)";
    console.log(likes3);
}
