def recursive_digit_sum(number: int) -> int:
    if number < 10:
        return number
    return number % 10 + recursive_digit_sum(number//10)


def task_6():
    print(recursive_digit_sum(678))


if __name__ == '__main__':
    task_6()
