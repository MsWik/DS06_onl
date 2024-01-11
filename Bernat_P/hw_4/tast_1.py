def solve():
  s = input()
  p = 'Yes'
  a = -1
  for i in range(len(s)):
    if s[i] != s[a]:
      p = 'No'
      break
    a -= 1
  print(p)

if __name__ == '__main__':
  solve()