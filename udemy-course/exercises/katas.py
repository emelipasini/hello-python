def make_negative(number):
    if number <= 0:
        return number
    return -number

    # return -abs(number)

print(make_negative(25))
print(make_negative(0))
print(make_negative(-9))


def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - son_years_old * 2)

print(twice_as_old(36, 7))
print(twice_as_old(55, 30))
print(twice_as_old(42, 21))


def string_to_array(s):
    return s.split(" ")

print(string_to_array("Robin Singh"))
print(string_to_array("CodeWars"))
print(string_to_array("I love arrays they are my favorite"))
string_to_array("1 2 3")
string_to_array("")


def close_compare(a, b, margin=0):
    distance = abs(a - b)
    if distance <= margin:
        return 0
    return -1 if a < b else 1

print(close_compare(4, 5))
print(close_compare(5, 5))
print(close_compare(6, 5))
print(close_compare(-6, -5))
print(close_compare(2, 5, 3))
print(close_compare(8.1, 5, 3))
print(close_compare(1.99, 5, 3))
print(close_compare(5, 5, 3))
print(close_compare(3, 5, 3))
print(close_compare(4, 5, 0))
print(close_compare(5, 5, 0))
print(close_compare(6, 5, 0))
