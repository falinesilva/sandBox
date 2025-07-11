// TypeScript Exercises

// Primitives without inference

let cat: string = "Nina is my cute cat.";

cat.toLocaleLowerCase();

let value: number = 1;

let isAnimals: boolean = true;

console.log(cat);

// Primitives with inference

let car = "Toyota Supra";

let year = 1999;

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

// Strict arrays

const cars: {
  brand: string;
  model: string;
  year: number;
}[] = [
  { brand: "Toyota", model: "Supra", year: 1999 },
  { brand: "Nissan", model: "Skyline", year: 1999 },
  { brand: "Mazda", model: "RX-7", year: 1995 },
];

const formatedCarList: string[] = cars.map(
  (car: { brand: string; model: string; year: number }): string => {
    return `<li>Brand: ${car.brand} | Model:  ${car.model} | Year: ${car.year}</li>`;
  }
);

const liCarListString: string = formatedCarList.join("");

document.getElementById("cars")!.innerHTML = `Cars: ${liCarListString}`;

// Interfaces

interface Engine {
  cylinders: number;
  liters: number;
  horsepower: number;
  isTurbo?: boolean;
  carList?: [{ car: "Skyline"; make: "Nissan"; year: 1999 }];
  preferred?: (racing: string) => void;
}

const engines: Engine[] = [
  {
    cylinders: 6,
    liters: 3.5,
    horsepower: 300,
    preferred: (racing: string) => {
      console.log(
        `For ${racing}, engines with ${engines[0].liters} litrs is preferred`
      );
    },
  },
  { cylinders: 8, liters: 6.0, horsepower: 410 },
];

engines[0].preferred?.("drifting");
const formatedEngineList: string[] = engines.map((engine: Engine): string => {
  return `<li>Cylinders: ${engine.cylinders} | Liters: ${engine.liters} | HP: ${engine.horsepower}`;
});

const liEngineListString: string = formatedEngineList.join("");

document.getElementById(
  "engines"
)!.innerHTML = `Engines: ${liEngineListString}`;

// Classes and access modifiers

class Vehicle {
  cost: number;
  private brand: string;
  static color: string = "Red";

  constructor(cost: number, brand: string) {
    this.cost = cost;
    this.brand = brand;
  }
  setBrand(newBrand: string): void {
    this.brand =
      newBrand[0].toUpperCase() +
      newBrand.slice(1, newBrand.length).toLowerCase();
  }

  getBrand(): string {
    return this.brand;
  }
}

const honda = new Vehicle(90000, "honda");

honda.setBrand("nissan");

console.log(honda);
console.log(Vehicle.color);

// Tuples

const rgb: [number, number, number] = [255, 2, 133];

// TS allows `push` on tuples because it's treated as a mutable array at runtime,
// and type checks don't block extra elements without readonly.
rgb.push("1");

console.log(rgb);

const topThreeBrands: readonly [string, string, string] = [
  "Nissan",
  "Toyota",
  "Mazda",
];

// TS shows an error here because the tuple is readonly,
// but JS still runs it since readonly is stripped at compile time.
topThreeBrands.push("Honda");

console.log(topThreeBrands);
