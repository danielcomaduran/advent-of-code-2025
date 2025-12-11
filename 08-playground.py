#%% Import data
with open("input.txt") as file:
    boxes_positions = file.read().split("\n")

boxes_int_positions = [[int(number) for number in numbers.split(",")] for numbers in boxes_positions]

#%% Functions
def compute_distance(box1: list, box2: list) -> int:
    distance = (box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2
    return distance

def get_all_distances(boxes_position: list) -> list[tuple[tuple[int, int], int]]:
    distances = []
    for b1, box1 in enumerate(boxes_position):
        for b2, box2 in enumerate(boxes_position[b1+1:], start=b1+1):
            distances.append(((b1, b2), compute_distance(box1, box2)))

    distances.sort(key=lambda x: x[1])

    return distances

def connect_boxes(boxes_position: list, n_connections: int) -> list[list[int]]:
    # Get all distances
    distances = get_all_distances(boxes_position)

    # Create connections
    connections = []
    i = 0 # Counter for current number of connections
    while i < n_connections and i < len(distances):
        box1, box2 = distances[i][0]

        # Find existing sublists (if any) for each box
        sublist1 = None
        sublist2 = None
        for sublist in connections:
            if box1 in sublist:
                sublist1 = sublist
            if box2 in sublist:
                sublist2 = sublist
            if sublist1 and sublist2:
                break

        # Add or merge according to what was found
        if sublist1 and sublist2:
            if sublist1 is not sublist2:
                # Merge the two groups so the connection counts
                sublist1.extend(x for x in sublist2 if x not in sublist1)
                connections.remove(sublist2)
            # else already in same group; skip
        elif sublist1:
            sublist1.append(box2)
        elif sublist2:
            sublist2.append(box1)
        else:
            connections.append([box1, box2])

        i += 1
    
    connections.sort(key=len, reverse=True)
    return connections
#%% Part 1
connections = connect_boxes(boxes_int_positions, n_connections=1000)
multiplication = 1
for group in connections[:3]:
    multiplication *= len(group)
print(f"Part 1 result: {multiplication}")

# %% Part 2
