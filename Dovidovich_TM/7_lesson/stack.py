class Stack:
    def __init__(self) -> None:
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.is_empty())


if __name__ == '__main__':
    main()
