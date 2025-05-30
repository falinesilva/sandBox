// JavaScript Fundamentals – Organized from Basic to Advanced

// --------------------
// VARIABLES & DATA TYPES
// --------------------
const interestRate = 8;
let firstName = "Faline"; // String Literal
let age = 30; // Number Literal
let isApproved = false; // Boolean Literal
let lastName = undefined;

// --------------------
// STRINGS & TEMPLATE LITERALS
// --------------------
console.log("My name is" + firstName + "and I am" + age); // Concatenation
console.log(`My name is ${firstName} and I am ${age}.`); // Template Literal

// --------------------
// OBJECTS
// --------------------
let person = {
  name: "Faline C.",
  age: 31,
};

let falineAge = person.age; // Dot Notation
person.email = "faline@website.com"; // Add a property
let falineName = person["name"];
let selection = "name";
person[selection] = "Faline"; // Bracket Notation

// --------------------
// ARRAYS
// --------------------
let selectedColors = ["red", "blue"];
selectedColors[2] = "green"; // Dynamic
selectedColors[4] = 4; // Mixed types
console.log("Array length:", selectedColors.length);

// Arrays of Objects
const users = [
  { name: "Alice", age: 25 },
  { name: "Bob", age: 30 },
];

// --------------------
// FUNCTIONS
// --------------------
function greet(name) {
  console.log("Hello," + name);
}

greet("Sarah");

function square(number) {
  return number * number;
}

// Arrow Functions
function add(a, b) {
  return a + b;
}

const addArrow = (a, b) => a + b;

// --------------------
// HIGHER-ORDER ARRAY METHODS
// --------------------
const someNumbers = [1, 2, 3];
someNumbers.forEach(function (num) {
  console.log("forEach value:", num);
});

const moreNumbers = [1, 2, 3];
const doubled = moreNumbers.map(function (num) {
  return num * 2;
});
console.log("Doubled values:", doubled); // [2, 4, 6]

const otherNumbers = [1, 2, 3, 4, 5];
const even = otherNumbers.filter(function (num) {
  return num % 2 === 0;
});
console.log("Even numbers:", even); // [2, 4]

// --------------------
// OPERATORS
// --------------------
let x = 10;
let y = 3;

// Arithmetic Operators
console.log("Addition:", x + y);
console.log("Subtraction:", x - y);
console.log("Multiplication:", x * y);
console.log("Division:", x / y);
console.log("Remainder:", x % y);
console.log("Exponentiation:", x ** y);

// Increment & Decrement
console.log("Pre-increment:", ++x);
console.log("Post-increment:", x++);
console.log("Pre-decrement:", --x);
console.log("Post-decrement:", x--);

// Assignment Operators
x++;
x = x + 1;
x += 5;
x *= 3;

// Comparison Operators
console.log("x > 0:", x > 0);
console.log("x >= 1:", x >= 1);
console.log("x < 1:", x < 1);
console.log("x <= 1:", x <= 1);
console.log("x === 0:", x === 0);
console.log("x !== 0:", x !== 0);
console.log("x === 0 again:", x === 0);
console.log("x == 0:", x == 0);

// Ternary Operator
let points = 110;
let type = points > 100 ? "gold" : "silver";
console.log("Membership type:", type);

// Logical Operators
let highIncome = true;
let goodCreditScore = true;
let eligibleForLoan = highIncome && goodCreditScore;
console.log("Eligible for loan:", eligibleForLoan);

let happy = false;
let sad = false;
let yourMood = happy || sad;
console.log("Your mood:", yourMood);

let applicationRefused = !eligibleForLoan;
console.log("Application refused:", applicationRefused);

// Logical Operators with Non-Boolean Values
console.log("0 || 'hello':", 0 || "hello");
console.log("'hi' && 5:", "hi" && 5);
console.log("null || undefined:", null || undefined);
console.log("'' && 'text':", "" && "text");
console.log("null || 1 || 2:", null || 1 || 2);
console.log("'' || null || 2:", "" || null || 2);

let userColor = "red";
let defaultColor = "blue";
let currentColor = userColor || defaultColor;
console.log("Current color:", currentColor);

// --------------------
// CONSTRUCTOR FUNCTIONS & PROTOTYPES
// --------------------
function Animal(name) {
  this.name = name;
}

Animal.prototype.speak = function () {
  console.log(this.name + " makes a noise.");
};

// ES6 Class
class Starship {
  constructor(model) {
    this.model = model;
  }
  launch() {
    console.log(this.model + " is launching!");
  }
}
