quad = False
penta = False

color_map = {
    'B': 'blue',
    'G': 'green',
    'O': 'orange',
    'P': 'purple',
    'R': 'red',
    'Y': 'yellow'
}

matches_triple = {
    'match_right': {
        'blue': [],
        'green': [],
        'orange': [],
        'purple': [],
        'red': [],
        'yellow': []
    },
    'match_left': {
        'blue': [],
        'green': [],
        'orange': [],
        'purple': [],
        'red': [],
        'yellow': []
    },
    'match_down': {
        'blue': [],
        'green': [],
        'orange': [],
        'purple': [],
        'red': [],
        'yellow': []
    },
    'match_up': {
        'blue': [],
        'green': [],
        'orange': [],
        'purple': [],
        'red': [],
        'yellow': []
    }
}

matches_quad = {
    'match_right': {
        'blue': [],
        'green': [],
        'orange': [],
        'purple': [],
        'red': [],
        'yellow': []
    },
    'match_left': {
        'blue': [],
        'green': [],
        'orange': [],
        'purple': [],
        'red': [],
        'yellow': []
    },
    'match_down': {
        'blue': [],
        'green': [],
        'orange': [],
        'purple': [],
        'red': [],
        'yellow': []
    },
    'match_up': {
        'blue': [],
        'green': [],
        'orange': [],
        'purple': [],
        'red': [],
        'yellow': []
    }
}

matches_penta = {
    'match_right': {
        'blue': [],
        'green': [],
        'orange': [],
        'purple': [],
        'red': [],
        'yellow': []
    },
    'match_left': {
        'blue': [],
        'green': [],
        'orange': [],
        'purple': [],
        'red': [],
        'yellow': []
    },
    'match_down': {
        'blue': [],
        'green': [],
        'orange': [],
        'purple': [],
        'red': [],
        'yellow': []
    },
    'match_up': {
        'blue': [],
        'green': [],
        'orange': [],
        'purple': [],
        'red': [],
        'yellow': []
    }
}

matrix = [
    ['G', 'R', 'Y', 'G', 'R', 'P', 'B'],
    ['Y', 'B', 'Y', 'G', 'P', 'O', 'Y'],
    ['G', 'P', 'B', 'B', 'R', 'B', 'B'],
    ['G', 'Y', 'Y', 'O', 'B', 'P', 'R'],
    ['B', 'O', 'R', 'B', 'B', 'P', 'R'],
    ['R', 'G', 'O', 'Y', 'G', 'Y', 'P'],
    ['Y', 'O', 'G', 'B', 'G', 'P', 'R']
]


for row in range(0, 7):
    if quad or penta:
        break
    for col in range(0, 7):
        if quad or penta:
            break
        color = matrix[row][col]
        color_name = color_map.get(color)

        # CHECK MOVE RIGHT

        # Check right matches (3p)
        if col != 6 and col != 5 and col != 4:
            if matrix[row][col + 2] == color and matrix[row][col + 3] == color:
                matches_triple['match_right'][color_name].append((row, col))

        # Check up and down matches (3p)
        if row != 0 and row != 6 and col != 6:
            if matrix[row - 1][col + 1] == color and matrix[row + 1][col + 1] == color:
                matches_triple['match_right'][color_name].append((row, col))
        if row != 6 and row != 5 and row != 4 and col != 6:
            if matrix[row + 1][col + 1] == color and matrix[row + 2][col + 1] == color:
                matches_triple['match_right'][color_name].append((row, col))


        # Check up and down matches (4d)
        if row != 0 and row != 6 and col != 6:
            if (matrix[row + 1][col + 1] == color and
                    matrix[row - 1][col + 1] == color and
                    matrix[row - 2][col + 1] == color):
                matches_quad['match_right'][color_name].append((row, col))




        # # Check left
        # if col != 0:
        #     pass
        # # Check down
        # if row != 6:
        #     pass
        # # Check up
        # if col != 0:
        #     pass


print(matches_triple)
print('\n\n\n')
print(matches_quad)

# print('3ple')
# for direction, colors in matches_triple.items():
#     for color, lst in colors.items():
#         if lst:
#             print(f"'{direction}': {{'{color}': {lst}}}")
#
# print('quad')
# for direction, colors in matches_quad.items():
#     for color, lst in colors.items():
#         if lst:
#             print(f"'{direction}': {{'{color}': {lst}}}")