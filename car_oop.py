class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_engine_on = False
        self.current_speed = 0

    def start_engine(self):
        if not self.is_engine_on:
            print("Engine started.")
            self.is_engine_on = True
        else:
            print("The engine is already running.")

    def stop_engine(self):
        if self.is_engine_on:
            print("Engine stopped.")
            self.is_engine_on = False
            self.current_speed = 0
        else:
            print("The engine is already off.")

    def accelerate(self, speed_increase):
        if self.is_engine_on:
            self.current_speed += speed_increase
            print(f"Accelerated to {self.current_speed} km/h.")
        else:
            print("Cannot accelerate, the engine is off.")

    def brake(self, speed_decrease):
        if self.is_engine_on:
            if self.current_speed >= speed_decrease:
                self.current_speed -= speed_decrease
                print(f"Decelerated to {self.current_speed} km/h.")
            else:
                print("Cannot brake below 0 km/h.")
        else:
            print("Cannot brake, the engine is off.")

# Create an instance of the Car class
my_car = Car(make="Toyota", model="Camry", year=2022, color="Blue")

# Interact with the car
my_car.start_engine()
my_car.accelerate(30)
my_car.brake(1)
my_car.stop_engine()
my_car.stop_engine()

