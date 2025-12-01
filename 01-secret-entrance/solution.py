#%% Load data
with open("input.txt") as file:
    movements = file.read().splitlines()

#%% Decoder
def decoder(starting_position, movements, count_passes=False):
    '''
    Decode the knob movements. 
    If count_passes is True, also count the number of times passing 0.
    '''

    knob_number = starting_position
    rotations = []
    passes = 0

    for line in movements:
        operation = line[0]
        number = int(line[1:])
        
        for _ in range(number):
            if operation == "R":
                knob_number = (knob_number + 1) % 100
            elif operation == "L":
                knob_number = (knob_number - 1) % 100

            if knob_number == 0:
                passes += 1
        
        # Adjust for landing on 0, not passing it
        if knob_number == 0:
            passes -= 1  

        rotations.append(knob_number)

    zero_count = sum(1 for num in rotations if num == 0)
    output = zero_count if not count_passes else (zero_count + passes)

    return output
#%% Part 1: Decode the secret entrance
# Count the number of 0's in the rotations
knob_number = 50    # Starting position
password = decoder(knob_number, movements)
print(f"The password for the secret entrance is: {password}")

# %% Part 2: Additional decoding
# Count the number of 0's and the number of times passing 0
knob_number = 50    # Starting position
password_extended = decoder(knob_number, movements, count_passes=True)
print(f"The extended password for the secret entrance is: {password_extended}")


