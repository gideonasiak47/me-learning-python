
# String data type

# literal assignment
first = "James"
last = "Bond"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Pepperoni")
# print(type(pizza)) 
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatentation
# fullname = first + " " + last
# print(fullname)
# fullname += " Jr."

# year = str(1980)
# print(fullname + " " + year)
# statement = "I like rock music from the " + year + "s."
# print(statement)

# # multiple lines
multiline = """
Hey, how are you?                    
I was just checking in.
                                          All good?


"""

# print(multiline)

# sentence = 'I\'m sorry!\tHey\n\nWhere\'s this at\\located?'
# print(sentence)


# string methods (functions called on the string object)

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                                  "
multiline = "                                 "+ multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")
# string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# some methods that return boolean values
print(first.startswith("J"))
print(first.endswith("k"))

# Boolean data type
value = False
x = bool(False)
print(type(x))
print(isinstance(x, bool))

# numeric data types

# integer
price = 100
best_price = int(99)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.55539
y = float(10.32)
print(type(y))

# complex
comp_value = 3+6j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)


# Built-in functions for numeric types
print(abs(gpa * -1))
print(round(gpa, 2))

import math
print("")
print(math.pi)
print(math.sqrt(32))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10010"
zip_value = int(zipcode)
print(type(zip_value))


# Error if you attempt to cast incorect data(eg non-numetic
# zip_value = int("New York")


