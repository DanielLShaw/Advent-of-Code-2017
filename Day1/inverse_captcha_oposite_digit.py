def execute(captcha):
    # split the captcha into a list of numbers
    numbers = [int(d) for d in str(captcha)]
    output = 0
    for i, number in enumerate(numbers):
        # check the match oposite condition
        matchOposite = match_oposite(i, numbers)
        if matchOposite:
            output += number
    print(captcha, "-->", output)
    return output


def match_oposite(index, numbers):
    # find half the length of the number
    oposite_index = int(len(numbers) / 2)
    # find if the oposite digit is behind the number
    if index + oposite_index >= len(numbers):
        # find the index of the digit behind the number
        looped_index = index + oposite_index - len(numbers)
        if numbers[index] == numbers[looped_index]:
            return True
    elif numbers[index] == numbers[index + oposite_index]:
        return True
    else:
        return False
