# variables
#def printx(x):
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

def vargrab1():
    type_test=0

    while type_test == 0:
        x = input("Enter a number: ")
        if x.isnumeric():
            type_test=1
            #printx(x)
            return x
            
        else:
            print ("Try again bozo")


def vargrab2():
    type_test=0

    while type_test == 0:
        y = input("Enter a number: ")
        if y.isnumeric():
            type_test=1
            #print(y)
            return y
        else:
            print ("Try again bozo")
    
   
def mainloop():

    dead=False
    var = input("Do you want to divide(div), subtract(sub), add(add), multiply(mul), power(pow), root(root): ")
    x=vargrab1()
    y=vargrab2()
    type_of_operation(var,x,y)
    

def type_of_operation(var,x,y):
    if var.lower() == "div":
        
        # x = vargrab1()
        # y = vargrab2()
       
        division(x, y)
       
    elif var.lower() == "mul":
        # x = vargrab1()
        # y = vargrab2()
        multiplication(x,y)
    elif var.lower() == "add":
        # x = vargrab1()
        # y = vargrab2()
        addition(x,y)
    elif var.lower() == "sub":
        # x = vargrab1()
        # y = vargrab2()
        subtraction(x,y)
    elif var.lower() == "pow":
        # x = vargrab1()
        # y = vargrab2()
        pow(x,y)
    elif var.lower() == "root":
        # x = vargrab1()
        # y = vargrab2()
        root(x,y)
    elif var.lower() == "exit":
        exit()
    else:
        #var.lower() != "sub" or "add" or "mul" or "div" or "pow" or "root":
        print("invalid answer")
        dead=True
        mainloop()
mainloop()
#testloop()
