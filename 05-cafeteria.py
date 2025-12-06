#%% Import file
with open("input.txt") as file:
    ingredients = file.read().strip().split("\n\n")

fresh = ingredients[0].split("\n")
available = ingredients[1].split("\n")

#%% Part 1: Count number of fresh ingredients that can be made with available ingredients
count_fresh_ingredients = 0

for ingredient in available:
    current_ingredient = int(ingredient)

    for fresh_ingredient in fresh:
        frest_start = int(fresh_ingredient.split("-")[0])
        fresh_end = int(fresh_ingredient.split("-")[1])

        if (current_ingredient >= frest_start) and (current_ingredient <= fresh_end):
            count_fresh_ingredients += 1
            break

print(f"Part 1: Number of fresh ingredients that can be made: {count_fresh_ingredients}")


# %% Part 2: Find the unique fresh ingredients from the fresh list
# Get complete overlapping ranges
ranges = []
for fresh_range in fresh:
    fresh_start = int(fresh_range.split("-")[0])
    fresh_end = int(fresh_range.split("-")[1])
    ranges.append([fresh_start, fresh_end])

ranges.sort()

# Merge overlapping ranges
merged = []
for start, end in ranges:
    # Merge overlapping or adjacent ranges
    if merged and start <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], end)
    # Append non-overlapping ranges
    else:
        merged.append([start, end])

# Count total unique ingredients
total_count = sum(end - start + 1 for start, end in merged)
print(f"Part 2: Total unique fresh ingredients available: {total_count}")