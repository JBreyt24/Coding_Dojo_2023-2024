//If the rider's height is greater than 42, the console.log should say "Get on that ride, kiddo!". 
//Otherwise, console.log should say "Sorry kiddo. Maybe next year."


// let age = 10;
// let height = 42;
// if (age >= 10 && height >= 42) {
//     console.log("Get on that ride, kiddo!");
// }
// else if(age <= 10 || height < 42){
//     console.log("Sorry kiddo. Maybe next year!")
// }



//this next like of code will be to determine if you should buy a certain guitar; EXCEPTIONS = the guitar HAS TO HAVE a 26.5 scale length neck. If it is less than that then we don't want it
//ALSO: it has to be made out of ash wood


// let scaleLength = 26.5;
// let woodType = "mahogany";

// if (scaleLength >= 26.5 && woodType === "ash") {
//     console.log("Buy it!");
// }
// else if (scaleLength <=25.5 || woodType != "ash") {
//     console.log("Don't buy it!");
// }


// YOUR COMMENT HERE - what would this variable do?
var likeCount = 0;
// YOUR COMMENT HERE - what would be the function of this code block?
function increaseLikes() {
    // YOUR COMMENT HERE - what is this sort operation for?
    likeCount = likeCount + 1;
}
console.log(likeCount)