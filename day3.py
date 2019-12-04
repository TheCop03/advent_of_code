
# Read the directions of the two wires from the text file
with open('day3_data.txt') as file:
    first_wire = file.readline().split(',')
    second_wire = file.readline().split(',')

# first_wire = ['R8','U5','L5','D3']
# second_wire = ['U7','R6','D4','L4']

def common_points(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return a_set & b_set
    else:
        print("No common elements")

def convert_to_xy(direction_list):
    # Position List
    xy_pos = []
    x, y = 0, 0

    for direction in direction_list:
        # Add to Y if going up
        if direction[0] == 'U':
            xy_pos.extend((x, y + len) for len in range(1, int(direction[1:]) + 1))
            y += int(direction[1:])
        # Add to X if going right
        elif direction[0] == 'R':
            xy_pos.extend((x + len, y) for len in range(1, int(direction[1:]) + 1))
            x += int(direction[1:])
        # Subtract from X if going left
        elif direction[0] == 'L':
            xy_pos.extend((x - len, y) for len in range(1, int(direction[1:]) + 1))
            x -= int(direction[1:])
        # Subtract from Y if going down
        elif direction[0] == 'D':
            xy_pos.extend((x, y - len) for len in range(1, int(direction[1:]) + 1))
            y -= int(direction[1:])

    return xy_pos

# Convert the directions to xy positions on the grid and remove (0, 0) positions
first_pos = convert_to_xy(first_wire)
second_pos = convert_to_xy(second_wire)

intersections = common_points(first_pos, second_pos)

# Check where the two wires intersect closest to the central point (0, 0)
closest_intersection = 1000000000000000000000000000
lowest_steps = 1000000000000000000000000000

for point in intersections:
    if ((abs(point[0]) + abs(point[1])) < closest_intersection):
        closest_intersection = abs(point[0]) + abs(point[1])
    if ((first_pos.index(point) + second_pos.index(point) + 2) < lowest_steps):
        lowest_steps = first_pos.index(point) + second_pos.index(point) + 2

print(closest_intersection)
print(lowest_steps)
