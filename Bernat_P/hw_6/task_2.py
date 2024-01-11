
def make_matrix (size, value = 0):
    if isinstance(size,int):
        x = y = size
    else:
        x, y = size
    for i in range(1,y+1):
        print([value]*x,end='\n')


if __name__ == '__main__':
    make_matrix((2,3), value = 1)
