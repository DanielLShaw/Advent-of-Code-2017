import sys
from collections import deque


def execute(input):
    output = False
    print(input, "-->", output)


def make_dat_spiral(last_number):
    i = 2
    Matrix = [[1]]
    matrix_width = 1
    first_add = True

    up = True
    left = True
    down = True
    right = True

    current_row = 0
    while i <= last_number:
        if matrix_square(Matrix):

            matrix_width += 1
            if first_add:
                  # add a number to the bottom
                Matrix[current_row].append(i)
                first_add = False
            else:
                # add a number to the top
                Matrix[current_row].insert(0, i)
        else:
            if up:
                # if expanding upward to make new 1st row
                if current_row == 0:
                    Matrix.insert(0, [i])
                    up = False
                else:
                    Matrix[current_row].append(i)
                    current_row -= 1
            elif left:
                Matrix[current_row].insert(0, i)
        i += 1
    print(Matrix)
    return Matrix


def print_matrix(matrix):
    matrix_str = ""
    for row in matrix:
        if type(row) is list:
            row_str = ' '.join(str(i) for i in row)
        else:
            row_str = str(row)
        matrix_str += row_str + "\n"
    sys.stdout.write("\r%s" % matrix_str)


def matrix_square(matrix):
    matrix_height = len(matrix)
    for row in matrix:
        if type(row) is int:
            return True
        elif len(row) != matrix_height:
            return False
        else:
            return True


if __name__ == '__main__':
    big_boy_number = 4
    output = make_dat_spiral(big_boy_number)
    print_matrix(output)
