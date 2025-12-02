#%% Import file
with open("input.txt") as file:
    raw_ids = file.read()

range_ids = raw_ids.split(",")

#%% Part 1: Identify repeated patterns
invalid_ids = []
for id in range_ids:
    split_ids = id.split("-")
    start = int(split_ids[0])
    end = int(split_ids[1])
        
    for number in range(start, end + 1):
        number_split = len(str(number)) // 2
        str_number = str(number)
        if str_number[0:number_split] == str_number[number_split:]:
            invalid_ids.append(number)

summed_invalid_ids = sum(invalid_ids)
print(f"The sum of all invalid gift shop IDs is: {summed_invalid_ids}")

#%% Part 2: Identify repeated digits sequences
invalid_ids_p2 = []
for id in range_ids:
    split_ids = id.split("-")
    start = int(split_ids[0])
    end = int(split_ids[1])
        
    for number in range(start, end + 1):
        max_number_split = len(str(number)) // 2

        
        for split in range(1, max_number_split + 1):
            if len(str(number)) % split != 0:
                continue  # Skip if the number length is not divisible by the split size

            invalid_count = 0
            str_number = str(number)
            
            for i in range(0, len(str_number) - 2*split + 1, split):
                if (str_number[i] != "0") or (str_number[i+split] != "0"):
                    if str_number[i:i+split] == str_number[i+split:i+2*split]:
                        invalid_count += 1

                        # Additional check for the case where the repeated sequence is exactly half the number
                        if (len(str_number) % 2 == 0) and (split == len(str_number) // 2):
                            invalid_count += 1
                    else:
                        invalid_count = 0
                        break  # Exit the innermost loop if the sequence is broken
            
            if invalid_count > 1:
                invalid_ids_p2.append(number)
                # print(f"Number {number} is invalid {invalid_count} times for split size {split}.")
                break  # Exit the outer loop if already invalid at least twice


summed_invalid_ids_p2 = sum(invalid_ids_p2)
print(f"The sum of all invalid gift shop IDs for part 2 is: {summed_invalid_ids_p2}")