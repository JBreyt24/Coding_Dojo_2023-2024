

const squareTen = () => {
    return 10*10
}

const squareNine = () => {
    return 9*9
}

const squareFive = () => {
    return 5*5
}


















const squareNums = (num) => {
    return num*num
}








const multiplyArrayBy2 = (arr) => {
    let output = []
    for (let index = 0; index < arr.length; index++) {
        output.push(arr[index] * 2)
    }
    return output 
}
let result = multiplyArrayBy2([2,4,6])
console.log(result);


const multiplyArrayBy3 = (arr) => {
    let output = []
    for (let index = 0; index < arr.length; index++) {
        output.push(arr[index] * 3)
    }
    return output 
}
let result2 = multiplyArrayBy3([2,4,6])
console.log(result2);


const divideArrayBy2 = (arr) => {
    let output = []
    for (let index = 0; index < arr.length; index++) {
        output.push(arr[index] / 2)
    }
    return output 
}
let result3 = divideArrayBy2([2,4,6])
console.log(result3);










const manipulateArray = (arr, instructions) => {
    console.log('ARRAY', arr);
    console.log('FUNCTION', instructions);
    let output = []
    for (let index = 0; index < arr.length; index++) {
        output.push(instructions(arr[index]))
    }
    return output 
}


const multiplyElementBy2 = (val) => {
    return val*2
}

const result4 = manipulateArray([2,4,6], multiplyElementBy2)
console.log(result4);


const divideElementBy2 = (val) => {
    return val/2
}

const result5 = manipulateArray([2,4,6], divideElementBy2)
console.log(result5);