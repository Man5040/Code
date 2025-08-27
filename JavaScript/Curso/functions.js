
var x = 3;
function ourReusablefunction(){
    console.log("hello world");
}                                   //If we do not return anything the function will return undefined

console.log(ourReusablefunction)

function ourReusablefunction2(a, b){
    var c= a-b;                      //We can use the parameters of the function
    d = 12;                          //In some compilers if we do not use var, it will turn to a global scope variable
    console.log(c);
    return c;                       
}


console.log(x); //The variables deckared outside the function have global scope
console.log(c); /*The variables declared inside a function cannot be used outside it(local scope),
                 we can have two variables with local scope and global scope with the same name and the local variable will have preference*/



function increment(_number, _value = 1) {
    return _number + _value;
}

/* Arrow Functions */
var magic = () => new Date();
var myConcat = (arr1, arr2) => arr1.concat(arr2);

const RealNumberArray = [4, 5.6, -9.8, 3.14, 42];

const squarelist = (arr) => {
    const squaredIntegers = arr.filter(num => Number.isInteger(num) && num > 0).map(x => x*x); //Filters the paramters inside the function
    return squaredIntegers;
}

const squaredIntegers = squarelist(RealNumberArray);


const bycicle = {
    gear : 2,
    setGear(newGear){   //This is a function insede an object
    "Use strict";
    this.gear = newGear;
}
}

class Book{
    constructor(author){
    this._author = author;
    }

    getWriter(){        //Getter
    return this._author;
    }

    setWriter(updatedAuthor){   //Setter
        this._author = updatedAuthor;
    }
}

var SpaceShuttle = function(targetPlanet) {     //Constructor function creation
    this.targetPlanet = targetPlanet;
}

class SpaceShuttle{                             //Class creation
    constructor(targetPlanet){
    this.targetPlanet = targetPlanet;
}
}

var zeus = new SpaceShuttle('Jupiter');
console.log(zeus.targetPlanet)

