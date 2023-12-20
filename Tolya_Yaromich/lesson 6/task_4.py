def recursive_digit_sum(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        remaining_digits = n // 10
        return last_digit + recursive_digit_sum(remaining_digits)
