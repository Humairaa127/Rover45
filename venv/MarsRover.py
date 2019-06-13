def getgridsize():
    global grid_size
    grid_size = str(input("Enter the upper right coordinates of the terrain in the form X Y (e.g 3 4): "))
    return grid_size

def getinstruction():
    global initial_location
    initial_location = str(input("Enter the initial location coordinates and heading of the rover in the form X Y H (e.g 1 3 S): "))
    # Split instruction
    global instructions

    instructions = str(input("Enter the list of instructions from the commands L, R, M (e.g. LMMRMLMM): "))
    return initial_location, instructions

def calculatedestination(grid_size, initial_location, instructions):
    # Split current location into a list
    current_location = list(initial_location)

    # Split instruction string into a list
    instruction_list = list(instructions)

    grid = list(grid_size)

    # For each instruction in instruction_list, determine new location after instruction is fulfilled.
    # Loops through each instruction in instruction_list, independent of list length
    for i in range(0, len(instruction_list)):
        instruction = instruction_list[i]

        # Create a list of cardinal headings.
        cardinal = ['N', 'E', 'S', 'W']
        # (L) Left instruction results in anticlockwise rotation between cardinal headings.
        if instruction == 'L':
            if current_location[4] == 'N':
                current_location[4] = 'W'
            else:
                current_location[4] = cardinal[cardinal.index(current_location[4]) - 1]
        # (R) Right instruction results in clockwise rotation between cardinal headings.
        elif instruction == 'R':
            if current_location[4] == 'W':
                current_location[4] = 'N'
            else:
                current_location[4] = cardinal[cardinal.index(current_location[4]) + 1]
        # (M) Move instruction results in:
        #   - Positive X translation if heading is E
        #   - Negative X translation if heading is W
        #   - Positive Y translation if heading is N
        #   - Negative Y translation if heading is S
        else:
            if current_location[4] == 'N' or current_location[4] == 'S':
                direction_index = 2
            else:
                direction_index = 0

            if current_location[4] == 'N' or current_location[4] == 'E':
                current_location[direction_index] = str(int(current_location[direction_index]) + 1)
                # Check if destination is within bounds
                if int(current_location[direction_index]) > int(grid[direction_index]) or int(current_location[direction_index]) < 0:
                    print("Destination out of bounds. You collided with a Martian!")
                    break

            else:
                current_location[direction_index] = str(int(current_location[direction_index]) - 1)
                # Check if destination is within bounds
                if int(current_location[direction_index]) > int(grid[direction_index]) or int(current_location[direction_index]) < 0:
                    print("Destination out of bounds. You collided with a Martian!")
                    break

    print('Final location is: ', (''.join(current_location)))

# ___________________________________________________________________________________________________________________________________
# This program calculates the final position of a rover after completing the given instructions.
# Initialise program
# ___________________________________________________________________________________________________________________________________


getgridsize()
repeat = 'y'

while repeat in ['Y', 'y', 'yes']:

    getinstruction()

    calculatedestination(grid_size, initial_location, instructions)

    repeat = input("Would you like to start the next rover? Y/N : ")


