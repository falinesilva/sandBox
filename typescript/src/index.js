// TypeScript Exercises
// Primitives without inference
var cat = "Nina is my cute cat.";
cat.toLocaleLowerCase();
var value = 1;
var isAnimals = true;
console.log(cat);
// Primitives with inference
var car = "Toyota Supra";
var year = 1990;
var isFast = true;
console.log(car);
// Functions with defaults
function sum(a, b) {
    if (b === void 0) { b = 5; }
    return a + b;
}
var result = sum(5, 100);
console.log("Result", result);
// Functions with optionals parameters
function fuelUsed(tank, fuel, nitro) {
    var remainingFuel = tank - (tank * fuel) / 100;
    if (nitro) {
        remainingFuel += 1000;
    }
    return remainingFuel;
}
var myTripFuel = fuelUsed(100, 40, true);
console.log("Fuel Used:", myTripFuel);
// Object type defined inline a function parameter
function printColors(colors) {
    console.log("Primary", colors.primary);
    console.log("Secondary", colors.secondary);
}
// Inline object type with optional chaining on parameter property
var house = { size: "Single family", condition: "Fair" };
function displayHouse(house) {
    var _a;
    console.log("House Size:", house.size, "House Condition:", (_a = house.condition) === null || _a === void 0 ? void 0 : _a.toLocaleLowerCase());
}
displayHouse(house);
// Arrays
