response = []


class MultiplesAndFactors:
    def find_multiples(self):
        try:
            global response, rt, factor
            factor = int(input("Type a factor to find it's multiples: "))
            rt = int(input("Type a R.T. to stop finding multiples at: "))
            for numbers in range(1, rt + 1):
                multiples = factor * numbers
                response.append(multiples)
            print(f' Multiples of {factor} are: {response}')
        except ValueError:
            print("Did you type a number?")

    def find_factors(self):
        global response
        try:
            multiple = int(input("Type a multiple to find it's factors: "))
            for rt in range(1, multiple + 1):
                factors = multiple / rt
                if factors not in response and multiple % rt == 0:  # Figure out how this gets rid of floats.
                    response.append(factors)
            print(f'Factors of {multiple} are: {response}')
        except ValueError:
            print("Did you type a number?")

    def multiples_factors_options(self):
        choice = input("""
        Choose an option and respond with the number corresponding to the option:
            1. Find multiples of a factor
            2. Find factors of a multiples
            3. Find common factors of a multiple (Work In Progress)
            4. Find common multiples of a factor (Work In Progress)
        Answer here: 
        """)
        if "1" in choice.split(" "):
            factors_and_multiples.find_multiples()
        elif "2" in choice.split(" "):
            factors_and_multiples.find_factors()
        else:
            print("That may be a work in progress or you did not type a proper response ")


while True:
    factors_and_multiples = MultiplesAndFactors()
    factors_and_multiples.multiples_factors_options()
    response.clear()
    run_status = input("Would you like to quit, [Y] or [N]: ")
    run_status.split(" ")
    if run_status.upper() == "Y":
        break