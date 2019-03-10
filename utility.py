import numpy as np

TRANSPOSE_COLUMNS = 2

def string_to_matrix(string, shape):
    """
    Returns matrix of type ndarray
    """

    string_list = np.array(list(string))

    matrix = np.reshape(string_list, shape, order='F')
    return matrix


def transpose_and_rotate_string(string):
    matrix_shape = (len(string) // TRANSPOSE_COLUMNS,\
        TRANSPOSE_COLUMNS)

    matrix_form = string_to_matrix(string, matrix_shape)

    # Reverse rows within the matrix
    for row in range(len(matrix_form)):
        matrix_form[row] = matrix_form[row][::-1]

    list_form = np.reshape(matrix_form, len(string))

    return ''.join(list_form)