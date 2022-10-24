Number1 = int(input("Number1: "))
Number2 = int(input("Number2: "))
sign = input("Sign (+, -, *, /, **): ")
if sign == '+':
    print("Result: ", Number1 + Number2)
elif sign == '-':
    print("Result: ", Number1 - Number2)
elif sign == '*':
    print("Result: ", Number1 * Number2)
elif sign == '/':
    print("Result: ", Number1 / Number2)
elif sign == '**':
    print("Result: ", Number1 ** Number2)