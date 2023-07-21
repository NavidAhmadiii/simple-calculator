def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("what's the first number? "))
    for symbol in operation:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation:")
        num2 = float(input("what's the next number? "))

        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        INPUT = input(f"Type 'y' to continue calculating with {answer}, or "
                      f"type 'n' to start new calculation or type 'e' to exit: ")

        if INPUT == "y":
            num1 = answer

        elif INPUT == "n":
            print("*" * 130)
            should_continue = False
            calculator()

        elif INPUT == "e":
            print("program finished ...")
            print("Good lock")
            break


calculator()
