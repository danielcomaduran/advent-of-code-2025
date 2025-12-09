#%% Import data
with open("input.txt") as file:
    manifold = file.read()

manifold_lines = manifold.split("\n")

#%% Functions
def count_splits(manifold_lines: list, count_timelines:bool = False) -> int:
    beam_splits = 0
    beams = [0] * len(manifold_lines[0])

    # Find start point
    start_point = manifold_lines[0].index("S")
    beams[start_point] = 1
    timeline_count = 1

    for line in manifold_lines[1:]:
        for c in range(len(beams)):
            if beams[c] > 0 and line[c] == "^":
                beam_splits += 1
                timeline_count += beams[c]
                beams[c-1] += beams[c]
                beams[c+1] += beams[c]
                beams[c] = 0

    if count_timelines:
        return timeline_count
    else:
        return beam_splits

#%% Part 1: Count beam splits
beam_splits = count_splits(manifold_lines)
print(f"Part 1: Total beam splits: {beam_splits}")

#%% Part 2: Count total combinations
total_combinations = count_splits(manifold_lines, count_timelines=True)
print(f"Part 2: Total combinations: {total_combinations}")