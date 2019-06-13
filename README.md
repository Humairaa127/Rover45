# Rover45


<h2>Problem</h2>
A squad of robotic rovers are to be landed by NASA on a plateau on Mars.

This plateau, which is curiously rectangular, must be navigated by the rovers so that their on board cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover's position is represented by a combination of an x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot.

'M' means move forward one grid point, and maintain the same heading.

** Source: https://code.google.com/archive/p/marsrovertechchallenge/

<h2>Assumptions</h2>
- NASA knows that coordinates must be input with a space between each\n
- Cardinal headings will be input in uppercase\n
- Rovers move one at a time, sequentially\n
- All instructions will be sent in one input string\n

<h2>Program Use</h2>
Run venv/MarsRover.py. \n

Three inputs are required:\n
  First input prompt requires top right coordinates of terrain grid.\n
Thereafter, two inputs for each rover:\n
Input a) Intial location of rover in the form X Y H (e.g 3 4 N)\n
Input b) A list of instructions from the commands L, R, M (e.g. LMMRMLMM)
