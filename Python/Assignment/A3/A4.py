from datetime import datetime

class Vehicle:
    def __init__(self, vehicle_id, brand, model, rental_price_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day
        self.is_available = True

    def __str__(self):
        return f"Vehicle ID: {self.vehicle_id}, {self.brand} {self.model}, Price per day: ${self.rental_price_per_day}, Available: {self.is_available}"


class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day, num_doors):
        super().__init__(vehicle_id, brand, model, rental_price_per_day)
        self.num_doors = num_doors

    def __str__(self):
        return f"Car: {super().__str__()}, Doors: {self.num_doors}"


class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day, bike_type):
        super().__init__(vehicle_id, brand, model, rental_price_per_day)
        self.bike_type = bike_type

    def __str__(self):
        return f"Bike: {super().__str__()}, Type: {self.bike_type}"


class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day, load_capacity):
        super().__init__(vehicle_id, brand, model, rental_price_per_day)
        self.load_capacity = load_capacity

    def __str__(self):
        return f"Truck: {super().__str__()}, Load Capacity: {self.load_capacity} tons"


class Customer:
    def __init__(self, name, driver_license_number):
        self.name = name
        self.driver_license_number = driver_license_number
        self.rented_vehicles = []

    def rent_vehicle(self, vehicle, rental_service):
        if vehicle.is_available:
            rental_service.rent_vehicle(self, vehicle)
        else:
            print(f"Vehicle {vehicle.vehicle_id} is not available for rent.")

    def return_vehicle(self, vehicle, rental_service, return_date):
        rental_service.return_vehicle(self, vehicle, return_date)

    def __str__(self):
        return f"Customer: {self.name}, License: {self.driver_license_number}, Rented Vehicles: {[vehicle.vehicle_id for vehicle in self.rented_vehicles]}"


class RentalRecord:
    def __init__(self, customer, vehicle, rental_date, return_date=None):
        self.customer = customer
        self.vehicle = vehicle
        self.rental_date = rental_date
        self.return_date = return_date

    def calculate_rental_cost(self):
        if self.return_date:
            duration = (self.return_date - self.rental_date).days
            return duration * self.vehicle.rental_price_per_day
        return 0

    def __str__(self):
        return f"Rental Record: {self.customer.name} rented {self.vehicle.brand} {self.vehicle.model} (ID: {self.vehicle.vehicle_id}) on {self.rental_date.strftime('%Y-%m-%d')}"

class RentalService:
    def __init__(self):
        self.fleet = []
        self.rental_history = []

    def add_vehicle(self, vehicle):
        self.fleet.append(vehicle)

    def view_available_vehicles(self):
        available_vehicles = [vehicle for vehicle in self.fleet if vehicle.is_available]
        if not available_vehicles:
            print("No vehicles available.")
        else:
            print("Available Vehicles:")
            for vehicle in available_vehicles:
                print(vehicle)

    def rent_vehicle(self, customer, vehicle):
        vehicle.is_available = False
        customer.rented_vehicles.append(vehicle)
        rental_record = RentalRecord(customer, vehicle, datetime.now())
        self.rental_history.append(rental_record)
        print(f"{customer.name} rented {vehicle.brand} {vehicle.model}.")

    def return_vehicle(self, customer, vehicle, return_date):
        if vehicle in customer.rented_vehicles:
            vehicle.is_available = True
            customer.rented_vehicles.remove(vehicle)
            for record in self.rental_history:
                if record.customer == customer and record.vehicle == vehicle and not record.return_date:
                    record.return_date = return_date
                    rental_cost = record.calculate_rental_cost()
                    print(f"{customer.name} returned {vehicle.brand} {vehicle.model}. Total rental cost: ${rental_cost:.2f}")
                    break
        else:
            print(f"{customer.name} does not have this vehicle rented.")

    def view_rental_history(self, customer):
        print(f"Rental History for {customer.name}:")
        for record in self.rental_history:
            if record.customer == customer:
                return_info = f"Returned on {record.return_date.strftime('%Y-%m-%d')}" if record.return_date else "Not yet returned"
                print(f"{record} - {return_info}")


# Test the Vehicle Rental System
if __name__ == "__main__":
    # Create a rental service
    rental_service = RentalService()

    # Add vehicles to the fleet
    car1 = Car(101, "Toyota", "Corolla", 50, 4)
    bike1 = Bike(201, "Yamaha", "MT-09", 30, "Sport")
    truck1 = Truck(301, "Ford", "F-150", 100, 5)
    
    rental_service.add_vehicle(car1)
    rental_service.add_vehicle(bike1)
    rental_service.add_vehicle(truck1)

    # View available vehicles
    rental_service.view_available_vehicles()

    # Create a customer
    customer1 = Customer("John Doe", "D12345")

    # Rent a vehicle
    customer1.rent_vehicle(car1, rental_service)

    # View available vehicles after renting
    rental_service.view_available_vehicles()

    # Return the vehicle
    customer1.return_vehicle(car1, rental_service, datetime(2024, 9, 10))

    # View rental history for the customer
    rental_service.view_rental_history(customer1)
