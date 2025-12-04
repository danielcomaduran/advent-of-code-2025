#%% Import file
with open("input.txt") as file:
    grid = file.read()

grid_list = grid.split("\n")

#%% Functions
def find_n_adjactent(grid: list, symbol: str, n_adjacent: int, return_index: bool = False) -> int:
    n_rows = len(grid)
    rolls_count = 0
    rolls_indices = []

    for l, line in enumerate(grid):
        n_cols = len(line)
        
        for c, char in enumerate(line):
            if char == symbol:
                count_adjacent = 0
                
                min_col = max(0, c - 1)
                max_col = min(n_cols, c + 2)
                min_row = max(0, l - 1)
                max_row = min(n_rows, l + 2)
                
                count_adjacent = sum(1 for row in grid[min_row:max_row] for adj_char in row[min_col:max_col] if adj_char == symbol)

                # Needs to be <= to exclude itself
                if count_adjacent <= n_adjacent:
                    # print(f"Roll at line {l}, column {c} has {count_adjacent} adjacent rolls.")
                    rolls_indices.append((l, c))
                    rolls_count += 1

    if return_index:
        output = rolls_count, rolls_indices
    else:
        output = rolls_count

    return output

def remove_rolls(grid: list, rolls_indices: list) -> list:
    for roll_index in rolls_indices:
        l, c = roll_index
        grid[l] = grid[l][:c] + "." + grid[l][c+1:]

    return grid

#%% Part 1: Count number of rolls with less than 4 adjacent rolls
n_rolls_part1 = find_n_adjactent(grid_list, "@", 4)
print(f"Part 1: Number of rolls with less than 4 adjacent rolls: {n_rolls_part1}")

#%% Part 2: Iteratively, remove as many rolls as possible with less than 4 adjacent rolls
count_removed_rolls, removed_rolls_indices = find_n_adjactent(grid_list, "@", 4, return_index=True)
new_grid_list = remove_rolls(grid_list, removed_rolls_indices)

while len(removed_rolls_indices) > 0:
    count_new_removed_rolls, removed_rolls_indices = find_n_adjactent(new_grid_list, "@", 4, return_index=True)
    count_removed_rolls += count_new_removed_rolls
    new_grid_list = remove_rolls(new_grid_list, removed_rolls_indices)

print(f"Part 2: Total number of removed rolls: {count_removed_rolls}")