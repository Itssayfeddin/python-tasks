#calculator project
result=0
print("""this is a simple calculator code as a beginner:
use :
+ for sum;
-for subtraction;
* for multiplication;
/ for division;""")
def calculator(firstnum, secondnum ,operation):
    if operation == "+":
        return firstnum + secondnum
    elif operation == "-":
        return firstnum - secondnum
    elif operation == "*":
        return firstnum * secondnum
    elif operation == "/":
        return firstnum / secondnum
    else:
        print("Invalid operation")
while True:
    firstNum=float(input("Enter first number: "))
    operation=input("Enter operation: ")
    if result==0:
        secondNum = float(input("Enter second number: "))
        result=calculator(firstNum,secondNum,operation)
        print(f"the result is : {result}")
    else:
        user_action=input("do you want to use the result of last operation? y/n: ")
        if user_action=="y":
            result=calculator(firstNum,result,operation)
            print(f"the result is : {result}")
        elif user_action=="n":
            secondNum = float(input("Enter second number: "))
            result=calculator(firstNum,secondNum,operation)
            print(f"the result is : {result}")
        else:
            print("Invalid input")