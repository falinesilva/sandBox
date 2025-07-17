console.log("🚀 Reloaded at:", new Date().toLocaleTimeString());

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
// rgb.push("1");

console.log(rgb);

const topThreeBrands: readonly [string, string, string] = [
  "Nissan",
  "Toyota",
  "Mazda",
];

// TS shows an error here because the tuple is readonly,
// but JS still runs it since readonly is stripped at compile time.
// topThreeBrands.push("Honda");

console.log(topThreeBrands);

// Unions

let theValue: number | string | boolean | [];

interface Square {
  kind: "square";
  size: number;
}

interface Circle {
  kind: "circle";
  radius: number;
}

let myShape: Square | Circle;

myShape = {
  kind: "square",
  size: 1337,
};

// Narrow the union type using a discriminant property ('kind') to access specific fields

function displayShape(shape: Square | Circle): void {
  console.log("Kind:", shape.kind);
  if (shape.kind === "circle") {
    console.log("Radius:", shape.radius);
  } else {
    console.log("Size", shape.size);
  }
}

displayShape(myShape);

// Be careful: unions in arrays apply to each element, not the array as a whole

let exampleArray: (number | string | (Square | Circle))[] = [
  1,
  "example",
  myShape,
];

// 'is' operator to narrow types

interface Fish {
  swim: () => void;
}

interface Bird {
  fly: () => void;
  walk: () => void;
}

function getRandomPet(): Fish | Bird {
  if (Math.random() > 0.5) {
    return { swim: () => console.log("Swimming...") };
  } else {
    return {
      fly: () => console.log("Flying"),
      walk: () => console.log("Walking"),
    };
  }
}

function isFish(pet: Fish | Bird): pet is Fish {
  return "swim" in pet;
}

const pet = getRandomPet();

if (isFish(pet)) {
  console.log("It's a fish");
} else {
  console.log("It's a bird");
}

// Enums (commented out because of nodemon limitation)

// enum Direction {
//   North = "North",
//   South = "South",
//   East = "East",
//   West = "West",
// }

// const direction: Direction = Direction.North;

// function move(direction: Direction) {
//   console.log("Moving", direction);
// }

// move(direction);

// Types vs. Interfaces

interface VehicleInterface {
  maxSpeed: number;
  brand: string;
}

type VehicleType = {
  maxSpeed: number;
  brand: string;
};

let v1: VehicleInterface;

let v2: VehicleType;

v1 = {
  brand: "Subaru",
  maxSpeed: 200,
  year: 1999,
};

v2 = {
  brand: "Subaru",
  maxSpeed: 200,
};

// Types cannot be redefined or merged once declared but can extend with &

type Car = {
  horsePower: number;
} & VehicleInterface;

let usedCar: Car;

// You can add types to interfaces
interface VehicleInterface {
  year: number;
}

let myNewCar: VehicleInterface;

// Heritage is reusing and extending existing classes or interfaces using extends

interface Garage extends VehicleInterface {
  floorMaterial: string;
  squareFeet: number;
}

let myNewGarage: Garage = {
  floorMaterial: "cement",
  squareFeet: 100,
  maxSpeed: 200,
  brand: "Dupont",
  year: 1999,
};

// Class accessors

class Tire {
  private _radius: number;

  constructor(radius: number) {
    if (radius > 0) {
      this._radius = radius;
    } else {
      console.log("Invalid tire radius.");
      this._radius = 0;
    }
  }
  set radius(radius: number) {
    if (radius > 0) {
      this._radius = radius;
    } else {
      console.log("Invalid tire radius.");
    }
  }

  get radius(): number {
    return this._radius;
  }
}

const tire = new Tire(205);

tire.radius = -2;

console.log(tire);

// Protected access modifer

class Animal {
  protected name: string;

  constructor(name: string) {
    this.name = name;
  }
}

class Dog extends Animal {
  speak() {
    return `${this.name} says woof!`;
  }
}

const dog = new Dog("Oreo");
// console.log(dog.name); Error: 'name' is protected
console.log(dog.speak());

// Implement

interface Flyable {
  altitude: number;
  fly(): void;
}

class Plane implements Flyable {
  altitude: number;

  constructor() {
    this.altitude = 0;
  }

  fly() {
    this.altitude = 30000;
    console.log(`Flying at ${this.altitude} feet.`);
  }
}

// Abstract

abstract class VideoGame {
  protected name: string;
  protected genre: string;
  protected platform: string;

  constructor(name: string, genre: string, platform: string) {
    this.name = name;
    this.genre = genre;
    this.platform = platform;
  }
}

class ArcadeGame extends VideoGame {
  constructor(name: string, platform: string) {
    super(name, "Arcade", platform);
  }
}

class ShooterGame extends VideoGame {
  constructor(name: string, platform: string) {
    super(name, "Shooter", platform);
  }
}

const donkeyKong = new ArcadeGame("Donkey Kong", "Gameboy");

const callOfDuty = new ShooterGame("Call of Duty", "PC");

console.log(donkeyKong);
console.log(callOfDuty);

// Generics

const numbers = [1, 2, 3];

const strings = ["Hello", "my", "friend"];

const booleans = [true, true, false];

interface Hero {
  name: string;
  superPower: string;
}

const h1: Hero = {
  name: "The flash",
  superPower: "Run super fast",
};

const h2: Hero = {
  name: "The Hulk",
  superPower: "Super strong",
};

const h3: Hero = {
  name: "Batman",
  superPower: "Is rich",
};

const h4: Hero = {
  name: "Superman",
  superPower: "Basically a God",
};

const heros = [h1, h2, h3, h4];

// Convention is to use 'T' to represent a generic (placeholder) type
function removeLastElement<T>(array: T[]): T[] {
  return array.slice(0, array.length - 1);
}

console.log(numbers);
const newNumbers = removeLastElement(numbers);
console.log(newNumbers);

console.log(heros);
const newHeros = removeLastElement<Hero>(heros);
console.log(newHeros);

// Generic classes

class SmartArray<T> {
  private array: T[] = [];

  constructor(array: T[]) {
    this.array = array;
  }

  get values() {
    return this.array;
  }

  shuffle(): T[] {
    return this.array.sort(() => Math.random() - 0.5);
  }

  push(element: T): void {
    this.array.push(element);
  }

  removeLast(): T[] {
    this.array.slice(0, this.array.length - 1);
    return this.array;
  }
}

const heroSmartArray = new SmartArray<Hero>(heros);

const shuffled = heroSmartArray.shuffle();

console.log(shuffled);

shuffled.push({
  name: "WonderWoman",
  superPower: "fly",
});

console.log(shuffled);
