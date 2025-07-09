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
