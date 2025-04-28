# There are 100 cars
cars = 100
# Each car can carry 4 passengers
space_in_a_car = 4
# There are 30 drivers
drivers = 30
# There are 90 total passengers
passengers = 90
# Each car has 1 driver, so there are 100 - 30 = 70 undriven cars
cars_not_driven = cars - drivers
# Each car has 1 driver, so 70 drivers -> 70 driven cars
cars_driven = drivers
# Total carpool capacity is the number of cars with drivers (30) times the passenger space in each car (4) = 120
carpool_capacity = cars_driven * space_in_a_car
# We have 90 passengers and 30 cars with drivers, so each car can carry an average of 3 passengers
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
