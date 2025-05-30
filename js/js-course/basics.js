// Exercise for learning JavaScript basics (Yes this is a mess, will organize better later on)

const interestRate = 8;
let firstName = "Faline"; // String Literal
let age = 30; // Number Literal
let isApproved = false; //Boolean Literal
let lastName = undefined;

// Concatenation (pre-ES6 way)
console.log("My name is" + firstName + "and I am" + age);
// Template Literal/Template String
console.log(`My name is ${firstName} and I am ${age}.`);

let person = {
  //Object Literal
  // Properites of the person object
  name: "Faline C.",
  age: 31,
};

let falineAge = person.age; // Dot Notation

// Add a property
person.email = "faline@website.com";

// Bracket Notaiton
let falineName = person["name"]; // Access the 'name' property using bracket notation
let selection = "name"; // Store the property name in a variable
person[selection] = "Faline"; // Use the variable to dynamically update the 'name' property

let selectedColors = ["red", "blue"];

selectedColors[2] = "green"; //JavaScript Arrays are Dynamic

selectedColors[4] = 4; // Can store different types in arrays

console.log(selectedColors.length); //Access Array properites

// Arrays of Objects
const users = [
  { name: "Alice", age: 25 },
  { name: "Bob", age: 30 },
];

// High-order array Methods

//forEach
const someNumbers = [1, 2, 3];

someNumbers.forEach(function (num) {
  console.log("Number is:", num);
});

//map
const moreNumbers = [1, 2, 3];

const doubled = moreNumbers.map(function (num) {
  return num * 2;
});

console.log(doubled); // [2, 4, 6]

//filter
const otherNumbers = [1, 2, 3, 4, 5];

const even = otherNumbers.filter(function (num) {
  return num % 2 === 0;
});

console.log(even); // [2, 4]
// Functions
// Perform a task
function greet(name) {
  console.log("Hello," + name); // Function statement
}
// Arrow Functions
//Both do the same thing—return the sum of a and b—but the arrow function is more concise.

//Without arrow function
function add(a, b) {
  return a + b;
}

//With arrow function
const add = (a, b) => a + b;

greet("Sarah");

// Calculates a value
function square(number) {
  return number * number;
}

// Constructor Functions & Prototypes

// ES5 Prototype-based
function Animal(name) {
  this.name = name;
}

Animal.prototype.speak = function () {
  console.log(this.name + " makes a noise.");
};

// ES6 Classes
class Starship {
  constructor(model) {
    this.model = model;
  }
  launch() {
    console.log(this.model + " is launching!");
  }
}

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

let userColor = "red";
let defaultColor = "blue";
let currentColor = userColor || defaultColor;

console.log(currentColor);
