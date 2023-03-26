# engine.py

import math
from typing import List, Tuple

def create_matrix(rows: int, cols: int) -> List[List[float]]:
    """
    Creates a new matrix with the specified number of rows and columns,
    initialized to all zeros.
    """
    return [[0.0 for j in range(cols)] for i in range(rows)]

def multiply_matrices(m1: List[List[float]], m2: List[List[float]]) -> List[List[float]]:
    """
    Multiplies two matrices and returns the resulting matrix.
    """
    rows_m1 = len(m1)
    cols_m1 = len(m1[0])
    rows_m2 = len(m2)
    cols_m2 = len(m2[0])
    if cols_m1 != rows_m2:
        raise ValueError("Invalid matrix dimensions")
    result = create_matrix(rows_m1, cols_m2)
    for i in range(rows_m1):
        for j in range(cols_m2):
            for k in range(cols_m1):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def make_identity_matrix(size: int) -> List[List[float]]:
    """
    Creates a new identity matrix of the specified size.
    """
    result = create_matrix(size, size)
    for i in range(size):
        result[i][i] = 1.0
    return result

def make_translation_matrix(dx: float, dy: float, dz: float) -> List[List[float]]:
    """
    Creates a new translation matrix for the specified offset.
    """
    result = make_identity_matrix(4)
    result[0][3] = dx
    result[1][3] = dy
    result[2][3] = dz
    return result

def make_scale_matrix(sx: float, sy: float, sz: float) -> List[List[float]]:
    """
    Creates a new scale matrix for the specified factors.
    """
    result = make_identity_matrix(4)
    result[0][0] = sx
    result[1][1] = sy
    result[2][2] = sz
    return result

def make_rotation_matrix_x(theta: float) -> List[List[float]]:
    """
    Creates a new rotation matrix for the specified angle (in degrees) around the x-axis.
    """
    rad = math.radians(theta)
    cos = math.cos(rad)
    sin = math.sin(rad)
    result = make_identity_matrix(4)
    result[1][1] = cos
    result[1][2] = -sin
    result[2][1] = sin
    result[2][2] = cos
    return result

def make_rotation_matrix_y(theta: float) -> List[List[float]]:
    """
    Creates a new rotation matrix for the specified angle (in degrees) around the y-axis.
    """
    rad = math.radians(theta)
    cos = math.cos(rad)
    sin = math.sin(rad)
    result = make_identity_matrix(4)
    result[0][0] = cos
    result[0][2] = sin
    result[2][0] = -sin
    result[2][2] = cos
    return result

def make_rotation_matrix_z(theta: float) -> List[List[float]]:
    """
    Creates a new rotation matrix for the specified angle (in degrees) around the z-axis.
    """
    rad = math.radians(theta)