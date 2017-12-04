import re


def part1(input_file_path):
    output = 0
    # read the input file safely
    print("opening:", input_file_path)
    with open(input_file_path, "r") as input_file:
        # get a list of rows
        rows = input_file.readlines()
        for index, row in enumerate(rows):

            # get numbers in row with a regex (seeing as the input file has space and tabs as delimeters)
            p = re.compile('\d+')
            number_strs = p.findall(row)
            # convert list of strings to list of numbers
            numbers = []
            for index, number_str in enumerate(number_strs):
                numbers.append(int(number_strs[index]))
            print(index, ":", numbers)
            # sort list to get the largest and smallest
            numbers.sort()

            output += numbers[len(numbers) - 1] - numbers[0]

    print(input_file_path, "-->", output)
    return output


def part2(input_file_path):
    output = 0
    # read the input file safely
    print("opening:", input_file_path)
    with open(input_file_path, "r") as input_file:
        # get a list of rows
        rows = input_file.readlines()
        for index, row in enumerate(rows):

            # get numbers in row with a regex (seeing as the input file has space and tabs as delimeters)
            p = re.compile('\d+')
            number_strs = p.findall(row)
            # convert list of strings to list of numbers
            numbers = []
            for index, number_str in enumerate(number_strs):
                numbers.append(int(number_strs[index]))
            print(index, ":", numbers)
            # sort list to get the largest and smallest

            # part 2 specific stuff

    print(input_file_path, "-->", output)
    return output
