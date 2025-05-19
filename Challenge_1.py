def infix_to_postfix(tokens):
    """Convert an infix expression (list of tokens) to postfix notation."""
    preced = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []
    
    for tok in tokens:
        if tok.isalnum():  # operand (number or variable)
            output.append(tok)
        elif tok == '(':
            stack.append(tok)
        elif tok == ')':
            # pop until matching '('
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # discard '('
        else:
            # operator: pop higher-or-equal precedence operators first
            while (stack and stack[-1] in preced and
                   preced[stack[-1]] >= preced[tok]):
                output.append(stack.pop())
            stack.append(tok)
    
    # drain remaining operators
    while stack:
        output.append(stack.pop())
    
    return output


# ✅ Test cases
print(infix_to_postfix(['2', '+', '3']) ==
      ['2', '3', '+'])                    # ➕ Simple operation

print(infix_to_postfix(['2', '+', '3', '*', '4']) ==
      ['2', '3', '4', '*', '+'])          # 📊 Precedence test

print(infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']) ==
      ['2', '3', '+', '4', '*'])          # 🔗 Parentheses

print(infix_to_postfix(
    ['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')']
) == ['1', '2', '+', '3', '4', '-', '*']) # 🧮 Complex

print(infix_to_postfix(['a', '+', 'b', '*', 'c', '/', 'd']) ==
      ['a', 'b', 'c', '*', 'd', '/', '+']) # 🔤 Variables
