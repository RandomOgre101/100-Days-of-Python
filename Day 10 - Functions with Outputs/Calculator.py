from art import logo

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)

    num1 = float(input("\nEnter the first number: "))
    for operation in operations:
        print(operation)

    should_continue = True

    while should_continue:
        symbol = input("\nPick an operation: ")
        num2 = float(input("\nWhat's the next number:  "))
        selected = operations[symbol]
        answer = selected(num1,num2)

        print(f"\n{num1} {symbol} {num2} = {answer}\n")

        if input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation: ").lower() == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()