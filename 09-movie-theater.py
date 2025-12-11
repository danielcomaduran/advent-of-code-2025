#%% Import data
with open("input.txt") as file:
    corner_positions = file.read().strip().split("\n")

corner_int_positions = [[int(number) for number in numbers.split(",")] for numbers in corner_positions if numbers.strip()]
# %% Part 1: Get biggest possible area
def largest_area(corners_positions: list) -> int:
    max_area = -1
    max_points = (None, None)

    for p1, point1 in enumerate(corners_positions):
        for p2, point2 in enumerate(corners_positions[p1+1:], start=p1+1):
            x = abs(point1[0] - point2[0]) + 1
            y = abs(point1[1] - point2[1]) + 1
            area = x * y

            if area > max_area:
                max_area = area
                max_points = (point1, point2)
    print(f"Points {max_points[0]} and {max_points[1]} give area {max_area}")

    return max_area


max_area = largest_area(corner_int_positions)
print(f"Part 1: max area is {max_area}")

# %%Part 2: Largest rectangle within corners
def largest_rectangle(corners_positions: list) -> int:
    c = [tuple(p) for p in corners_positions]
    n = len(c)
    
    # Calculate area between two corners
    def area(p1, p2):
        return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
    
    # Create edges between consecutive corners
    edges = []
    for i in range(n):
        p1 = c[i]
        p2 = c[(i + 1) % n]
        edges.append((min(p1, p2), max(p1, p2)))
    
    # Try all rectangle pairs, largest first
    rectangles = [(area(c[i], c[j]), c[i], c[j]) for i in range(n) for j in range(i + 1, n)]
    rectangles.sort(reverse=True)
    
    for rect_area, p1, p2 in rectangles:
        x1, x2 = sorted([p1[0], p2[0]])
        y1, y2 = sorted([p1[1], p2[1]])
        
        # Check if any edge cuts through rectangle interior
        cuts_through = False
        for (x3, y3), (x4, y4) in edges:
            # Edge cuts through if it overlaps the interior
            if x4 > x1 and x3 < x2 and y4 > y1 and y3 < y2:
                cuts_through = True
                break
        
        if not cuts_through:
            print(f"Rectangle area {rect_area}")
            return rect_area
    
    return 0
max_rectangle_area = largest_rectangle(corner_int_positions)
print(f"Part 2: max rectangle area is {max_rectangle_area}")
# %%
