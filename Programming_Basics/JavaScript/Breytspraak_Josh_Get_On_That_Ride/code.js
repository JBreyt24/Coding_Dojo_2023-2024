//As a user, I need to know how many pieces of cake I will have left if I divide out my cake (which has 12 pieces) for 5 people to eat.
//As the designated cake slicer and distributor at our office birthday parties, 
//I want a function called howMuchLeftOverCake that passes two variables numberOfPieces and numberOfPeople into it and figures out the remaining pieces of cake.
//


var numberOfPieces = 12
var numberOfPeople = 5
var leftOverPieces = numberOfPieces % numberOfPeople

function howMuchLeftOverCake() {
    for (var numberOfPieces = 12; numberOfPieces >= 0; numberOfPieces--) {
        if (leftOverPieces >= 5) {
            return leftOverPieces
        }
        console.log("Hold another party!")

        if(leftOverPieces = 3 && 5 ) {
            return leftOverPieces
        }
            console.log("You have leftovers to share!")

        if (leftOverPieces = 1 && 2) {
            return leftOverPieces
        }
            console.log("You have some leftovers!")

        if (leftOverPieces = 0) {
            return leftOverPieces
        }
        console.log("No leftovers for you!")
}
}
howMuchLeftOverCake(12,5)