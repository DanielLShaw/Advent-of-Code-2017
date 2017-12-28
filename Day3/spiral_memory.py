import sys
from collections import deque


def execute(input):
    output = False
    print(input, "-->", output)


def make_dat_spiral(last_number):
    i = 5
    Matrix = [[4, 3], [1, 2]]
    matrix_width = 2
    up = True
    left = True
    down = False
    right = False

    current_row = 0
    while i <= last_number:
        if matrix_square(Matrix):
            matrix_width += 1
            up = True
            left = True
            down = True
            right = True
            current_row = 0
            Matrix[0].insert(0, i)
        else:
            print(Matrix)
            print(down)
            print(len(Matrix))
            print(matrix_width)
            print(current_row)
            if down and len(Matrix) <= matrix_width:
                if current_row == len(Matrix) - 1:
                    Matrix += [i]
                    down = False
                    current_row += 1
                else:
                    current_row += 1
                    Matrix[current_row].insert(0, i)
            elif right and len(Matrix[current_row]) <= matrix_width:
                Matrix[current_row].append(i)
                if len(Matrix[current_row]):
                    right = False
            elif up and len(Matrix) <= matrix_width:
                if current_row == 0:
                    Matrix.insert(0, [i])
                    up = False
                else:
                    Matrix[current_row].append(i)
                    current_row -= 1
            elif left and len(Matrix[current_row]) <= matrix_width:
                Matrix[current_row].insert(0, i)
                if len(Matrix[current_row]):
                    left = False
        i += 1
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
    big_boy_number = 8
    output = make_dat_spiral(big_boy_number)
    print_matrix(output)
