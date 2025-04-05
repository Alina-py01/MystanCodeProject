"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    space_between_lines = (width - 2 * GRAPH_MARGIN_SIZE) // len(YEARS)
    return GRAPH_MARGIN_SIZE + year_index * space_between_lines


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Draw top horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)

    # Draw bottom horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)

    # Draw vertical lines for each year
    for i, year in enumerate(YEARS):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)

        # Add year text below each vertical line
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=str(year), anchor=tkinter.NW, font=('Arial', 10))


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    num_years = len(YEARS)

    # Iterate through each name in lookup_names
    for i, name in enumerate(lookup_names):
        color = COLORS[i % len(COLORS)]  # Loop through colors
        prev_x, prev_y = None, None  # Used to store the coordinates of the previous point

        for j in range(num_years):
            year = str(YEARS[j])  # Convert to string
            x = get_x_coordinate(CANVAS_WIDTH, j)  # Calculate x coordinate

            # Get the ranking for that year, if not, set it to "*"
            if year in name_data.get(name, {}):
                rank = int(name_data[name][year])
                y = GRAPH_MARGIN_SIZE + (rank / MAX_RANK) * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)
            else:
                rank = '*'  # Ranking exceeds 1000
                y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE  # Set to the bottom

            # Draw the label "name ranking" at this point
            label = f"{name} {rank}"
            canvas.create_text(x + TEXT_DX, y, text=label, anchor=tkinter.SW, font=('Arial', 10), fill=color)

            # Draw a line from the previous point to the current year point
            if prev_x is not None and prev_y is not None:
                canvas.create_line(prev_x, prev_y, x, y, fill=color, width=LINE_WIDTH)

            # Update the coordinates of the previous point
            prev_x, prev_y = x, y


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
