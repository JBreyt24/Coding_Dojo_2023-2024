var animalImg= document.querySelector("#fav-animal");


function pickCat(element) {
    // console.log(element.style);
    // element.style.backgroundColor = "goldenrod";
    element.remove();
    animalImg.src = "imgs/cat.png";
}

function pickDog(element) {
    console.log(element.classList);
    element.classList.add("btn");
    animalImg.src = "imgs/dog.jpg";
}