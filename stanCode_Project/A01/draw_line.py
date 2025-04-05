"""
File: 
Name:Alina
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constants for the circle size
SIZE = 20

# Create an instance of the GWindow class
window = GWindow()

# Variable to store the coordinates of the first click
first_click = None
# Use a fixed-size list for storing a single circle
holes = [None]


def main():
    """
    This program creates lines on an instance of the GWindow class.
    The first click draws a circle. On the second click, a line is drawn
    connecting the two clicks, and the circle is removed.
    """
    onmouseclicked(create_hole)


def create_hole(mouse):
    global first_click
    if first_click is None:
        # First click: create and display a circle
        hole = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        hole.filled = True
        hole.fill_color = 'white'
        window.add(hole)
        holes[0] = hole  # Store the hole at index 0
        first_click = (mouse.x, mouse.y)
    else:
        # Second click: draw a line and remove the circle
        line = GLine(first_click[0], first_click[1], mouse.x, mouse.y)
        window.add(line)
        first_click = None  # Reset the first click
        if holes[0] is not None:
            window.remove(holes[0])  # Remove the circle
            holes[0] = None  # Reset the circle storage


if __name__ == "__main__":
    main()
