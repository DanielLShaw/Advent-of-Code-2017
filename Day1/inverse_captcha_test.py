import inverse_captcha
if __name__ == '__main__':
    assert inverse_captcha.execute(1122) == 3
    assert inverse_captcha.execute(1111) == 4
    assert inverse_captcha.execute(1234) == 0
    assert inverse_captcha.execute(91212129) == 9
