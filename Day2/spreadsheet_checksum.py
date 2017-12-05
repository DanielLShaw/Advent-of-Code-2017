import re


def part1(input_file_path):
    output = 0
    # read the input file safely
    print("opening:", input_file_path)
    with open(input_file_path, "r") as input_file:
        # get a list of rows
        rows = input_file.readlines()
        for i, row in enumerate(rows):

            # get numbers in row with a regex (seeing as the input file has space and tabs as delimeters)
            p = re.compile('\d+')
            number_strs = p.findall(row)
            # convert list of strings to list of numbers
            numbers = []
            for j, number_str in enumerate(number_strs):
                numbers.append(int(number_strs[j]))
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
        for i, row in enumerate(rows):
            # get numbers in row with a regex (seeing as the input file has space and tabs as delimeters)
            p = re.compile('\d+')
            number_strs = p.findall(row)
            # convert list of strings to list of numbers
            numbers = []
            for number_str in number_strs:
                numbers.append(int(number_str))

            # sort list to get the smallest and largest
            numbers.sort()
            # see if lowest number goes into a larger number - repeat
            for k, number in enumerate(numbers):
                pointer = k + 1
                while pointer <= len(numbers) - 1:
                    # use Mod to find if divisible
                    if numbers[pointer] % numbers[k] == 0:
                        output += numbers[pointer] / numbers[k]
                        break
                    pointer += 1

    print(input_file_path, "-->", output)
    return output
