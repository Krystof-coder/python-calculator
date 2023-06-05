first_num = int(input('first number: '))
operator = input('operation: ')
second_num = int(input('second number: '))

def result(a, b, o):
    
    if o == "+":
        return a + b
    elif o == "-":
        return a - b
    elif o == "*":
        return a * b
    elif o == "/":
        return a / b
    elif o == "**":
        return a ** b
    else:
        return "please use one of these operators: +, -, *, /"

result = result(first_num, second_num, operator)
print(result)