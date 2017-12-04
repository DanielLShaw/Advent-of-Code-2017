import re


def execute(input_file_path):
    # read the input file safely
    print("opening:", input_file_path)
    with open(input_file_path, "r") as input_file:
        # get a list of rows
        rows = input_file.readlines()
        for index, row in enumerate(rows):
            print(index, ":", row)
            # get numbers in row with a regex (seeing as the input file has space and tabs as delimeters)
            p = re.compile('\d')
            numbers = p.findall(row)

    output = False
    print(input_file_path, "-->", output)
    return output
