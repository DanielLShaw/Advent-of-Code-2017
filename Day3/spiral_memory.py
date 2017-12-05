import sys


def execute(input):
    output = False
    print(input, "-->", output)


def make_dat_spiral(last_number):
    spiral = [[1, 2], [1, 2]]
    return spiral


def print_matrix(matrix):
    matrix_str = ""
    for row in matrix:
        row_str = ' '.join(str(i) for i in row)
        matrix_str += row_str + "\n"
    sys.stdout.write("\r%s" % matrix_str)


if __name__ == '__main__':
    big_boy_number = 23
    spiral = make_dat_spiral(big_boy_number)
    print_matrix(spiral)
