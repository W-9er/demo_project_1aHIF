import random
import math

def set_random_position(rect, screen_width, screen_height):
    """Set a rect to a random position within the screen boundaries

    @param rect Rectangle to relocate
    @param screen_width Width of the screen
    @param screen_height Height of the screen

    @return The updated Rectangle
    """
    rect.left = random.randint(0, screen_width-rect.width)
    rect.top = random.randint(0, screen_height-rect.height)

    return rect


def random_direction():
    """Create a new random direction vector with unit length

    @return Returns a random direction vector
    """
    x = random.random() - 0.5
    y = random.random() - 0.5

    # Normalize to a length of 1
    l = math.sqrt(x*x + y*y)
    x /= l
    y /= l

    return [x, y]