
let a = [9, 9, 9];
let b = [1];
let c = [];

// Reverse the arrays to start from the least significant digit
a.reverse();
b.reverse();

let carry = 0;
let maxLen = Math.max(a.length, b.length);

for (let i = 0; i < maxLen; i++) {
    let digitA = i < a.length ? a[i] : 0;
    let digitB = i < b.length ? b[i] : 0;

    let sum = digitA + digitB + carry;
    c.push(sum % 10);
    carry = Math.floor(sum / 10);
}

if (carry > 0) {
    c.push(carry);
}

// Reverse the result back
c.reverse();



