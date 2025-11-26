# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration}")


# Display instructions
def instructions():
    statement_generator("instructions", "-")
    print('''
instruction go here. 
To use this program simply enter a number you want to convert. 
The program will show you the conversion of your chosen number. 
    ''')


# Ask user for width snf loop until they
# Enter a number that is more than zero
def num_check(question):

        error = "Please enter a number that is more than zero\n"
        while True:


            try:
                # ask the user for a number
                    response = float(input(question))

                # check that the number is more than zero

                    if response >0:
                       return response
                    else:
                        print(error)


            except ValueError :
                print(error)

# Main routine
# Heading
statement_generator("The ultimate conversion calculator", "*")

# Display instructions if user has not used the program before
want_instructions = input("press<enter> to read the instructions or any key to continue")

if want_instructions == "":
    instructions()

# Find the domain
valid_type ={"distance", "mass", "time"}

# Set up (initialise) the dictionaries
time_dict = {
            "ms": 3600 * 1000,
            "s": 3600,
            "min": 60,
            "h": 1,
            "d": 1 / 24,
            "month": 1 / 168,
            "y": 1 / (24 * 365 + 6 + 9 / 60)  # it accounts for leap years
        }

distance_dict = {
    "mm": 1000000,
    "cm": 100,
    "m": 1,
    "km": .001
}
mass_dict = {
    "mg": 1000000,
    "gr": 1000,
    "kg": 1,
    "t": .001
}
while True:
    calc_type = input("calc_type: ").strip().lower()
    if calc_type == "xxx":
        print("Thank you for using conversion calculator!!!^-^")
        break
    if calc_type not in valid_type:
        print("Please enter a valid calculation type.")
        continue
    # get amount and units
    amount = float(num_check("how much? "))
    from_unit = input("From Unit? ")
    to_unit = input("To Unit? ")


    if calc_type == "time":
       dictionary = time_dict

    elif calc_type == "distance":
        dictionary =distance_dict
    else:
        dictionary = mass_dict

    # multiply to get to our standard value...
    multiply_by = dictionary[to_unit]
    standard = amount * multiply_by

    # Divide to get to our desired value
    divide_by = dictionary[from_unit]
    answer = standard / divide_by
    print(f"There are {answer} {to_unit} in {amount} {from_unit} ")


















