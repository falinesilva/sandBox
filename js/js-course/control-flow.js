// Exercises for learning Control Flow in JS

//If...else

let hour = 10;

if (hour >= 6 && hour < 12) console.log("Good morning");
else if (hour >= 12 && hour < 18) console.log("Good afternoon");
else console.log("Good evening");

// Switch...case

let role;

switch (role) {
  case "guest":
    console.log("Guest Role");
    break;

  case "moderator":
    console.log("Moderator Role");
    break;

  default:
    console.log("Unknown Role");
}

// The same can be achieved with if..else

if (role === "guest") console.log("Guest");
else if (role === "moderator") console.log("Moderator");
else console.log("Unknown Role");

// Loops

// for
for (let i = 0; i < 5; i++) {
  console.log("Hello World");
}

for (let i = 0; i <= 5; i++) {
  if (i % 2 !== 0) console.log(i);
  i++;
}

// while

// Direct translation of the last for loop
let i = 0;
while (i <= 5) {
  if (i % 2 !== 0) console.log(i);
  i++;
}

// do-while
let x = 0;

do {
  if (x % 2 !== 0) console.log(x);
} while (i <= 5);

// for-in loop

const person = {
  name: "Sarah",
  age: 30,
};

for (let key in person) console.log(key, person[key]);

colors = ["red", "green", "blue"];

for (let index in colors) console.log(index, colors[index]);

// for-of loop

games = ["soccer", "football", "golf"];

for (let game of games) console.log(game);

//Max of two numbers exercise

result = biggerNumber(2, 12);

console.log(result);

function biggerNumber(x, y) {
  if (x > y) return x;
  else return y;
}

// Landscape or Portrait exercise

let photo = isLandscape(100, 5);

console.log(photo);

function isLandscape(width, height) {
  return width > height;
}

// FizzBuzz Exercise

const output = fizzBuzz("cat");

console.log(output);

function fizzBuzz(input) {
  if (typeof input != "number") return NaN;
  else if (input % 5 === 0 && input % 3 === 0) return "FizzBuzz";
  else if (input % 3 === 0) return "Fizz";
  else if (input % 5 === 0) return "Buzz";
  else return input;
}

// Demerit Points

console.log(checkSpeed(20));

function checkSpeed(speed) {
  if (speed < 75) return "ok"; // TODO: Magic number
  let points = Math.floor(speed - 70) / 5; // TODO: Magic number
  if (points > 12) return "License suspended";
  else return points;
}

// Even Odd Exercise

showNumbers(4);

function showNumbers(limit) {
  for (let i = 0; i < limit; i++) {
    // if (i % 2 === 0) console.log(i, "EVEN");
    // else console.log(i, "ODD");

    const message = i % 2 === 0 ? "EVEN" : "ODD";
    console.log(i, message);
  }
}

// Count Truthy Exercise

const testArray = [null, 1, 2, 3, "hello", "hello 2"];

console.log(countTruthy(testArray));

function countTruthy(array) {
  let truthies = 0;
  for (let i = 0; i < array.length; i++) {
    //TODO: Tighten up with for..of loop
    if (array[i]) truthies++;
  }
  return truthies;
}

// String Properties Exercise

const movie = {
  title: "Not Time to Die",
  rating: 8,
  director: "Mr. Smith",
  year: 2025,
};

showProperties(movie);

function showProperties(object) {
  for (let key in object)
    if (typeof object[key] === "string") console.log(key, object[key]);
}

// Multiples Exercise

function sum(limit) {
  let total = 0; // Initialize total sum

  for (let i = 1; i <= limit; i++) {
    // Loop from 1 to limit
    if (i % 3 === 0 || i % 5 === 0) total += i; // Add if multiple of 3 or 5
  }

  return total; // Return the final sum
}

console.log(sum(10));
