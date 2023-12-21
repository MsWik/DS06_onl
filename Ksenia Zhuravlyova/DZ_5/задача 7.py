# Напишите функцию recursive_digit_sum, которая находит сумму всех цифр натурального числа.

def recursive_digit_sum(number):
    if number < 10:
        return number
    else:
        last_digit = number % 10
        remaining_digits = number // 10
        return last_digit + recursive_digit_sum(remaining_digits)

# Пример использования:
n = 12345
total_digit_sum = recursive_digit_sum(n)
print("Сумма всех цифр числа", n, "равна", total_digit_sum)

