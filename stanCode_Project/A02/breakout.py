"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    lives = NUM_LIVES
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    while lives > 0:
        # ensure the ball is moving
        if graphics.get__dx() != 0 or graphics.get__dy() != 0:
            graphics.ball.move(graphics.get__dx(), graphics.get__dy())
            check_collision(graphics)  # collision check

            # If all bricks are removed, the game ends.
            if graphics.count_bricks == 0:
                print("You Win!")
                break

            # the left and the right borders rebound
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.set_dx(-graphics.get__dx())
            # the upper border rebound
            if graphics.ball.y <= 0:
                graphics.set_dy(-graphics.get__dy())
            # fall to the bottom, deduct life and reset the ball
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                lives -= 1
                graphics.set_ball_position()
                graphics.set_dx(0)
                graphics.set_dy(0)
        pause(FRAME_RATE)
    if lives == 0 or graphics.count_bricks != 0:
        print("You lose")  # game over!


def check_collision(graphics):
    """
    Detect whether the four vertices of the ball collide with the object
    """
    ball = graphics.ball
    window = graphics.window
    # Get the four vertices of the sphere
    points = [(ball.x, ball.y),  # top left corner
        (ball.x + ball.width, ball.y),  # top right corner
        (ball.x, ball.y + ball.height),  # lower left corner
        (ball.x + ball.width, ball.y + ball.height)]  # lower right corner

    for x, y in points:
        obj = window.get_object_at(x, y)
        if obj is not None:  # If the vertex has a collision
            if obj is graphics.paddle:  # Hit the board
                if graphics.get__dy() > 0:  # Make sure the ball bounces when it moves downward
                    graphics.set_dy(-graphics.get__dy())
            else:  # Hit the bricks
                graphics.set_dy(-graphics.get__dy())  # bounce
                window.remove(obj)  # remove bricks
                graphics.count_bricks -= 1  # Decrement the count after removing a brick
            return  # After collision handling, jump out of the loop


if __name__ == '__main__':
    main()
