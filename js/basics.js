// JavaScript Fundamentals – One Example per Topic (Ordered from Basic to Advanced)

// --------------------
// SCRIPT TAGS (for index.html)
// --------------------
// <script src="script.js"></script> – placed before closing </body> tag

// --------------------
// CONSOLE OUTPUT
// --------------------
console.log("JavaScript is running!");

// --------------------
// VARIABLES
// --------------------
const pi = 3.14;
let message = "Hello World";
var count = 5;

// --------------------
// DATA TYPES
// --------------------
let number = 42; // Number
let text = "Faline"; // String
let isActive = true; // Boolean
let nothingHere = null; // Null
let notAssigned; // Undefined

// --------------------
// STRINGS & STRING METHODS
// --------------------
let sentence = "Learning JavaScript";
console.log(sentence.includes("JavaScript"));

// --------------------
// ARRAYS
// --------------------
let fruits = ["apple", "banana", "cherry"];
console.log(fruits.length);

// --------------------
// OBJECT LITERALS
// --------------------
let profile = {
  username: "faline123",
  age: 31,
  isVerified: false,
};
console.log(profile.username);

// --------------------
// ARRAYS OF OBJECTS & JSON
// --------------------
let users = [
  { id: 1, name: "Alice" },
  { id: 2, name: "Bob" },
];
console.log(JSON.stringify(users));

// --------------------
// LOOPS
// --------------------
for (let i = 1; i <= 3; i++) {
  console.log("Number:", i);
}

// --------------------
// HIGHER-ORDER ARRAY METHODS
// --------------------
let nums = [1, 2, 3, 4];
let evens = nums.filter((n) => n % 2 === 0);
console.log(evens);

// --------------------
// CONDITIONALS
// --------------------
let temp = 72;
if (temp > 80) {
  console.log("Too hot");
} else if (temp < 60) {
  console.log("Too cold");
} else {
  console.log("Just right");
}

// --------------------
// FUNCTIONS
// --------------------
function greetUser(user) {
  return `Hello, ${user}!`;
}
console.log(greetUser("Faline"));

// --------------------
// ARROW FUNCTIONS
// --------------------
const divide = (x, y) => x / y;
console.log(divide(10, 2));

// --------------------
// CONSTRUCTOR FUNCTIONS & PROTOTYPES
// --------------------
function Pet(name) {
  this.name = name;
}
Pet.prototype.talk = function () {
  console.log(`${this.name} says hello!`);
};
let cat = new Pet("Whiskers");
cat.talk();

// --------------------
// ES6 CLASSES
// --------------------
class Appliance {
  constructor(type) {
    this.type = type;
  }
  start() {
    console.log(`${this.type} is starting.`);
  }
}
let blender = new Appliance("Blender");
blender.start();

// --------------------
// WINDOW OBJECT & DOM
// --------------------
console.log("Window height:", window.innerHeight);
document.title = "JavaScript Practice";

// --------------------
// MANIPULATING THE DOM
// --------------------
// Single element selector (only selects the first one)

console.log(document.getElementById("my-form"));
console.log(document.querySelector("h1"));

// Multiple element selector
console.log(document.querySelectorAll(".item"));
// Gives a node list similar to an array

// Create and add new element to the page
let paragraph = document.createElement("p");
paragraph.textContent = "This is added with JavaScript.";
document.body.appendChild(paragraph);

// --------------------
// EVENTS
// --------------------
paragraph.addEventListener("mouseover", () => {
  console.log("You hovered over the paragraph!");
});

// --------------------
// FORM SCRIPT
// --------------------
document.body.innerHTML += `
  <form id="signup">
    <input type="email" name="email" placeholder="Enter your email">
    <button type="submit">Sign Up</button>
  </form>
`;

document.querySelector("#signup").addEventListener("submit", function (e) {
  e.preventDefault();
  console.log("Signup form submitted");
});
