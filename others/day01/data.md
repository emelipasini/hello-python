# Day 1

Python is a high level programming language for general-purpose programming.
It is an open source, interpreted, object-oriented programming language.

Python uses indentation to create blocks of code.
One common bug when writing python is wrong indentation.

## Data Types

- Numbers
    - int -5, 0, 3
    - float -3.1, 0.0, 5.4
    - complex 2 + 4j
- Strings
    - "Hello world"
    - 'Hello Python'
- Boolean
    - True
    - False
- List: is an ordered collection which allows to store different data type items, is similar to an array in JS.
    - [0, 1, -3]
    - ["Hello", "World"]
    - ["Hello", 2, True]
- Dictionary: is an unordered collection of data in a key value pair format.
    - {
        "firstname": "Name",
        "age": 20,
        "is_married": True,
        "skills": ["JS", "Node", "Python"]
      }
- Tuple: is an ordered collection of different data types like list but tuples can not be modified once they are created.
    - ("Hello", 36, False)
- Set: is a collection of data types similar to list and tuple but unordered and stores only unique items.
    - { 2, 4, 3, 5 }
    - { 3.14, 9.81, 2.7 }

## Useful info

To check the data type of a certain data/variable, we use the **type** function.
```py
type("Hello world")
```

To print a value, we use the **print** function
```py
print("Hello Python")
```

To comment one line, start it with # signal
```py
# This is a one line comment
```

To comment multiple lines, they have to be between 3 quotes
```py
"""
    This is a
    multiple lines
    comment
"""
```

## Exercises

### Exercise: Level 1

    Check the python version you are using
    Open the python interactive shell and do the following operations. The operands are 3 and 4.
        addition(+)
        subtraction(-)
        multiplication(*)
        modulus(%)
        division(/)
        exponential(**)
        floor division operator(//)
    Write strings on the python interactive shell. The strings are the following:
        Your name
        Your family name
        Your country
        I am enjoying 30 days of python
    Check the data types of the following data:
        10
        9.8
        3.14
        4 - 4j
        ['Asabeneh', 'Python', 'Finland']
        Your name
        Your family name
        Your country

### Exercise: Level 2

    Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

### Exercise: Level 3

    Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
    Find an Euclidian distance between (2, 3) and (10, 8)
