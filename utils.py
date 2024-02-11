def fact(number: int):
    if number < 0:
        return None

    if number == 0:
        return 1

    else:
        return number * fact(number - 1)


def is_pow_of_five(number: int):
    if number < 1:
        return False

    if number == 1:
        return True

    elif number % 5 != 0:
        return False

    return is_pow_of_five(number // 5)

