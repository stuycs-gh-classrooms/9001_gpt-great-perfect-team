from matrix import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = new_matrix()

def clear_screen():
    global screen
    screen = new_screen()

def display(screen):
    save_ppm(screen, 'pic.ppm')
    display('pic.ppm')

def save_extension(screen, fname):
    save_ppm(screen, fname)

def parse_file( fname, edges, polygons, screen, color ):
    f = open(fname)
    lines = f.readlines()

    c = 0
    while c < len(lines):
        line = lines[c].strip()

        if line == "line":
            c += 1
            args = lines[c].strip().split(' ')
            add_edge(edges, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
            matrix_mult(transform, edges)

        elif line == "circle":
            c += 1
            args = lines[c].strip().split(' ')
            add_circle(polygons, int(args[0]), int(args[1]), int(args[2]), int(args[3]))
            matrix_mult(transform, polygons)

        elif line == "bezier":
            c += 1
            args = lines[c].strip().split(' ')
            add_curve(polygons, "bezier", args)
            matrix_mult(transform, polygons)

        elif line == "hermite":
            c += 1
            args = lines[c].strip().split(' ')
            add_curve(polygons, "hermite", args)
            matrix_mult(transform, polygons)

        elif line == "display":
            display(screen)

        elif line == "save":
            c += 1
            args = lines[c].strip()
            save_extension(screen, args)

        elif line == "color":
            c += 1
            args = lines[c].strip().split(' ')
            color = [ int(args[0]), int(args[1]), int(args[2]) ]

        elif line == "clear":
            edges = []
            polygons = []
            clear_screen()

        elif line == "scale":
            c += 1
            args = lines[c].strip().split(' ')
            scale_matrix = make_scale(int(args[0]), int(args[1]), int(args[2]))
            matrix_mult(scale_matrix, transform)

        elif line == "move":
            c += 1
            args = lines[c].strip().split(' ')
            translate_matrix = make_translate(int(args[0]), int(args[1]), int(args[2]))
            matrix_mult(translate_matrix, transform)

        elif line == "rotate":
            c += 1
            args = lines[c].strip().split(' ')
            axis = args[0]
            theta = int(args[1])
            if axis == "x":
                rotate_matrix = make_rotX(theta)
            elif axis == "y":
                rotate_matrix = make_rotY(theta)
            elif axis == "z":
                rotate_matrix = make_rotZ(theta)
            matrix_mult(rotate_matrix, transform)

        elif line == "ident":
            ident(transform)

        elif line == "apply":
            matrix_mult(transform, edges)
            matrix_mult(transform, polygons)

        c += 1
