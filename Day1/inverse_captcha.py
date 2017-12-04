def execute(captcha):
    numbers = [int(d) for d in str(captcha)]
    output = 0
    for i, number in enumerate(numbers):
        print(i, number)
    return output
