#learning variables in python

cars = 100 

space_in_car = 4.0 

drivers = 30 

passengers = 90 

cars_not_driven = cars - drivers

cars_driven = drivers

car_pool_capacity = cars_driven * space_in_car

average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars avilable")
print("There are only ", drivers, "drivers aviable")
print("There will be ", cars_not_driven, "empty cars today")
print("We can transport", car_pool_capacity, "people today")
print("We have", car_pool_capacity, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")