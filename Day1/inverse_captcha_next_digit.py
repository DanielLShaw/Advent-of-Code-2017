def execute(captcha):
    # split the captcha into a list of numbers
    numbers = [int(d) for d in str(captcha)]
    output = 0
    for i, number in enumerate(numbers):
        # check if the next digit matches this one
        matchAfter = match_after(i, numbers)
        if matchAfter:
            output += number
    print(captcha, "-->", output)
    return output


def match_after(index, numbers):
    # check if this is this last number in the list
    if index == len(numbers) - 1 and numbers[0] == numbers[index]:
        return True
    elif index != len(numbers) - 1 and numbers[index + 1] == numbers[index]:
        return True
    else:
        return False
