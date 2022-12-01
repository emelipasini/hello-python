# Day 2

## Built in functions

In Python we have lots of built in functions that are globally available for your use, that means you can make use of them without importing or configuring.

```py
len("Hello, world") # it counts the number of characters including space
str(10) # converts number to string
int("10") # converts string to number
float(10) # converts integer to decimal
input("Enter your name: ") # it takes user input
help("keyboards") # prints all python reserverd words

min(20, 30, 40, 50) # gives you the minimum value
max(20, 30, 40, 50) # gives you the maximum value
# it also can take a list as an argument

sum([20, 30, 40, 50]) # it takes only a list as an argument and return the sum
```

![Built in functions](./builtin-functions.png)

## Variables

Variables store data in a computer memory. Mnemonic variables are recommended to use, this are variables with easy to remember and associate names.

Python variable name rules:
- It must start with a letter or the underscore character
- It cannot start with a number
- It can only contain alphanumeric characters and underscores
- Variables names are case sensitive

Standard Python variable naming style is snake_case

```py
first_name = "Name"
first_name_to_list = list(first_name)
print(first_name_to_list) # ["N", "a", "m", "e"]
```

## Exercises

### Exercises: Level 1

    Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
    Write a python comment saying 'Day 2: 30 Days of python programming'
    Declare a first name variable and assign a value to it
    Declare a last name variable and assign a value to it
    Declare a full name variable and assign a value to it
    Declare a country variable and assign a value to it
    Declare a city variable and assign a value to it
    Declare an age variable and assign a value to it
    Declare a year variable and assign a value to it
    Declare a variable is_married and assign a value to it
    Declare a variable is_true and assign a value to it
    Declare a variable is_light_on and assign a value to it
    Declare multiple variable on one line

### Exercises: Level 2

    Check the data type of all your variables using type() built-in function
    Using the len() built-in function, find the length of your first name
    Compare the length of your first name and your last name
    Declare 5 as num_one and 4 as num_two
        Add num_one and num_two and assign the value to a variable total
        Subtract num_two from num_one and assign the value to a variable diff
        Multiply num_two and num_one and assign the value to a variable product
        Divide num_one by num_two and assign the value to a variable division
        Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
        Calculate num_one to the power of num_two and assign the value to a variable exp
        Find floor division of num_one by num_two and assign the value to a variable floor_division
    The radius of a circle is 30 meters.
        Calculate the area of a circle and assign the value to a variable name of area_of_circle
        Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
        Take radius as user input and calculate the area.
    Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
    Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
