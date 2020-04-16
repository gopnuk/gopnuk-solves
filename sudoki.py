import sys
from copy import deepcopy
def get_variants(sudoku):
    variants = []
    for i, row in enumerate(sudoku):
        for j, value in enumerate(row):
            if not value:
                row_values = set(row)
                column_values = set([sudoku[k][j] for k in range(4)])
                sq_y = i // 2
                sq_x = j // 2
                square2x2_values = set([
                    sudoku[m][n]
                    for m in range(sq_y * 2, sq_y * 2 + 2)
                    for n in range(sq_x * 2, sq_x * 2 + 2)
                ])
                exists = row_values | column_values | square2x2_values
                values = set(range(1, 5)) - exists
                variants.append((i, j, values))
    return variants
def solve_sudoku(matrix):
    if all([k for row in matrix for k in row]):
        return matrix
    variants = get_variants(matrix)
    x, y, values = min(variants, key=lambda x: len(x[2]))
    for v in values:
        new_sudoku = deepcopy(matrix)
        new_sudoku[x][y] = v
        s = solve_sudoku(new_sudoku)
        if s:
            for s1 in s:
                for x in s1:
                    print(x, end='')
                print()
a = [[int(x) for x in s] for s in map(str.strip, sys.stdin)]
solve_sudoku(a)
