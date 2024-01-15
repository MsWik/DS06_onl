# #4
# Угадайка, больше/меньше/угадал

def guess_the_number():
    left_bound = 1
    right_bound = 1001
    cnt = 0

    while True:
        cnt += 1
        mid = (left_bound + right_bound) // 2
        print(mid)
        feedback = input().strip()
        if feedback == "Угадал!":
            break
        elif feedback == "Меньше":
            right_bound = mid
        else:
            left_bound = mid + 1
        if cnt == 10:
            break


if __name__ == "__main__":
    guess_the_number()