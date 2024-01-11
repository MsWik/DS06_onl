
def multiplication_matrix(x):
    ans = []
    for i in range(1,x+1):
     ans.append([i * n for n in range(1,x+1)])   
    return ans


if __name__ == '__main__':
  print(multiplication_matrix(int(input())))   
