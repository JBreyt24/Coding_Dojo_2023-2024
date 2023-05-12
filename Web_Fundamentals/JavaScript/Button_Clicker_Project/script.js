console.log("it's working");

// if statement
// if = if true, execute this
// else = if false, execute this instead

function signIn(element) {
    if(element.innerText == "Login") {
        element.innerText = "Logout";
    } else {
        element.innerText = "Login";
    }
}

function hide(addDef) {
    addDef.remove();
}

function notification() {
    alert("Ninja was liked!");
}

