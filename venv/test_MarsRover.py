import MarsRover


def test_normal_input():
    result = str(MarsRover.calculatedestination('5 5','3 3 E', 'MMRMMRMRRM'))
    assert (result == "Final location is:  5 1 E")


def test_positive_boundary():
    result = str(MarsRover.calculatedestination('5 5','3 3 N', 'MMMMRMRRM'))
    assert (result == "Destination out of bounds. You collided with a Martian!")
    
def test_instruction_length():
    result = str(MarsRover.calculatedestination('5 5','0 0 N', 'MMMMMRMRMMMMMLMLMMMMM'))
    assert (result == "Final location is:  2 5 N")
    
def test_grid_size():
    result = str(MarsRover.calculatedestination('10 5','0 0 N', 'MMMMMRMRMMMMMLMLMMMMM'))
    assert (result == "Final location is:  2 5 N")


test_normal_input()
test_positive_boundary()
test_instruction_length()
test_grid_size()
