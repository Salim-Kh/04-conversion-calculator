# Time
Time_dict = {
    "ms" : 3600*1000,
    "sec":3600,
    "min":60,
    "h": 1,
    "d": 1/24,
    "y": 1 /(24 * 365 + 6 + 6 + 9/60)

}

# Get amount and units (assume they are valid)
amount = float(input("how much? "))
from_unit = input("from Unit? ")
To_Unit = input("To Unit? ")

# Multiply to get to our standard value...
multiply_by = Time_dict[To_Unit]
standard = amount * multiply_by

# Divide to get to our desired value
divide_by = Time_dict[from_unit]
answer = standard / divide_by

print(f"There are {answer: .2f} {To_Unit} in {amount} {from_unit} " )