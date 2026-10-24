
def filter_strings(words, k):
    return [word for word in words if len(word) > k]


def area(shape, *dimensions):
    if shape == "circle":
        return 3.14 * dimensions[0] ** 2
    elif shape == "rectangle":
        return dimensions[0] * dimensions[1]
    return "Invalid shape"


def split_email(email):
    username, domain = email.split("@")
    return username, domain


def sum_numbers(items):
    return sum(item for item in items if type(item) in (int, float))


class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    def book_tables(self, table_number):
        self.book_table.append(table_number)

    def customer_order(self, table_number, items):
        self.customer_orders.append({
            "table": table_number,
            "items": items
        })

    def print_menu(self):
        print("Menu:", self.menu_items)

    def print_reservations(self):
        print("Table Reservations:", self.book_table)

    def print_orders(self):
        print("Customer Orders:", self.customer_orders)


class Customer:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


class Bike:
    def __init__(self, name="", price=0):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


class MainBikeRental:
    def __init__(self):
        self.bikes = []
        self.rentals = []

    def get_bikes(self):
        return self.bikes

    def set_bikes(self, bikes):
        self.bikes = bikes

    def get_rentals(self):
        return self.rentals

    def set_rentals(self, rentals):
        self.rentals = rentals

    def addBike(self, bike, quantity=1):
        for _ in range(quantity):
            self.bikes.append(bike)

    def requestBike(self, customer, number_of_bikes):
        if customer.get_age() <= 6:
            print("Customer must be older than 6 years.")
        elif number_of_bikes <= 0:
            print("Invalid number of bikes.")
        elif number_of_bikes <= len(self.bikes):
            rented = self.bikes[:number_of_bikes]
            del self.bikes[:number_of_bikes]
            self.rentals.append({
                "customer": customer,
                "bikes": rented
            })
            print("Bikes rented successfully.")
        else:
            print("Please wait 10 minutes.")

    def returnBike(self, rentalTime, num_of_bikes):
        available_rentals = sum(
            len(rental["bikes"]) for rental in self.rentals
        )

        if num_of_bikes <= 0 or num_of_bikes > available_rentals:
            print("Invalid return quantity.")
            return

        remaining = num_of_bikes

        for rental in self.rentals[:]:
            while rental["bikes"] and remaining > 0:
                self.bikes.append(rental["bikes"].pop())
                remaining -= 1

            if not rental["bikes"]:
                self.rentals.remove(rental)

            if remaining == 0:
                break

        print("Total Bill:", rentalTime * 40)

    def totalCost(self):
        return sum(bike.get_price() for bike in self.bikes)


print("Question 1:")
print(filter_strings(["apple", "pie", "banana"], 3))

print("\nQuestion 2:")
print("Circle Area:", area("circle", 5))
print("Rectangle Area:", area("rectangle", 4, 6))

print("\nQuestion 3:")
username, domain = split_email("support@google.com")
print("Username:", username)
print("Domain:", domain)

print("\nQuestion 4:")
print("Total Sum:", sum_numbers([10, "apple", 20, True, 5]))

print("\nQuestion 5:")
restaurant = Restaurant()
restaurant.add_item_to_menu("Pizza", 100)
restaurant.add_item_to_menu("Burger", 60)
restaurant.book_tables(1)
restaurant.customer_order(1, ["Pizza", "Burger"])
restaurant.print_menu()
restaurant.print_reservations()
restaurant.print_orders()

print("\nQuestion 6:")
customer = Customer("Ahmed", 20)
rental_shop = MainBikeRental()

rental_shop.addBike(Bike("Mountain Bike", 500), 3)
rental_shop.addBike(Bike("Road Bike", 700), 2)

print("Available Bikes:", len(rental_shop.get_bikes()))
rental_shop.requestBike(customer, 2)
print("Available Bikes:", len(rental_shop.get_bikes()))
rental_shop.returnBike(3, 2)
print("Available Bikes:", len(rental_shop.get_bikes()))
print("Total Cost:", rental_shop.totalCost())
