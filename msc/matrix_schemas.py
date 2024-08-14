# Schemas for unit testing the ma3x walker


def happy_matrix_triple():
    # r3 c2 (G)
    matrix_right_happy = [
        ['P', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'B', 'Y', 'G', 'G', 'B', 'Y'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'G', 'O', 'B', 'P', 'G'],
        ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    # r1 c6 (G)
    matrix_left_happy = [
        ['P', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'B', 'Y', 'G', 'G', 'B', 'G'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'P', 'O', 'B', 'P', 'G'],
        ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    # r1 c4 (B)
    matrix_down_happy = [
        ['P', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'B', 'Y', 'G', 'B', 'B', 'Y'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'P', 'O', 'B', 'P', 'G'],
        ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    # r6 c4 (B)
    matrix_up_happy = [
        ['P', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'B', 'Y', 'G', 'G', 'B', 'Y'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'P', 'O', 'B', 'P', 'G'],
        ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'B', 'R', 'R']
    ]

    return matrix_right_happy, matrix_left_happy, matrix_down_happy, matrix_up_happy


def overboard_matrix_triple():
    # trying to move r1 c6 to r1 c0 (G)
    matrix_right_over_board = [
        ['P', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'B', 'Y', 'G', 'G', 'B', 'G'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'G', 'O', 'B', 'P', 'G'],
        ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    # trying to move r2 c0 to r2 c6 (G)
    matrix_left_over_board = [
        ['P', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'B', 'Y', 'G', 'G', 'B', 'G'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'P', 'O', 'B', 'P', 'G'],
        ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    # trying to move r6 c4 to r0 c4 (B)
    matrix_down_over_board = [
        ['P', 'R', 'Y', 'B', 'R', 'B', 'B'],
        ['Y', 'B', 'Y', 'G', 'B', 'B', 'Y'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'P', 'O', 'B', 'P', 'G'],
        ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'B', 'R', 'R']
    ]

    # trying to move r0 c4 to r6 c4 (R)
    matrix_up_over_board = [
        ['P', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'B', 'Y', 'G', 'G', 'B', 'Y'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'P', 'O', 'B', 'P', 'G'],
        ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    return matrix_right_over_board, matrix_left_over_board, matrix_down_over_board, matrix_up_over_board


def happy_matrix_quad():
    # r1 c3 (R)
    matrix_right_quad_happy = [
        ['P', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'B', 'Y', 'R', 'G', 'B', 'Y'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'P', 'O', 'R', 'P', 'G'],
        ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    # r3 c4 (G)
    matrix_left_quad_happy = [
        ['P', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'B', 'Y', 'G', 'G', 'B', 'Y'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'P', 'O', 'G', 'P', 'G'],
        ['B', 'O', 'R', 'G', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    # r4 c4 (Y)
    matrix_down_quad_happy = [
        ['P', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'B', 'Y', 'G', 'G', 'B', 'Y'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'P', 'O', 'B', 'P', 'G'],
        ['B', 'O', 'R', 'B', 'Y', 'P', 'R'],
        ['R', 'G', 'Y', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    # r2 c2 (G)
    matrix_up_quad_happy = [
        ['P', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'G', 'Y', 'G', 'G', 'B', 'Y'],
        ['G', 'P', 'G', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'P', 'O', 'B', 'P', 'G'],
        ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    return matrix_right_quad_happy, matrix_left_quad_happy, matrix_down_quad_happy, matrix_up_quad_happy


def overboard_matrix_quad():
    # trying to move from r6 c1 to r0 c1 (G)
    matrix_right_over_board_quad = [
        ['G', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'B', 'Y', 'G', 'G', 'B', 'G'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'P', 'O', 'B', 'P', 'G'],
        ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    # trying to move from r3 c0 to r3 c6 (R)
    matrix_left_over_board_quad = [
        ['P', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'B', 'Y', 'G', 'G', 'B', 'R'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'R'],
        ['R', 'Y', 'P', 'O', 'B', 'P', 'G'],
        ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    # trying to move r6 c3 to r0 c3 (B)
    matrix_down_over_board_quad = [
        ['P', 'B', 'B', 'Y', 'B', 'P', 'B'],
        ['Y', 'B', 'Y', 'G', 'G', 'B', 'Y'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'P', 'O', 'B', 'P', 'G'],
        ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    # trying to move r0 c5 to r6 c5 (G)
    matrix_up_over_board_quad = [
        ['P', 'R', 'Y', 'B', 'R', 'G', 'B'],
        ['Y', 'B', 'Y', 'G', 'G', 'B', 'Y'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'P', 'O', 'B', 'P', 'G'],
        ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'G', 'G', 'R', 'R']
    ]

    return (matrix_right_over_board_quad, matrix_left_over_board_quad, matrix_down_over_board_quad,
            matrix_up_over_board_quad)


def happy_matrix_penta():

    # r4 c1 (B)
    matrix_right_penta = [
        ['P', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'B', 'Y', 'G', 'G', 'B', 'Y'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'B', 'O', 'B', 'P', 'G'],
        ['B', 'B', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    # r3 c4 (G)
    matrix_left_penta = [
        ['P', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'B', 'Y', 'G', 'G', 'B', 'Y'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['P', 'G', 'G', 'O', 'G', 'P', 'G'],
        ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    # r2 c3 (G)
    matrix_down_penta = [
        ['P', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'B', 'Y', 'P', 'G', 'B', 'Y'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['P', 'G', 'G', 'O', 'G', 'G', 'P'],
        ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'R', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    # r5 c2 (B)
    matrix_up_penta = [
        ['P', 'R', 'Y', 'B', 'R', 'P', 'B'],
        ['Y', 'B', 'Y', 'G', 'G', 'B', 'Y'],
        ['G', 'P', 'B', 'G', 'R', 'R', 'B'],
        ['G', 'Y', 'P', 'O', 'B', 'P', 'G'],
        ['B', 'B', 'R', 'B', 'B', 'P', 'R'],
        ['R', 'G', 'B', 'Y', 'G', 'Y', 'G'],
        ['Y', 'O', 'G', 'B', 'G', 'R', 'R']
    ]

    return matrix_right_penta, matrix_left_penta, matrix_down_penta, matrix_up_penta

