def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

def start():
    next_num = True
    num1 = int(input("First number:\n"))
    for symbol in operations:
        print(symbol)
    while next_num:
        operation_symbol = input("Operation: ")
        num2 = int(input("Second number:\n"))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input("Next Number (y/n)") == "y":
            num1 = answer
        else:
            next_num = False

