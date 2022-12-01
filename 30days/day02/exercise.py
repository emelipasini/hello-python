first_name = "Carl"
last_name = "Sagan"
full_name = first_name + " " + last_name
country = "USA"
city = "Brooklyn"
age = 62
year = 1996
is_married = True
is_light_on = False

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))

print(len(first_name))
print(len(first_name) < len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = 3.14 * (radius ** 2)
circum_of_circle = 2 * 3.14 * radius

radius = input("Enter radius: ")
radius = int(radius)
print(3.14 * (radius ** 2))

first_name = input("Enter your first name: ")
last_name = input("Enter yout last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

help("keywords")
