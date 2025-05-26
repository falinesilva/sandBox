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
