#%% Import file
with open("input.txt") as file:
    batteries = file.read()

batteries_list = batteries.split("\n")

#%% Functions
def get_highest_joltage(joltage: str) -> int:
    joltage_digits = [int(c) for c in joltage]

    first_digit = 0
    first_digit_index = 0
    second_digit = 0

    # Get first highest digit
    for d, digit in enumerate(joltage_digits[:-1]):
        if digit > first_digit:
            first_digit = digit
            first_digit_index = d

    # Get second highest digit
    for d, digit in enumerate(joltage_digits[first_digit_index+1:]):
        if digit > second_digit:
            second_digit = digit

    output = 10*first_digit + second_digit

    return output

def get_highest_joltage_extended(joltage: str, n_digits: int) -> int:
    joltage_digits = [int(c) for c in joltage]
    max_n_digits = len(joltage_digits)

    highest_joltage = []
    d = 0

    while (len(highest_joltage) < n_digits) and (d < max_n_digits):
        # Calculate how far to look ahead
        remaining_needed = n_digits - len(highest_joltage)
        search_end = max_n_digits - remaining_needed + 1
        
        # Find highest digit in the allowed range
        highest_digit = 0
        highest_digit_index = d

        for current_digit in range(d, min(search_end, max_n_digits)):
            if joltage_digits[current_digit] > highest_digit:
                highest_digit = joltage_digits[current_digit]
                highest_digit_index = current_digit

        highest_joltage.append(highest_digit)
        d = highest_digit_index + 1 # Start search after the chosen digit

    output = int("".join(map(str, highest_joltage)))

    return output
    
#%% Part 1: Calculate highest joltage using 2 digits
highest_joltage = []
for battery in batteries_list:
    highest_joltage.append(get_highest_joltage(battery))

summed_joltage = sum(highest_joltage)
print(f"The sum of all highest joltage ratings is: {summed_joltage}")

# %% Part 2: Find the highest joltage using 12 digits
highest_joltage_extended = []
for battery in batteries_list:
    highest_joltage_extended.append(get_highest_joltage_extended(battery, 12))

summed_joltage_extended = sum(highest_joltage_extended)
print(f"The sum of all highest extended joltage ratings is: {summed_joltage_extended}")