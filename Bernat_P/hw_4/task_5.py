def solve():
  s = input().split()
  operations =[]
  stack = []
  for i in s:
    match i:
      case '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(int(a) + int(b))
      case '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(int(b) - int(a))
      case '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(int(a) * int(b))
      case _:
        stack.append(i)

  print(stack[0])  

if __name__ == '__main__':
    solve()

