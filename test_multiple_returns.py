def calculate():
    name = "Paul"
    age = 23
    return name, age


def use_values():
    name, age = calculate()
    print(name, age)

use_values()