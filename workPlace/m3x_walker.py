class MatrixWalker:

    def __init__(self, matrix):

        self.quad = False
        self.penta = False
        self.matrix = matrix

        self.color_map = {
            'B': 'blue',
            'G': 'green',
            'O': 'orange',
            'P': 'purple',
            'R': 'red',
            'Y': 'yellow'
        }

        self.matches_triple = {
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

        self.matches_quad = {
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

        self.matches_penta = {
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

        self.m3x_walker()

    def m3x_walker(self):
        self.quad = False
        self.penta = False
        for row in range(0, 7):
            if self.quad or self.penta:
                break
            for col in range(0, 7):
                if self.quad or self.penta:
                    break
                color = self.matrix[row][col]
                color_name = self.color_map.get(color)


                # CHECK MOVE RIGHT

                # 3ple - 2 right
                if col not in [4, 5, 6]:
                    if (self.matrix[row][col + 2] == color
                            and self.matrix[row][col + 3] == color):
                        self.matches_triple['match_right'][color_name].append((row, col))
                # 3ple - above + bellow
                if row not in [0, 6] and col != 6:
                    if (self.matrix[row - 1][col + 1] == color
                            and self.matrix[row + 1][col + 1] == color):
                        self.matches_triple['match_right'][color_name].append((row, col))
                # 3ple - 2 above
                if row not in [0, 1] and col != 6:
                    if (self.matrix[row - 1][col + 1] == color and
                            self.matrix[row - 2][col + 1] == color):
                        self.matches_triple['match_right'][color_name].append((row, col))
                # 3ple - 2 bellow
                if row not in [5, 6] and col != 6:
                    if (self.matrix[row + 1][col + 1] == color and
                            self.matrix[row + 2][col + 1] == color):
                        self.matches_triple['match_right'][color_name].append((row, col))

                # quad - 1 above, 2 bellow
                if row not in [0, 5, 6] and col != 6:
                    if (self.matrix[row - 1][col + 1] == color and
                            self.matrix[row + 1][col + 1] == color and
                            self.matrix[row + 2][col + 1] == color):
                        self.quad = True
                        self.matches_quad['match_right'][color_name].append((row, col))
                # quad - 1 bellow, 2 above
                if row not in [6, 0, 1] and col != 6:
                    if (self.matrix[row + 1][col + 1] == color and
                            self.matrix[row - 1][col + 1] == color and
                            self.matrix[row - 2][col + 1] == color):
                        self.quad = True
                        self.matches_quad['match_right'][color_name].append((row, col))

                # penta - 2 above, 2 bellow
                if row not in [0, 1, 5, 6] and col != 6:
                    if (self.matrix[row - 1][col + 1] == color and
                            self.matrix[row - 2][col + 1] == color and
                            self.matrix[row + 1][col + 1] == color and
                            self.matrix[row + 2][col + 1] == color):
                        self.penta = True
                        self.matches_penta['match_right'][color_name].append((row, col))

                # penta - 2 above, 2 right
                if row not in [0, 1] and col not in [6, 5, 4]:
                    if (
                            self.matrix[row - 1][col + 1] == color and
                            self.matrix[row - 2][col + 1] == color and
                            self.matrix[row][col + 2] == color and
                            self.matrix[row][col + 3] == color
                    ):
                        self.penta = True
                        self.matches_penta['match_right'][color_name].append((row, col))

                # penta - 2 bellow, 2 right
                if row not in [6, 5] and col not in [6, 5, 4]:
                    if (
                            self.matrix[row + 1][col + 1] == color and
                            self.matrix[row + 2][col + 1] == color and
                            self.matrix[row][col + 2] == color and
                            self.matrix[row][col + 3] == color
                    ):
                        self.penta = True
                        self.matches_penta['match_right'][color_name].append((row, col))

                # CHECK MOVE LEFT

                # triple 2 left
                if col not in [0, 1, 2]:
                    if (
                            self.matrix[row][col - 2] == color and
                            self.matrix[row][col - 3] == color
                    ):
                        self.matches_triple['match_left'][color_name].append((row, col))

                # triple above and below
                if row not in [0, 6] and col != 0:
                    if (
                            self.matrix[row - 1][col - 1] == color and
                            self.matrix[row + 1][col - 1] == color
                    ):
                        self.matches_triple['match_left'][color_name].append((row, col))

                # triple - 2 above
                if row not in [0, 1] and col != 0:
                    if (
                            self.matrix[row - 1][col - 1] == color and
                            self.matrix[row - 2][col - 1] == color
                    ):
                        self.matches_triple['match_left'][color_name].append((row, col))

                # triple - 2 bellow
                if row not in [6, 5] and col != 0:
                    if (
                            self.matrix[row + 1][col - 1] == color and
                            self.matrix[row + 2][col - 1] == color
                    ):
                        self.matches_triple['match_left'][color_name].append((row, col))

                # quad - 1 above, 2 bellow
                if row not in [0, 6, 5] and col != 0:
                    if (
                            self.matrix[row - 1][col - 1] == color and
                            self.matrix[row + 1][col - 1] == color and
                            self.matrix[row + 2][col - 1] == color
                    ):
                        self.quad = True
                        self.matches_quad['match_left'][color_name].append((row, col))

                # quad - 1 bellow, 2 above
                if row not in [6, 0, 1] and col != 0:
                    if (
                            self.matrix[row + 1][col - 1] == color and
                            self.matrix[row - 1][col - 1] == color and
                            self.matrix[row - 2][col - 1] == color
                    ):
                        self.quad = True
                        self.matches_quad['match_left'][color_name].append((row, col))

                # penta - 2 above, 2 bellow
                if row not in [0, 1, 6, 5] and col != 0:
                    if (
                            self.matrix[row - 1][col - 1] == color and
                            self.matrix[row - 2][col - 1] == color and
                            self.matrix[row + 1][col - 1] == color and
                            self.matrix[row + 2][col - 1] == color
                    ):
                        self.penta = True
                        self.matches_penta['match_left'][color_name].append((row, col))

                # penta - 2 above, 2 left
                if row not in [0, 1] and col not in [0, 1, 2]:
                    if (
                            self.matrix[row - 1][col - 1] == color and
                            self.matrix[row - 2][col - 1] == color and
                            self.matrix[row][col - 2] == color and
                            self.matrix[row][col - 3] == color
                    ):
                        self.penta = True
                        self.matches_penta['match_left'][color_name].append((row, col))

                # penta - 2 bellow, 2 right
                if row not in [6, 5] and col not in [0, 1, 2]:
                    if (
                            self.matrix[row + 1][col - 1] == color and
                            self.matrix[row + 2][col - 1] == color and
                            self.matrix[row][col - 2] == color and
                            self.matrix[row][col - 3] == color
                    ):
                        self.penta = True
                        self.matches_penta['match_left'][color_name].append((row, col))

                # MOVE DOWN CHECKS

                # triple - 2 down
                if row not in [6, 5, 4]:
                    if (
                            self.matrix[row + 2][col] == color and
                            self.matrix[row + 3][col] == color
                    ):
                        self.matches_triple['match_down'][color_name].append((row, col))

                # triple - 2 right
                if row != 6 and col not in [6, 5]:
                    if (
                            self.matrix[row + 1][col + 1] == color and
                            self.matrix[row + 1][col + 2] == color
                    ):
                        self.matches_triple['match_down'][color_name].append((row, col))

                # triple - 2 left
                if row != 6 and col not in [0, 1]:
                    if (
                            self.matrix[row + 1][col - 1] == color and
                            self.matrix[row + 1][col - 2] == color
                    ):
                        self.matches_triple['match_down'][color_name].append((row, col))

                # quad - 1 left, 2 right
                if row != 6 and col not in [0, 6, 5]:
                    if (
                            self.matrix[row + 1][col - 1] == color and
                            self.matrix[row + 1][col + 1] == color and
                            self.matrix[row + 1][col + 2] == color
                    ):
                        self.quad = True
                        self.matches_quad['match_down'][color_name].append((row, col))

                # quad - 2 left, 1 right
                if row != 6 and col not in [0, 1, 6]:
                    if (
                            self.matrix[row + 1][col - 1] == color and
                            self.matrix[row + 1][col - 2] == color and
                            self.matrix[row + 1][col + 1] == color
                    ):
                        self.quad = True
                        self.matches_quad['match_down'][color_name].append((row, col))

                # penta - 2 left, 2 right
                if row != 6 and col not in [0, 1, 6, 5]:
                    if (
                            self.matrix[row + 1][col - 1] == color and
                            self.matrix[row + 1][col - 2] == color and
                            self.matrix[row + 1][col + 1] == color and
                            self.matrix[row + 1][col + 2] == color
                    ):
                        self.penta = True
                        self.matches_penta['match_down'][color_name].append((row, col))

                # penta - 2 down, 2 right
                if row not in [6, 5, 4] and col not in [6, 5]:
                    if (
                            self.matrix[row + 2][col] == color and
                            self.matrix[row + 3][col] == color and
                            self.matrix[row + 1][col + 1] == color and
                            self.matrix[row + 1][col + 2] == color
                    ):
                        self.penta = True
                        self.matches_penta['match_down'][color_name].append((row, col))

                # penta - 2 down, 2 left
                if row not in [6, 5, 4] and col not in [0, 1]:
                    if (
                            self.matrix[row + 2][col] == color and
                            self.matrix[row + 3][col] == color and
                            self.matrix[row + 1][col - 1] == color and
                            self.matrix[row + 1][col - 2] == color
                    ):
                        self.penta = True
                        self.matches_penta['match_down'][color_name].append((row, col))

                # MOVE UP CHECKS

                # triple - 2 up
                if row not in [0, 1, 2]:
                    if (
                            self.matrix[row - 2][col] == color and
                            self.matrix[row - 3][col] == color
                    ):
                        self.matches_triple['match_up'][color_name].append((row, col))

                # triple - 2 right
                if row != 0 and col not in [6, 5]:
                    if (
                            self.matrix[row - 1][col + 1] == color and
                            self.matrix[row - 1][col + 2] == color
                    ):
                        self.matches_triple['match_up'][color_name].append((row, col))

                # triple - 2 left
                if row != 0 and col not in [0, 1]:
                    if (
                            self.matrix[row - 1][col - 1] == color and
                            self.matrix[row - 1][col - 2] == color
                    ):
                        self.matches_triple['match_up'][color_name].append((row, col))

                # quad - 2 right, 1 left
                if row != 0 and col not in [0, 6, 5]:
                    if (
                            self.matrix[row - 1][col - 1] == color and
                            self.matrix[row - 1][col + 1] == color and
                            self.matrix[row - 1][col + 2] == color
                    ):
                        self.quad = True
                        self.matches_quad['match_up'][color_name].append((row, col))

                # quad - 2left, 1 right
                if row != 0 and col not in [0, 1, 6]:
                    if (
                            self.matrix[row - 1][col - 1] == color and
                            self.matrix[row - 1][col - 2] == color and
                            self.matrix[row - 1][col + 1] == color
                    ):
                        self.quad = True
                        self.matches_quad['match_up'][color_name].append((row, col))

                # penta - 2left, 2right
                if row != 0 and col not in [0, 1, 6, 5]:
                    if (
                            self.matrix[row - 1][col - 1] == color and
                            self.matrix[row - 1][col - 2] == color and
                            self.matrix[row - 1][col + 1] == color and
                            self.matrix[row - 1][col + 2] == color
                    ):
                        self.penta = True
                        self.matches_penta['match_up'][color_name].append((row, col))

                # penta - 2up, 2right
                if row not in [0, 1, 2] and col not in [6, 5]:
                    if (
                            self.matrix[row - 2][col] == color and
                            self.matrix[row - 3][col] == color and
                            self.matrix[row - 1][col + 1] == color and
                            self.matrix[row - 1][col + 2] == color
                    ):
                        self.penta = True
                        self.matches_penta['match_up'][color_name].append((row, col))

                # penta - 2up, 2left
                if row not in [0, 1, 2] and col not in [0, 1]:
                    if (
                            self.matrix[row - 2][col] == color and
                            self.matrix[row - 3][col] == color and
                            self.matrix[row - 1][col - 1] == color and
                            self.matrix[row - 1][col - 2] == color
                    ):
                        self.penta = True
                        self.matches_penta['match_up'][color_name].append((row, col))

        return self.matches_triple, self.matches_quad, self.matches_penta, self.quad, self.penta
