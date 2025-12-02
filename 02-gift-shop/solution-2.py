#%% Import file
with open("input.txt") as file:
    raw_ids = file.read()

range_ids = raw_ids.split(",")

#%% Function to count repeating patterns in a string
def count_patterns(s) -> int:
    
    max_pattern = 0
    for split in range(1, len(s) // 2 + 1):
        # Skip if the number length is not divisible by the pattern size
        if len(s) % split != 0:
            continue

        max_repeats = len(s) // split
        pattern = s[0:split] * max_repeats

        if pattern == s:
            max_pattern = max_repeats

    return max_pattern

#%% Part 1: Identify patterns that repeat exactly twice
invalid_ids = []
for id in range_ids:
    split_ids = id.split("-")
    start = int(split_ids[0])
    end = int(split_ids[1])
        
    for number in range(start, end + 1):
        str_number = str(number)
        
        if count_patterns(str_number) == 2:
            invalid_ids.append(number)

summed_invalid_ids = sum(invalid_ids)
print(f"The sum of all invalid gift shop IDs is: {summed_invalid_ids}")

#%% Part 2: Identify patterns that repeat more than twice
invalid_ids = []
for id in range_ids:
    split_ids = id.split("-")
    start = int(split_ids[0])
    end = int(split_ids[1])
        
    for number in range(start, end + 1):
        str_number = str(number)
        
        if count_patterns(str_number) >= 2:
            invalid_ids.append(number)

summed_invalid_ids = sum(invalid_ids)
print(f"The sum of all invalid gift shop IDs is: {summed_invalid_ids}")