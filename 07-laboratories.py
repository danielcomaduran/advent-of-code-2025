#%% Import data
with open("example.txt") as file:
    manifold = file.read()

manifold_lines = manifold.split("\n")

#%% Functions
def count_splits(manifold_lines: list, count_timelines:bool = False) -> int:
    beam_splits = 0
    current_beams = []
    combinations = 0
    for l, line in enumerate(manifold_lines):
        # Detect start of beam
        if l == 0:
            for c, char in enumerate(line):
                if char == "S":
                    current_beams.append(c)
                    break

        # Detect beam splits and ends
        else:
            row_splits = 0
            new_beams = []

            for b, beam in enumerate(current_beams):
                if line[beam] == "^": # Beam splits
                    row_splits += 1
                    new_beams.extend([beam-1, beam+1])
                else: # Beam continues
                    new_beams.append(beam)
                    
            current_beams = list(set(new_beams))  # Remove duplicates
            
            if row_splits > 0:
                beam_splits += row_splits 
            combinations += len(current_beams)

    if count_timelines:
        return combinations + len(current_beams) - 1 # Add remaining beams at the end
    else:
        return beam_splits

#%% Part 1: Count beam splits
beam_splits = count_splits(manifold_lines)
print(f"Part 1: Total beam splits: {beam_splits}")

#%% Part 2: Count total combinations
total_combinations = count_splits(manifold_lines, count_timelines=True)
print(f"Part 2: Total combinations: {total_combinations}")

# %%