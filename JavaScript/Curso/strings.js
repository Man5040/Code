
var myStr1= " \" Hola mundo \" "; // If we need to put "" we can use

var myStr2 = "Hello world";

var myStr = myStr1 + myStr2; // We can add the strings the they will appear together

number = myStr.length; //We can obtain the number of characters of a string
number1 = myStr1[0]; // We can obtain a letter by its position

function wordBlanks(myNoun, myAdjetive, myVerb){

var result = "";
result += "The " + myAdjetive + " " + myNoun + " " + myVerb;
return result
}

wordBlanks("dog", "big", "ran");

const person = {
    name: "Walter",
    age: 51
}

//Template literal, is like a string where we can put variables inside of it
const greeting =  `Hello my name is ${person.name} ! I am ${person.age} years old  `