def res():
    restart = input("Do you want to go again?: ")
    if restart.lower() == "yes":
        mainloop()
    if restart.lower() == "no":
        exit()
    elif restart.lower() != "yes" or "no":
        print("Invalid answer. Answer yes or no")
        res()
def addition(x,y):
    z = int(x) + int(y)
    result = z
    print(result)
    res()
def subtraction(x,y):
    z = int(x) - int(y)
    result = z
    print(result)
    res()
def multiplication(x,y):
    z = int(x) * int(y)
    result = z
    print(result)
    res()
def division(x,y):
    z = int(x) / int(y)
    result = z
    print(result)
    res()
def pow(x,y):
    z = int(x) ** int(y)
    result = z
    print(result)
    res()
def root(x,y):
    z = int(y) ** (int(x) ** -1)
    result = z
    print(result)
    res()
def mainloop():
    dead=False
    var = input("Do you want to divide(div), subtract(sub), add(add), multiply(mul), power(pow), root(root): ")
    if var.lower() == "div":
        x = input("Enter a number: ")
        y = input("Enter a number: ")
        division(x,y)
    if var.lower() == "mul":
        x = input("Enter a number: ")
        y = input("Enter a number: ")
        multiplication(x,y)
    if var.lower() == "add":
        x = input("Enter a number: ")
        y = input("Enter a number: ")
        addition(x,y)
    if var.lower() == "sub":
        x = input("Enter a number: ")
        y = input("Enter a number: ")
        subtraction(x,y)
    if var.lower() == "pow":
        x = input("Enter a number: ")
        y = input("Enter a number: ")
        pow(x,y)
    if var.lower() == "root":
        x = input("Enter a number (What type of root): ")
        y = input("Enter a number (Number being rooted): ")
        root(x,y)
    elif var.lower() != "sub" or "add" or "mul" or "div" or "pow":
        print("invalid answer")
        dead=True
        mainloop()
mainloop()