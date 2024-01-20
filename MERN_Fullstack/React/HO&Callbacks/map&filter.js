const nums = [23,56,19,20,9,20,78,55,32,42,8,12,80]

const nbaAthletes = [
    {name:'Kevin Durant', league:'NBA', position: 'Small Forward', active:true},
    {name:'Charles Barkley', league:'NBA',position: 'Power Forward', active:false},
    {name:'Stephen Curry', league:'NBA',  position: 'Point Guard', active:true },
    {name:'Shaq', league:'NBA',  position: 'Center', active:false },
    {name:'Damian Lillard', league:'NBA',  position: 'Point Guard', active:true },
    {name:'Mike James', league:'Euro',  position: 'Shooting Guard', active:true },
]

// const newNums = nums.map((number) => number*2)
// console.log(newNums);
// console.log(nums);

// const evenNums = nums.filter((number) => number % 2 === 0)
// console.log(evenNums);
// console.log(nums);

const pointGuards = nbaAthletes.filter((athletes) => athletes.position === 'Point Guard')
console.log(pointGuards);