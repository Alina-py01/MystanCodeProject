"""
File: 
Name:Alina
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global variables
window = GWindow(800, 500, title='Bouncing Ball')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
bouncing = False  # Control whether the ball is moving
exit_count = 0  # Number of times the ball went beyond the right side


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball)
    onmouseclicked(start_bounce)


def start_bounce(mouse):
    """
    Handle the mouse click and make the ball bounce.
    """
    global bouncing, exit_count

    if not bouncing and exit_count < 3:
        bouncing = True
        simulate_bounce()


def simulate_bounce():
    """
    Simulates the bouncing motion of a ball, including the effects of gravity and bounds checking.
    """
    global bouncing, exit_count

    vy = 0  # Vertical speed
    while bouncing:
        ball.move(VX, vy)
        vy += GRAVITY
        # Bounce on the floor
        if ball.y + SIZE >= window.height:
            vy = -vy * REDUCE
            ball.y = window.height - SIZE
        # Beyond the right window
        if ball.x > window.width:
            exit_count += 1
            reset_ball()
            break
        pause(DELAY)
    bouncing = False


def reset_ball():
    """
    Reset the ball to the starting position.
    """
    global bouncing
    ball.x = START_X
    ball.y = START_Y
    bouncing = False


if __name__ == "__main__":
    main()
