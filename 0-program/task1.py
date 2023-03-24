from PIL import Image

# function for drawing line using Bresenham's line algorithm
def drawline(x1, y1, x2, y2):
    img = Image.new('RGB', (512, 512), color = 'white')
    pixels = img.load()

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if x1 < x2:
        sx = 1
    else:
        sx = -1

    if y1 < y2:
        sy = 1
    else:
        sy = -1

    err = dx - dy

    while True:
        pixels[x1, y1] = (0, 0, 0)

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x1 += sx

        if e2 < dx:
            err += dx
            y1 += sy

    img.show()

# example usage of the drawline function
drawline(256, 100, 100, 256)