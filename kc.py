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
    ['Y', 'B', 'Y', 'G', 'B', 'B', 'Y'],
    ['G', 'P', 'B', 'B', 'R', 'R', 'B'],
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

        # 3ple - 2 right
        if col not in [4, 5, 6]:
            if (matrix[row][col + 2] == color
                    and matrix[row][col + 3] == color):
                matches_triple['match_right'][color_name].append((row, col))
        # 3ple - above + bellow
        if row not in [0, 6] and col != 6:
            if (matrix[row - 1][col + 1] == color
                    and matrix[row + 1][col + 1] == color):
                matches_triple['match_right'][color_name].append((row, col))
        # 3ple - 2 above
        if row not in [0, 1, 2] and col != 6:
            if (matrix[row - 1][col + 1] == color and
                    matrix[row - 2][col + 1] == color):
                matches_triple['match_right'][color_name].append((row, col))
        # 3ple - 2 bellow
        if row not in [4, 5, 6] and col != 6:
            if (matrix[row+1][col+1] == color and
                    matrix[row+2][col+1] == color):
                matches_triple['match_right'][color_name].append((row, col))

        # quad - 1 above, 2 bellow
        if row not in [0, 5, 6] and col != 6:
            if (matrix[row - 1][col +1] == color and
                    matrix[row + 1][col + 1] == color and
                    matrix[row + 2][col + 1] == color):
                quad = True
                matches_quad['match_right'][color_name].append((row, col))
        # quad - 1 bellow, 2 above
        if row not in [6, 0, 1] and col != 6:
            if (matrix[row + 1][col + 1] == color and
                    matrix[row - 1][col + 1] == color and
                    matrix[row - 2][col + 1] == color):
                quad = True
                matches_quad['match_right'][color_name].append((row, col))

        # penta - 2 above, 2 bellow
        if row not in [0, 1, 5, 6] and col != 6:
            if (matrix[row - 1][col + 1] == color and
                    matrix[row - 2][col + 1] == color and
                    matrix[row + 1][col + 1] == color and
                    matrix[row + 2][col + 2] == color):
                penta = True
                matches_penta['match_right'][color_name].append((row, col))


print('triple')
print(matches_triple)
print('\n\n\n')
print('quad')
print(matches_quad)
print('\n\n\n')
print('penta')
print(matches_penta)

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
