
boolean= true // True and false

3 == "3" //The double equality sign will not change the datatype (true)
3 === "3" //The triple equality sign will change the datatype (false)

var val =2;
if (val <= 3 && val >= 0){ //We can use the and operator &&
    return val;
} else if (val == 2 || val == 1){ //We also can use the or operator
    return val + 2;
} else {
    return 0
}

function isLess(a,b){
    return a < b;
}

function checkequal(a, b){
    return a === b ? true : false;  //The ? statement is "condition" + ? + "statement true" + : + "statement false", instead of if and else
}

