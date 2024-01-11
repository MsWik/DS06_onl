def recursive_digit_sum(args):
    if args < 10:
        return args
    else:
        return recursive_digit_sum(args // 10) + args % 10 


if __name__ == '__main__':
    print(recursive_digit_sum(1233))



