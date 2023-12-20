'''Напишите функцию recursive_digit_sum, которая находит сумму всех цифр натурального числа.'''


def recursive_digit_sum(num):
    if num < 10:
        return num
    else:
        last_digit = num % 10
        remaining_digits = num // 10
        return last_digit + recursive_digit_sum(remaining_digits)


print(recursive_digit_sum(123))


