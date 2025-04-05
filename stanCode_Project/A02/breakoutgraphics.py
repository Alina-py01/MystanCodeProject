"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width) // 2, y=window_height - paddle_height - paddle_offset)
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.set_ball_position()
        self.window.add(self.ball)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.handle_mouse_click)
        onmousemoved(self.handle_mouse_move)
        ###
        self.count_bricks = 0  # Record the number of bricks remaining
        ###
        # Draw bricks
        self.draw_bricks(brick_rows, brick_cols, brick_width, brick_height, brick_offset, brick_spacing)

    def set_ball_position(self):
        x = (self.window.width-self.ball.width)//2
        y = (self.window.height - self.ball.height)//2
        self.ball.x = x
        self.ball.y = y

    def draw_bricks(self, rows, cols, width, height, offset, spacing):
        colors = ["red", "orange", "yellow", "green", "blue"]  # Color pattern
        for i in range(rows):
            for j in range(cols):
                brick = GRect(width, height)
                brick.filled = True
                brick.fill_color = colors[i // 2 % len(colors)]  # Assign color
                x_pos = j * (width + spacing)
                y_pos = offset + i * (height + spacing)
                self.window.add(brick, x=x_pos, y=y_pos)
                ###
                self.count_bricks += 1  # Each time a brick is added, the count increases by one.

    def handle_mouse_click(self, event):
        if self.__dx == 0 and self.__dy == 0:  # Start the game only if the ball has not moved
            self.__dy = INITIAL_Y_SPEED  # Set the vertical speed of the ball
            self.__dx = random.randint(1, MAX_X_SPEED)  # Set the horizontal speed of the ball
            # Randomly determine the direction of the ball
            if random.random() > 0.5:
                self.__dx = -self.__dx  # 50% chance to change direction

    def handle_mouse_move(self, event):
        # Calculate the new position of the board (let the board move with the mouse as the center)
        new_x = event.x - self.paddle.width / 2
        # Limit left border
        if new_x < 0:
            new_x = 0
        # Limit right border
        elif new_x > self.window.width - self.paddle.width:
            new_x = self.window.width - self.paddle.width
        self.paddle.x = new_x  # Update the board position

    def get__dx(self):
        return self.__dx

    def get__dy(self):
        return self.__dy

    def set_dx(self, dx):
        self.__dx = dx

    def set_dy(self, dy):
        self.__dy = dy
