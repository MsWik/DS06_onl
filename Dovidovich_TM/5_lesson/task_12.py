# Нам был дан файл со скрытым текстом. И было сообщено, что для выделения полезной информации,
# нужно из каждого кода символа в тексте «выдернуть» младший байт.
# Это и будет код символа полезной информации.
# Однако есть одно «но». Если код символа меньше 128 — это и есть полезная информация.
# Разработайте программу, которая из текстового файла выделяет полезную информацию.
# Формат ввода
# В файле secret.txt хранится текст.
# Формат вывода
# Выведите спрятанное сообщение.
# Примечание
# Для манипуляции кодами символов изучите работу функций chr и ord.
# Пример
# Ввод
# ᥈୥ᙬᱬᝯ, ᭷ᝯ୲੬๤!
# Вывод
# Hello, world!


def task_12():
    file_name = "secret.txt"
    secret_message = ""
    with open(file_name, "r", encoding="utf-8") as input_file:
        secret_message = input_file.readline()
    input_file.close()
    for symbol in secret_message:
        if ord(symbol) < 128:
            print(symbol, end="")
        else:
            code = ord(symbol)
            pow_start = 31  # utf-8 4 byte
            while code > 128:
                if 2**pow_start > code:
                    pow_start -= 1
                else:
                    code -= 2**pow_start
            print(chr(code), end="")


if __name__ == "__main__":
    task_12()
