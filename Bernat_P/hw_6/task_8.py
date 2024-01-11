def make_linear(*args):
    result = []
    i = 0
    while i < len(args):
        if type(args[i]) == int:
            result.append(args[i])
        else:
            result.append( int(args[i][0]))
        i += 1
    return result

if __name__ == '__main__':
    print(make_linear(1,2,3,['4'],[5]))