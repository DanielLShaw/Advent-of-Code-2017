import inverse_captcha_oposite_digit
if __name__ == '__main__':
    assert inverse_captcha_oposite_digit.execute(1212) == 6
    assert inverse_captcha_oposite_digit.execute(1221) == 0
    assert inverse_captcha_oposite_digit.execute(123425) == 4
    assert inverse_captcha_oposite_digit.execute(123123) == 12
    assert inverse_captcha_oposite_digit.execute(12131415) == 4
