// TypeScript Exercises

// Primitives without inference

let cat: string = "Nina is my cute cat.";

cat.toLocaleLowerCase();

let value: number = 1;

let isAnimals: boolean = true;

console.log(cat);

// Primitives with inference

let car = "Toyota Supra";

let year = 1990;

let isFast = true;

console.log(car);

// Functions with defaults

function sum(a: number, b: number = 5): number {
  return a + b;
}

let result = sum(5, 100);

console.log("Result", result);

// Functions with optionals parameters

function fuelUsed(tank: number, fuel: number, nitro?: boolean): number {
  let remainingFuel = tank - (tank * fuel) / 100;
  if (nitro) {
    remainingFuel += 1000;
  }
  return remainingFuel;
}

let myTripFuel = fuelUsed(100, 40, true);

console.log("Fuel Used:", myTripFuel);

// Object type defined inline a function parameter

function printColors(colors: { primary: string; secondary: string }) {
  console.log("Primary", colors.primary);
  console.log("Secondary", colors.secondary);
}

// Inline object type with optional chaining on parameter property

const house = { size: "Single family", condition: "Fair" };

function displayHouse(house: { size: string; condition?: string }) {
  console.log(
    "House Size:",
    house.size,
    "House Condition:",
    house.condition?.toLocaleLowerCase()
  );
}

displayHouse(house);

// Arrays
