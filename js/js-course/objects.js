// Exercises for learning about Objects in JavaScript

const circle = {
  // Object literal syntax
  radius: 1,
  color: "blue",
  location: {
    x: 10,
    y: 5,
  },
  isVisible: true, // Nested object
  draw: function circleDraw() {
    // Nested function (Method)
    // Nested function
    console.log("Circle");
  },
};

circle.draw(); // Calling the draw 'Method' of the circle object

// Exercise Grade

const grades = [80, 80, 50];

console.log(letterGrade(grades));
// TODO: Apply single responsibility,
// split into separate functions for average and letter grade.

function letterGrade(grades) {
  let sum = 0;
  for (score in grades) {
    sum += grades[score];
  }
  let average = sum / grades.length;

  if (average < 60) return "F";
  else if (average < 70) return "D";
  else if (average < 80) return "C";
  else if (average < 90) return "B";
  return "A";
}
