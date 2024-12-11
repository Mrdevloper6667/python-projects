def addtion(n1,n2):
    return n1 + n2
def subtraction(n1,n2):
    return n1 - n2
def multipy(n1,n2):
    return n1 * n2
def division(n1,n2):
    return n1/n2






operator_dict = {
    "+" : addtion,
    "-" : subtraction,
    "*" : multipy,
    "/" : division
}

while True:
    n1 = float(input("Type the first number : "))
    while True:
        for key in operator_dict:
            print(key)
        operator = input("Choose an operator : ")
        n2 = float(input("Type the second number : "))
        result = operator_dict[operator](n1=n1,n2=n2)
        print(f"{n1} {operator} {n2} = {result}")
        proceed_with_result = input(f"Type 'yes' to continue calculating with {result}, or type 'no' to start a new calculation: ").lower()
        if proceed_with_result == "yes":
            n1 = result
        else :
            break    