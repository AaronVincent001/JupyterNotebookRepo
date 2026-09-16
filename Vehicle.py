class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


def main():
    print("Please enter the details for your car.")
    
    # Automatically set the vehicle type to "car" as requested
    vehicle_type = "car"
    
    # Collect user input for the Automobile attributes
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")
    
    # Create the Automobile object with the collected data
    my_car = Automobile(vehicle_type, year, make, model, doors, roof)
    
    # Print the formatted output
    print("\n--- Vehicle Data ---")
    print(f"  Vehicle type: {my_car.vehicle_type}")
    print(f"  Year: {my_car.year}")
    print(f"  Make: {my_car.make}")
    print(f"  Model: {my_car.model}")
    print(f"  Number of doors: {my_car.doors}")
    print(f"  Type of roof: {my_car.roof}")


if __name__ == "__main__":
    main()
