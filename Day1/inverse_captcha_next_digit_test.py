import inverse_captcha_next_digit
if __name__ == '__main__':
    assert inverse_captcha_next_digit.execute(1122) == 3
    assert inverse_captcha_next_digit.execute(1111) == 4
    assert inverse_captcha_next_digit.execute(1234) == 0
    assert inverse_captcha_next_digit.execute(91212129) == 9
