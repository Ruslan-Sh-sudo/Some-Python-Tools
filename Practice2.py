import random

# Generator function

turn = ["Alex", "Ruslan", "Vadim"]


def cleaning():
    while True:
        m = random.choice(turn)
        yield m


# This generator decides randomly who will clean the room in my dormitory

turn_gen = cleaning()
for _ in range(7):
    print(next(turn_gen))  # Here we can define the weekly cleaning schedule

print("_______")

turn = ["Jadon", "Martin", "Vadim"]
for _ in range(7):
    print(next(turn_gen))  # If residents change, we will remember all past schedule

print("_______")


# Decorator function

def html_doctype(myfunc):
    def inner(*args, **kwargs):
        print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>''')
        myfunc(*args, **kwargs)
        print('''</body>
</html>''')

    return inner()


@html_doctype  # This decorator frames the input of the function into html DOCTYPE standard
def body_html():
    print("Something that body contains...")


print("_______")

# Iterator

my_nums = [1, 2, 5, 75, 34, 86, 32, 75, 98, 33, 55, 77, 12]
even_nums = []

for i in my_nums:
    if i % 2 == 0:
        even_nums.append(i)

iterator = iter(even_nums)
try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("Too many iterations!")
    print(even_nums)
    print("Here is a complete list of even numbers")


# Context manager

class MyFile:
    def __init__(self, file_name, method):
        self.file_object = open(file_name, method)

    def __enter__(self):
        return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_object.close()


# Created context manager that allows me to open, edit & close file

"""
with MyFile('SomeName.SomeFormat', 'SomeMethod') as f:
    f.write('blablabla')
"""
