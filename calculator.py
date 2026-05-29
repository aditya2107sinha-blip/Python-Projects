def function():

    number1= int(input("enter the number:"))
    operation=input("enter the operation you want to do:")
    number2=int(input("enter the number:"))

    if(operation=="*"):
        print(number1*number2)
    elif(operation=="/"):
        print(number1/number2)
    elif(operation=="+"):
        print(number1+number2)
    elif(operation=="-"):
        print(number1 - number2)
    elif(operation=="%"):
        print(number1%number2)

function()
