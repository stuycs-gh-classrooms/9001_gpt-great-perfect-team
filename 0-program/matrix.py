import math

def make_bezier():
    return [[-1, 3, -3, 1],
            [3, -6, 3, 0],
            [-3, 3, 0, 0],
            [1, 0, 0, 0]]

def make_hermite():
    return [[2, -2, 1, 1],
            [-3, 3, -2, -1],
            [0, 0, 1, 0],
            [1, 0, 0, 0]]

def generate_curve_coefs( p0, p1, p2, p3, t ):
    coefs = [[p0, p1, p2, p3]]
    if t == "bezier":
        matrix = make_bezier()  
    elif t == "hermite":
        matrix = make_hermite()
    else:
        return None

    coefs_matrix = [[coefs[0][0], coefs[0][1], coefs[0][2], coefs[0][3]]]
    matrix_mult(matrix, coefs_matrix)

    return coefs_matrix[0]

def make_translate( x, y, z ):
    return [[1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]]

def make_scale( x, y, z ):
    return [[x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]]

def make_rotX( theta ):
    theta = math.radians(theta)
    return [[1, 0,              0,               0],
            [0, math.cos(theta), math.sin(-theta), 0],
            [0, math.sin(theta), math.cos(theta),  0],
            [0, 0,              0,               1]]

def make_rotY( theta ):
    theta = math.radians(theta)
    return [[math.cos(theta),  0, math.sin(theta), 0],
            [0,               1, 0,              0],
            [math.sin(-theta), 0, math.cos(theta), 0],
            [0,               0, 0,              1]]

def make_rotZ( theta ):
    theta = math.radians(theta)
    return [[math.cos(theta), math.sin(-theta), 0, 0],
            [math.sin(theta), math.cos(theta),  0, 0],
            [0,              0,               1, 0],
            [0,              0,               0, 1]]

def matrix_mult( m1, m2 ):
    temp = []
    for r in range(4):
        row = []
        for c in range(4):
            sum = 0
            for i in range(4):
                sum += m1[r][i] * m2[i][c]
            row.append(sum)
        temp.append(row)
    # copy temp into m2, so that m2 is the product of m1 and m2
    for r in range(4):
        for c in range(4):
            m2[r][c] = temp[r][c]
            
def new_matrix(rows=4, cols=4):
    """
    Creates and returns a new matrix of size rows x cols with all elements initialized to 0.
    """
    return [[0 for j in range(cols)] for i in range(rows)]


def ident(matrix):
    """
    Changes matrix to an identity matrix.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
