def calculator():
    print("Simple calculator")
    print("Operations: +,-,*,/")

    num1=float(input("Enter first number"))
    operator=input("Enter operation: (+,-,*,/)")
    num2=float(input("Enter the second number"))

    if operator == "+":  
            result = num1 + num2  
    elif operator == "-":  # Ensure correct indentation
            result = num1 - num2  
    elif operator == "*":  
            result = num1 * num2  
    elif operator == "/":  
        if num2 == 0:  
                result = "Error! Division by zero."  
        else:  
                result = num1 / num2  
    else:  
            result = "Invalid operator!"  

    print("Result:", result)
calculator()
