class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print(f"The {self.year} {self.make} {self.model} is accelerating. Current speed: {self.speed} km/h")

    def brake(self):
        if self.speed >= 10:
            self.speed -= 10
            print(f"The {self.year} {self.make} {self.model} is braking. Current speed: {self.speed} km/h")
        else:
            print(f"The {self.year} {self.make} {self.model} has already stopped.")

car = Car("Toyota", "Camry", 2021)
print(f"Car: {car.year} {car.make} {car.model}\n")

while True:
    action = input("What do you want to do? (accelerate, brake, exit) ")
    if action == "accelerate":
        car.accelerate()
    elif action == "brake":
        car.brake()
    elif action == "exit":
        break
    else:
        print("Invalid action. Please try again.\n")

print("Thank you for using the car simulator!")