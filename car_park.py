class CarPark:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        self.vehicles.remove(vehicle)

    def get_total_count(self):
        return len(self.vehicles)

    def get_total_value(self):
        return sum(vehicle.price for vehicle in self.vehicles)

    def get_all_vehicles(self):
        return [vehicle.get_description() for vehicle in self.vehicles]


class Vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def get_description(self):
        return f"{self.brand} {self.model} ({self.year}) - ${self.price}"


class Car(Vehicle):
    def __init__(self, brand, model, year, price, num_seats):
        super().__init__(brand, model, year, price)
        self.num_seats = num_seats

    def get_description(self):
        return f"Car: {super().get_description()}, Seats: {self.num_seats}"


class Truck(Vehicle):
    def __init__(self, brand, model, year, price, max_load):
        super().__init__(brand, model, year, price)
        self.max_load = max_load

    def get_description(self):
        return f"Truck: {super().get_description()}, Max Load: {self.max_load}"


class Bus(Vehicle):
    def __init__(self, brand, model, year, price, capacity):
        super().__init__(brand, model, year, price)
        self.capacity = capacity

    def get_description(self):
        return f"Bus: {super().get_description()}, Capacity: {self.capacity}"


# Менюха
def print_menu():
    print("Menu:")
    print("1. Add a vehicle to the car park")
    print("2. Remove a vehicle from the car park")
    print("3. Display the total count of vehicles in the car park")
    print("4. Display the total value of vehicles in the car park")
    print("5. Display the list of vehicles in the car park")
    print("0. Exit")


car_park = CarPark()

while True:
    print_menu()
    choice = input("Enter your choice (0-5): ")

# Додавання нового автомобілю до парку
    if choice == "1":
        vehicle_type = input("Enter the type of vehicle (car/truck/bus): ")
        brand = input("Enter the brand: ")
        model = input("Enter the model: ")
        year = int(input("Enter the year: "))
        price = float(input("Enter the price: "))

        if vehicle_type == "car":
            num_seats = int(input("Enter the number of seats: "))
            vehicle = Car(brand, model, year, price, num_seats)
        elif vehicle_type == "truck":
            max_load = float(input("Enter the maximum load: "))
            vehicle = Truck(brand, model, year, price, max_load)
        elif vehicle_type == "bus":
            capacity = int(input("Enter the capacity: "))
            vehicle = Bus(brand, model, year, price, capacity)
        else:
            print("Invalid vehicle type.")
            continue

        car_park.add_vehicle(vehicle)
        print("Vehicle added to the car park.")

# Видалення автомобілю з парку
    elif choice == "2":
        if car_park.get_total_count() == 0:
            print("The car park is empty.")
            continue

        print("Vehicles in the car park:")
        for index, vehicle in enumerate(car_park.get_all_vehicles()):
            print(f"{index+1}. {vehicle}")

        vehicle_index = int(input("Enter the index of the vehicle to remove: "))
        if vehicle_index < 1 or vehicle_index > car_park.get_total_count():
            print("Invalid vehicle index.")
            continue

        vehicle = car_park.vehicles[vehicle_index - 1]
        car_park.remove_vehicle(vehicle)
        print("Vehicle removed from the car park.")

# Виведення загальної кількості автомобілів в парку
    elif choice == "3":
        print("Total count of vehicles in the car park:", car_park.get_total_count())

# Виведення загальної вартості автомобілів в парку
    elif choice == "4":
        print("Total value of vehicles in the car park: $", car_park.get_total_value())

# Виведення списку всіх автомобілів в парку
    elif choice == "5":
        print("Vehicles in the car park:")
        for index, vehicle in enumerate(car_park.get_all_vehicles()):
            print(f"{index+1}. {vehicle}")

# Вихід
    elif choice == "0":
        break

    else:
        print("Invalid choice. Please enter a number from 0 to 5.")