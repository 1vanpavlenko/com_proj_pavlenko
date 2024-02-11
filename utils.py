def fact(number: int):
    if number < 0:
        return None

    if number == 0:
        return 1

    else:
        return number * fact(number - 1)


def Ncd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_prime(number: int):
    from math import ceil

    number = abs(number)

    if number == 0 or number == 1:
        return False

    elif number == 2:
        return True

    end = ceil(number ** 0.5) + 1

    for i in range(2, end):
        if number % 2 == 0:
            return False

    return True


def is_pow_of_five(number: int):
    if number < 1:
        return False

    if number == 1:
        return True

    elif number % 5 != 0:
        return False

    return is_pow_of_five(number // 5)


def from_dec_to_thirteen(dec_number: int):
    alphabet = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C')

    if dec_number < 13:
        return alphabet[dec_number]

    else:
        return from_dec_to_thirteen(dec_number // 13) + from_dec_to_thirteen(dec_number % 13)

