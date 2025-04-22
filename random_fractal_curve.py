import math
import random
from PIL import Image

# Image dimensions
IMG_WIDTH = 300
IMG_HEIGHT = 600

# Create a new RGB image
image = Image.new("RGB", (IMG_WIDTH, IMG_HEIGHT))


def draw_fractal_curve(xa: float, ya: float, xb: float, yb: float, roughness: float):
    """
    Recursively draw a fractal curve between points (xa, ya) and (xb, yb).
    """
    xa_int = int(xa)
    ya_int = int(ya)
    xb_int = int(xb)
    yb_int = int(yb)

    dx = xb - xa
    dy = yb - ya
    distance = math.hypot(dx, dy)

    if distance <= 1:
        for x, y in [(xa_int, ya_int), (xb_int, yb_int)]:
            if 0 <= x < IMG_WIDTH and 0 <= y < IMG_HEIGHT:
                image.putpixel((x, y), (0, 255, 0))
        return

    mid_x = xa + dx * roughness
    mid_y = ya + dy * roughness + math.copysign(dx * roughness, random.uniform(-0.5, 0.5))

    draw_fractal_curve(xa, ya, mid_x, mid_y, roughness)
    draw_fractal_curve(mid_x, mid_y, xb, yb, roughness)


def main():
    # Random roughness for the curve
    roughness = random.uniform(0.3, 0.7)

    # Start drawing the fractal curve
    start_y = (IMG_HEIGHT - 1) / 2
    draw_fractal_curve(0, start_y, IMG_WIDTH - 1, start_y, roughness)

    # Save the result
    image.save("random_fractal_curve.png", "PNG")
    print("Fractal curve saved as 'random_fractal_curve.png'")


if __name__ == '__main__':
    main()
