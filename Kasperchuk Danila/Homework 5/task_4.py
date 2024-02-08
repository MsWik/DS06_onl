from random import randint

def main():
    right_answer = randint(1,1000)
    attempts_made = 0
    is_guessed = False
    while True:
        if attempts_made >= 10:
            print("Попытки закончились!")
            break
        user_attempt = int(input())

        if user_attempt > right_answer:
            print("Меньше")
            attempts_made += 1
        elif user_attempt < right_answer:
            print("Больше")
            attempts_made += 1
        elif user_attempt == right_answer:
            print("Угадал!")
            break
            is_guessed = True
        
    


if __name__ == '__main__':
    main()