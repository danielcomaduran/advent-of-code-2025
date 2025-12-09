#%% Import data
with open("example.txt") as file:
    boxes_positions = file.read().split("\n")

boxes_int_positions = [[int(number) for number in numbers.split(",")] for numbers in boxes_positions]

#%% Functions
def compute_distance(box1: list, box2: list) -> int:
    distance = ((box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2) ** 0.5
    return distance

def connect_boxes(boxes_position: list, n_connections: int) -> int:
    distances = []

    # Compute distances
    for b1, box1 in enumerate(boxes_position):
        for b2, box2 in enumerate(boxes_position):
            if box1 != box2:
                distances.append(((b1, b2), compute_distance(box1, box2)))
    
    # Sort distances
    distances = sorted(distances, key=lambda x: x[1])

    # Create connections
    connections = []
    for i in range(n_connections):
        
        connections.append(distances[i])
    
    return distances
#%% Part 1
distances = connect_boxes(boxes_int_positions, n_connections=2)


# %%
