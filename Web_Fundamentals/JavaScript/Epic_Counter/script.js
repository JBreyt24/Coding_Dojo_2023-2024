console.log("<| main system, engaging test mode |>")

var count = 1;
var countElement = document.querySelector("#count");

function add1() {
    count++;
    countElement.innerText = "The count is " + count;
    console.log(count);
}

function subtract1() {
    count--;
    countElement.innerText = "The count is " + count;
    console.log(count);
}