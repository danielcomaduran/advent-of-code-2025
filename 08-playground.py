#%% Import data
with open("example.txt") as file:
    boxes_positions = file.read().split("\n")

boxes_int_positions = [[int(number) for number in numbers.split(",")] for numbers in boxes_positions]

#%% Functions
def compute_distance(box1: list, box2: list) -> int:
    distance = (box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2
    return distance

def connect_boxes(boxes_position: list, n_connections: int) -> int:
    distances = []

    # Compute distances
    for b1, box1 in enumerate(boxes_position):
        for b2, box2 in enumerate(boxes_position[b1+1:], start=b1+1):
            distances.append(((b1, b2), compute_distance(box1, box2)))
    
    # Sort distances
    distances = sorted(distances, key=lambda x: x[1])

    # Create connections
    connections = []
    i = 0 # Counter for current number of connections
    while i < n_connections and i < len(distances):
        box_pair = distances[i][0]

        # Check if box_id exist in any sublist
        box1_found = False
        box2_found = False 
        for sublist in connections:
            if box_pair[0] in sublist:
                box1_found = True
                for sublist2 in connections:
                    if sublist2 != sublist and box_pair[1] in sublist2:
                        box2_found = True
                        break

            elif box_pair[1] in sublist:
                box2_found = True
                for sublist2 in connections:
                    if sublist2 != sublist and box_pair[0] in sublist2:
                        box1_found = True
                        break

        # Add connections appropriately
        if box1_found and box2_found:
            pass
        elif box1_found and not box2_found:
            sublist.append(box_pair[1])
        elif box2_found and not box1_found:
            sublist.append(box_pair[0])
        else:
            connections.append([box_pair[0], box_pair[1]])

        i += 1
        
    return distances
#%% Part 1
distances = connect_boxes(boxes_int_positions, n_connections=10)


# %%
