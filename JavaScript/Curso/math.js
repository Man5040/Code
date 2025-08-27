
// % give us the remainder 
var x = 10;
var remainder = x % 3;
console.log(remainder);

x += 12     //We can use += instead of = x+12

var min;
var max;
function random(min, max){
    parseInt(min, 10);                  //It converts a string into a number, and the second number is the base of the number
    Math.random();                   //It gives random values between 0 and 1 but it cant be 1
    Math.floor(Math.random()*20);   //It returns the nearest integer below the number
    return Math.floor(Math.random()*(max +1 - min )+ min); //This is how we get a random number between a range     

}


