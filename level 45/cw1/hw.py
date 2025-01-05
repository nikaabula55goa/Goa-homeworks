def evaluate(equation):
    def at_operator(a, b):
        if b == 0:
            return None
        return (a + b) + (a - b) + (a * b) + (a // b)

    # Parse the equation
    tokens = []
    current_number = ""
    for char in equation:
        if char.isdigit() or char == '-':  # Handle digits and negatives
            current_number += char
        elif char == '@':  # Operator
            if current_number:
                tokens.append(int(current_number))
                current_number = ""
            tokens.append(char)
    if current_number:
        tokens.append(int(current_number))

    # Evaluate left-associatively
    while len(tokens) > 1:
        a, op, b = tokens[:3]
        if op == '@':
            result = at_operator(a, b)
            if result is None:
                return None
            tokens = [result] + tokens[3:]
        else:
            raise ValueError("Invalid operator")
    
    return tokens[0]

# Examples
print(evaluate("1 @ 1"))        # Output: 4
print(evaluate("3 @ 2"))        # Output: 13
print(evaluate("6 @ 9"))        # Output: 66
print(evaluate("4 @ -4"))       # Output: -9
print(evaluate("1 @ 1 @ -4"))   # Output: -9
print(evaluate("2 @ 2 @ 2"))    # Output: 40
print(evaluate("0@1@2"))        # Output: 0
print(evaluate("5 @ 0"))        # Output: None
