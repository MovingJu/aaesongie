def add(a, b): return a + b
def sub(a, b): return a - b

calc_dict = {
    "Add": add,
    "Sub": sub
}

print(calc_dict["Add"](41, 3))
print(add(41, 3))