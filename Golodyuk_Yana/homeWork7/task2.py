## 2
# Класс Stack

class Stack:

    def __init__(self):
        self.l = []

    def push(self, item):
        self.l.append(item)

    def pop(self):
        return self.l.pop()

    def is_empty(self):
        return len(self.l) == 0

if __name__ == "__main__":
    stack = Stack()
    for item in range(10):
        stack.push(item)
    while not stack.is_empty():
        print(stack.pop(), end = " ")