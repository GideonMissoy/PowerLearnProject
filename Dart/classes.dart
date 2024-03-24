import 'dart:io';

// Interface for vehicles
abstract class Vehicle {
  void start();
  void stop();
}

// Base class for vehicles
class Car implements Vehicle {
  String model;
  int year;

  Car(this.model, this.year);

  @override
  void start() {
    print('$model ($year) - Engine started');
  }

  @override
  void stop() {
    print('$model ($year) - Engine stopped');
  }
}

// Subclass of Car
class ElectricCar extends Car {
  ElectricCar(String model, int year) : super(model, year);

  @override
  void start() {
    print('$model ($year) - Electric motor started');
  }
}

void main() {
  // Create an instance of ElectricCar
  var tesla = ElectricCar('Tesla Model S', 2022);

  // Demonstrate method overriding
  tesla.start();
  tesla.stop();

  // Read data from file and initialize objects
  File file = File('cars.txt');
  List<String> lines = file.readAsLinesSync();
  List<Car> cars = [];

  for (var line in lines) {
    var data = line.split(',');
    var model = data[0];
    var year = int.parse(data[1]);
    cars.add(Car(model, year));
  }

  // Demonstrate the use of a loop
  for (var car in cars) {
    car.start();
    car.stop();
  }
}