# draw.py
import matrix
import math

def new_screen(width, height):
    """
    Initialize a new screen with the specified dimensions.
    """
    return [[0] * width for _ in range(height)]

def plot(screen, color, x, y):
    """
    Set the pixel at position (x, y) on the screen to the specified color.
    """
    screen[y][x] = color

def add_edge(matrix, x0, y0, z0, x1, y1, z1):
    """
    Add an edge to the specified matrix connecting (x0, y0, z0) to (x1, y1, z1).
    """
    matrix.add_edge(x0, y0, z0, x1, y1, z1)

def add_circle(matrix, cx, cy, cz, r, steps=100):
    """
    Add a circle to the specified matrix centered at (cx, cy, cz) with radius r.
    The circle is approximated with the specified number of line segments (default 100).
    """
    x0, y0, z0 = r, 0, 0
    for i in range(steps+1):
        t = 2 * math.pi * i / steps
        x1 = r * math.cos(t)
        y1 = r * math.sin(t)
        z1 = 0
        matrix.add_edge(cx + x0, cy + y0, cz + z0, cx + x1, cy + y1, cz + z1)
        x0, y0, z0 = x1, y1, z1

def add_curve(matrix, type, *args, steps=100):
    """
    Add a curve to the specified matrix defined by the given control points.
    The type of curve is specified as a string ('bezier' or 'hermite').
    The curve is approximated with the specified number of line segments (default 100).
    """
    if type == "bezier":
        points = matrix.bezier_curve(*args, steps)
    elif type == "hermite":
        points = matrix.hermite_curve(*args, steps)
    else:
        raise ValueError(f"Unknown curve type: {type}")
    for i in range(len(points)-1):
        x0, y0, z0 = points[i]
        x1, y1, z1 = points[i+1]
        matrix.add_edge(x0, y0, z0, x1, y1, z1)

def draw_lines(matrix, screen, color):
    """
    Draw all the lines in the specified matrix onto the screen with the specified color.
    """
    for i in range(0, matrix.num_cols(), 2):
        x0, y0, _, x1, y1, _ = matrix.get_edge(i)
        matrix.draw_line(screen, color, x0, y0, x1, y1)

def save_ppm(screen, fname):
    """
    Save the specified screen as a PPM image with the specified filename.
    """
    with open(fname, 'w') as f:
        f.write('P3\n')
        f.write(f"{len(screen[0])} {len(screen)}\n")
        f.write('255\n')
        for row in screen:
            for col in row:
                f.write(f"{col} {col} {col} ")
            f.write('\n')
