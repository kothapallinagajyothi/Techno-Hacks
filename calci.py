def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "cannot divided by zero"
def get_number_input(prompt):
        while True:
            try:
                number=float(input(prompt))
                return number 
            except ValueError:
                print("It is a invalid input,please enter valid input ")
def calculator():
    print("Simple calculator")
    
    while True:
        print("\n select the operator: ")
        print("1.addition")
        print("2.subtraction")
        print("3.multiplication")
        print("4.division")
        print("5.exit")
        choice=input("Enter your choice (1,2,3,4,5) : ")
        if choice == "5":
            print("Exit from calculator ")
            break
        if choice not in ["1","2","3","4"]:
            print("Invalid choice.please enter a number from 1 to 5: ")
            continue
        num1= get_number_input("enter first number: ")
        num2= get_number_input("enter second number: ")
        if choice=="1":
            result = add(num1,num2)
            print(f"result : {num1}+{num2}={result}")
        if choice=="2":
            result = subtract(num1,num2)
            print(f"result : {num1}-{num2}={result}")
        if choice=="3":
            result = multiply(num1,num2)
            print(f"result : {num1}*{num2}={result}")
        if choice=="4":
            result = divide(num1,num2)
            print(f"result : {num1}/{num2}={result}")
if __name__=="__main__":
    calculator()
