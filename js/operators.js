// Arithmetic Operators

let x = 10;
let y = 3;

console.log(x + y); // Addition
console.log(x - y); // Subtraction
console.log(x * y); // Multiplication
console.log(x / y); // Division
console.log(x % y); // Remainder (modulo)
console.log(x ** y); // Exponentiation (x to the power of y)

// Increment (++)

//Pre-increment
console.log(++x); // Increases x by 1, then returns the new value

// Post-increment
console.log(x++); // Returns x, then increases it by 1

// Decrement (--)

// Pre-decrement
console.log(--x); // Decreases x by 1, then returns the new value

// Post-decrement
console.log(x--); // Returns x, then decreases it by 1

//Assignment Operators

// These two are the same
x++;
x = x + 1;

// These two are the same
x = x + 5;
x += 5;

// These two are the same
x = x * 3;
x *= 3;

// Comparison Operators

// Relational
console.log(x > 0); // True if x is greater than 0
console.log(x >= 1); // True if x is greater than or equal to 1
console.log(x < 1); // True if x is less than 1
console.log(x <= 1); // True if x is less than or equal to 1

// Equality
console.log(x === 0); // Is x equal to 0?
console.log(x !== 0); // Is x NOT equal to 0?

// Strict equality: checks value and type
console.log(x === 0);
// Loose equality: checks value only, allows type coercion
console.log(x == 0);

// Ternary Operator (i.e. conditional operator)

let points = 110;

// Assigns "gold" to type if points is over 100; otherwise, assigns "silver".

let type = points > 100 ? "gold" : "silver";

console.log(type);

// Logical Operators

// Logical AND(&&) returns TRUE if both operands are TRUE
console.log(true && true);

let highIncome = true;
let goodCreditScore = true;

let eligibleForLoan = highIncome && goodCreditScore;

console.log(eligibleForLoan);

// Logical OR (||) returns TRUE if one of the operands is TRUE
let happy = false;
let sad = false;

let yourMood = happy || sad;

console.log(yourMood);

// The ! (NOT) operator gives the opposite boolean value

// applicationRefused is true if eligibleForLoan is false
// applicationRefused is false if eligibleForLoan is true
let applicationRefused = !eligibleForLoan;

console.log(applicationRefused);

// Logical Operators with Non-Boolean Values

console.log(0 || "hello"); // 0 is falsy, returns "hello"
console.log("hi" && 5); // both are truthy, returns 5
console.log(null || undefined); // both are falsy, returns undefined
console.log("" && "text"); // "" is falsy, returns ""
console.log(null || 1 || 2); // null is falsy, 1 is truthy, returns 1
// Short-circuiting example
console.log("" || null || 2); // "" is falsy, null is falsy, 2 is truthy, returns 2

// Use userColor if it's truthy; otherwise, use defaultColor

let userColor = "red";
let defaultColor = "blue";
let currentColor = userColor || defaultColor;

console.log(currentColor);

//BitWise Operators

console.log(5 & 1);
// Bitwise AND compares each bit of 5 (0101),
// and 1 (0001) and returns a new number with bits,
// set to 1 only where both bits are 1; here, it returns 1 (0001).

// Operator Precedence

// Multiplication (*) has higher precedence than addition (+)
// So, 3 * 4 is calculated first, then 2 is added, resulting in 14
let z = 2 + 3 * 4;

// Parentheses have highest precedence, so 2 + 3 is calculated first (5)
// Then, 5 is multiplied by 4, resulting in 20
let j = (2 + 3) * 4;

// Swapping Variables Exercise

let a = "red";
let b = "blue";

// Value overwrite: original value lost by assigning before saving it,

// After a = b, both are 'blue', original 'red' is lost
a = b;
b = a;

// Correct swap using a temporary variable:
let temp = a; // Save original 'a' value
a = b; // Assign 'b' to 'a'
b = temp; // Assign saved original 'a' to 'b'
