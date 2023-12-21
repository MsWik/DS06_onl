class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def get_stack(self):
        return self.stack

def evaluate_expression(expression):
    stack = Stack()
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.push(int(token))
        elif token == '+':
            b = stack.pop()
            a = stack.pop()
            stack.push(a + b)
        elif token == '*':
            b = stack.pop()
            a = stack.pop()
            stack.push(a * b)
        elif token == '-':
            b = stack.pop()
            a = stack.pop()
            stack.push(a - b)

    return stack.pop()

expression_1 = "7 2 3 * -"
expression_2 = "10 15 - 7 *"
result1 = evaluate_expression(expression_1)
result2 = evaluate_expression(expression_2)
print(result1)
print(result2)