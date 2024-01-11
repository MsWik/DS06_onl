def enter_results(*value):

    return value

def get_sum(value):
    print([value[i] + value[i+2] for i in range(0,len(value),2)])

if __name__ == '__main__':    
    print(enter_results(1,2,3,4),get_sum)


