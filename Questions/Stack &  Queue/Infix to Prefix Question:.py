def infix_to_prefix(s):
    operators = set(['+', '-', '*', '/', '^', '(', ')'])
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []
    s = s[::-1]  # Reverse the string

    for char in s:
        if char not in operators:
            output.append(char)
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                output.append(stack.pop())
            stack.pop()  # Remove ')'
        else:
            while (stack and stack[-1] != ')' and
                   precedence.get(char, 0) < precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output[::-1])  # Reverse the output

if __name__=="__main__":
    Input1 = 'a*b+c/d'
    Output1 = '+*ab/cd '
    Input2 = '(a-b/c)*(a/k-l)'
    Output2 = '*-a/bc-/akl'
    print(infix_to_prefix(Input1))
    print(infix_to_prefix(Input2))