console.log("loading page...")

var inCart = 0;
var countElement = document.querySelector("#cart-amt");

function addItem() {
    inCart++;
    countElement.innerText =  inCart;
    console.log(inCart);
}

function message() {
    alert("This game is supported on Linux");
}

var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
showDivs(slideIndex += n);
}

function showDivs(n) {
var i;
var x = document.getElementsByClassName("mySlides");
if (n > x.length) {slideIndex = 1}
if (n < 1) {slideIndex = x.length} ;
for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
}
x[slideIndex-1].style.display = "block";
}





// References:
// W3 schools -> slideshow function