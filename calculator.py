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
    num1 = int(input("First number:\n"))
    num2 = int(input("Second number:\n"))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Operation: ")
    print(f"{num1} {operation_symbol} {num2} = {operations[operation_symbol](num1, num2)}")