//build a loop function to know when to give a piece of candy and when to stop

//questions

//1. how do we know we need to loop here?
//2. What's the starting point of the loop?
//3. When should the loop stop?
//4. How will the loop stop?
//5. What's incrementing for each iteration of the loop?
//6. What variables do we need?


//candy pops out of device every time a runner reaches 2 miles on treadmill but stops giving candy out at mile 6

var miles = 0 

for(var miles = 0; miles <6; miles++) {
    if(miles % 2 == 0) {
        if(miles != 0) {
            console.log("We are on mile: " + miles);
            console.log("Here is a candy");
        }
    }
}