def is_valid_walk(walk):
    # Check if the walk takes exactly 10 minutes
    if len(walk) != 10:
        return False
    
    # Track the net movement in each direction
    north_south = 0
    east_west = 0
    
    # Iterate through the directions
    for direction in walk:
        if direction == 'n':
            north_south += 1
        elif direction == 's':
            north_south -= 1
        elif direction == 'e':
            east_west += 1
        elif direction == 'w':
            east_west -= 1
    
    # Check if the net movement returns to the starting point
    return north_south == 0 and east_west == 0

# Examples
print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # Output: True
print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))  # Output: True
print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # Output: False
print(is_valid_walk(['n', 's']))                                          # Output: False
