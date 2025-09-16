def add(fn, sn):
    result = fn + sn
    return result

def subtract(fn, sn):
    result = fn - sn
    return result

def multiply(fn, sn):
    result = fn * sn
    return result

def divide(fn, sn):
    result = fn / sn
    return result

choice = "START"

while True:
    if choice == "START" or choice == "n":
        fn = int(input("First Number: "))
    operation = str(input("Operation: "))
    sn = int(input("Second Number: "))

    if operation == "+":
        result = add(fn, sn)
        print(f"{fn} {operation} {sn} = {result}")
        
    elif operation == "-":
        result = subtract(fn, sn)
        print(f"{fn} {operation} {sn} = {result}")
        
    elif operation == "*":
        result = multiply(fn, sn)
        print(f"{fn} {operation} {sn} = {result}")

    elif operation == "/":
        result = divide(fn, sn)
        print(f"{fn} {operation} {sn} = {result}")

        
    
    choice = input(f"Type 'y' if you want to continue using {result} or 'n' to start a new calculation. \n")

    if choice == "y":
        fn = result
