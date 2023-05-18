console.log("<| main system, engaging test mode |>")

var likes = 3;
var countElement = document.querySelector("#amt-liked");

function addLike() {
    likes++;
    countElement.innerText =  likes + " like(s)";
    console.log(likes);
}

