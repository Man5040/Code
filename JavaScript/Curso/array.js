
var myArray = []; //It is a variable that can store multiple values 

ourArray = [18,60,[10, 11, 15]]; //We can have arrays inside arrays, is called nested array
myData = ourArray[2][1]; //We can acces a value by its number, the second 

ourArray.push([11, "dog"]);
ourArray.pop(); //Erases the last element and returns it
ourArray.shift(); //Erases the first element and returns it
ourArray.unshift("cat"); //Inserts elements at the start of the array

ourArray[1] = 50; //Reassigns the array

const numbers = [1, 2, 3, 4, 5];
const sum = numbers.reduce((acc, num) => acc + num, 0); //We put the acumulator at left , and the current value at right 
console.log(sum); 

const month1 = [JAN, FEV, MAR];
const month2 = [...month1, APR, MAY];   //The spread operator divides the array so we can use the elements individually, it also works with objects
console.log(month2); // [JAN, FEV, MAR, APR, MAY]

//Deconstructing objects
const [x, y, , , z] = [1, 2, 3, 4, 5, 6]; //We can deconstruct arrays but it will ned to be in order
console.log(x, y, z);

let a= 8, b= 6;
() => {[a, b] = [b, a]} //It switches a and b
