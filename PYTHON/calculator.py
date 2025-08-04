def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"
print(calculator(10, 5, 'add'))
print(calculator(10, 5, 'subtract'))
print(calculator(10, 5, 'multiply'))
print(calculator(10, 5, 'divide'))
print(calculator(10, 0, 'divide'))
print(calculator(10, 5, 'modulus'))  # Invalid operation example