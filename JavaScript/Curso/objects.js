
var ourDog = {
    "name" : "camper",
    "legs": 4,
    "tails": 1,
    "friends":["everything!"],
    PI : 3.14
};

var namevalue = ourDog.name; //This is going to be "camper"
var numbervalue = ourDog["name"] //Yhis is also "camper"
var val = ["name"];
var nameval = ourDog[val]; //We can also use variables

ourDog.name = "no camper" //This is how we change the values
delete ourDog.legs; //It deletes the object


function chekObj(chekProp) {
if (ourDog.hasOwnProperty(chekProp)) {
    return myObj[chekProp]
} else {
    return "Not Found"
}
}


var voxel = { x : 1.2, y: 2.7, z: 4.4}//Destructuring objects
const { x : a, y: b, z: c} = voxel; //Get the field of x and copy to value a... We are creating 3 variables a = 1.2, b = 2.7 and z = 4.4


const CreatePerson = (name, person, gender) => ({name, person, gender}); //This creates a object with the pair values name:name, person:person, gender:gender


Object.freeze(ourDog); // This frezees the object and prevents mutation

try {   //We use try to prove something that might have an error
    ourDog.PI = 3
} catch (ex) {  //Code to handle the error
    console.log(ex);    //Code that runs no matter what
}
    return ourDog.PI











