// TypeScript Exercises
var _a, _b;
// Primitives without inference
var cat = "Nina is my cute cat.";
cat.toLocaleLowerCase();
var value = 1;
var isAnimals = true;
console.log(cat);
// Primitives with inference
var car = "Toyota Supra";
var year = 1999;
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
// Strict arrays
var cars = [
    { brand: "Toyota", model: "Supra", year: 1999 },
    { brand: "Nissan", model: "Skyline", year: 1999 },
    { brand: "Mazda", model: "RX-7", year: 1995 },
];
var formatedCarList = cars.map(function (car) {
    return "<li>Brand: ".concat(car.brand, " | Model:  ").concat(car.model, " | Year: ").concat(car.year, "</li>");
});
var liCarListString = formatedCarList.join("");
document.getElementById("cars").innerHTML = "Cars: ".concat(liCarListString);
var engines = [
    {
        cylinders: 6,
        liters: 3.5,
        horsepower: 300,
        preferred: function (racing) {
            console.log("For ".concat(racing, ", engines with ").concat(engines[0].liters, " litrs is preferred"));
        },
    },
    { cylinders: 8, liters: 6.0, horsepower: 410 },
];
(_b = (_a = engines[0]).preferred) === null || _b === void 0 ? void 0 : _b.call(_a, "drifting");
var formatedEngineList = engines.map(function (engine) {
    return "<li>Cylinders: ".concat(engine.cylinders, " | Liters: ").concat(engine.liters, " | HP: ").concat(engine.horsepower);
});
var liEngineListString = formatedEngineList.join("");
document.getElementById("engines").innerHTML = "Engines: ".concat(liEngineListString);
// Classes and access modifiers
var Vehicle = /** @class */ (function () {
    function Vehicle(cost, brand) {
        this.cost = cost;
        this.brand = brand;
    }
    Vehicle.prototype.setBrand = function (newBrand) {
        this.brand =
            newBrand[0].toUpperCase() +
                newBrand.slice(1, newBrand.length).toLowerCase();
    };
    Vehicle.prototype.getBrand = function () {
        return this.brand;
    };
    Vehicle.color = "Red";
    return Vehicle;
}());
var honda = new Vehicle(90000, "honda");
honda.setBrand("nissan");
console.log(honda);
console.log(Vehicle.color);
// Tuples
var rgb = [255, 2, 133];
// TS allows `push` on tuples because it's treated as a mutable array at runtime,
// and type checks don't block extra elements without readonly.
rgb.push("1");
console.log(rgb);
var topThreeBrands = [
    "Nissan",
    "Toyota",
    "Mazda",
];
// TS shows an error here because the tuple is readonly,
// but JS still runs it since readonly is stripped at compile time.
topThreeBrands.push("Honda");
console.log(topThreeBrands);
