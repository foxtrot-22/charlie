# variables
# def printx(x):
#    print(x)

def res():
    restart = input("Do you want to go again?: ")
    if restart.lower() == "yes":
        mainloop()
    if restart.lower() == "no":
        exit()
    elif restart.lower() != "yes" or "no":
        print("Invalid answer. Answer yes or no")
        res()


def addition(x, y):
    z = int(x) + int(y)
    result = z
    print(result)
    res()


def subtraction(x, y):
    z = int(x) - int(y)
    result = z
    print(result)
    res()


def multiplication(x, y):
    z = int(x) * int(y)
    result = z
    print(result)
    res()


def division(x, y):
    z = int(x) / int(y)
    result = z
    print(result)
    res()


def pow(x, y):
    z = int(x) ** int(y)
    result = z
    print(result)
    res()


def root(x, y):
    z = int(y) ** (int(x) ** -1)
    result = z
    print(result)
    res()


def vargrab1():
    type_test = 0

    while type_test == 0:
        x = input("Enter a number: ")
        if x.isnumeric():
            type_test = 1
            # printx(x)
            return x

        else:
            print("Try again bozo")


def vargrab2():
    type_test = 0

    while type_test == 0:
        y = input("Enter a number: ")
        if y.isnumeric():
            type_test = 1
            # print(y)
            return y
        else:
            print("Try again bozo")


def mainloop():
    # dead=False
    operator_list = ["div", "sub", "add", "mul", "pow", "root"]
    # Original code
    # var = input("Do you want to divide(div), subtract(sub), add(add), multiply(mul), power(pow), root(root): ")
    while True:
        var = input("Do you want to divide(div), subtract(sub), add(add), multiply(mul), power(pow), root(root): ")
        if var.lower() not in operator_list:
            print("Please enter a valid operator")
        else:
            break
    x = vargrab1()
    y = vargrab2()
    type_of_operation(var, x, y)


# hello world
def type_of_operation(var, x, y):
    if var.lower() == "div":

        division(x, y)

    elif var.lower() == "mul":

        multiplication(x, y)
    elif var.lower() == "add":

        addition(x, y)
    elif var.lower() == "sub":

        subtraction(x, y)
    elif var.lower() == "pow":

        pow(x, y)
    elif var.lower() == "root":

        root(x, y)
    elif var.lower() == "exit":
        exit()
    else:

        print("invalid answer")

        mainloop()


mainloop()
