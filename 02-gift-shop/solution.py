#%% Import file
with open("input.txt") as file:
    raw_ids = file.read()

#%% Organize input
range_ids = raw_ids.split(",")

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