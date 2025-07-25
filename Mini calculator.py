while True:
    try:
        a = int(input("Enter the first number(or type 0 to exit)- "))
        if a == 0:
            print("Ok, exiting...")
            break
        b = int(input("Enter the second number- "))
        solution = input("add/sub/mul/div- ").lower()
        if solution.lower() == 'add':
            print(a+b)
        elif solution.lower() == 'sub':
            print(a-b)
        elif solution.lower() == 'mul':
            print(a*b)
        elif solution.lower() == 'div':
            if b == 0:
                print("cannot divide by zero!")
            else:
                print(a/b)
        else:
            print("unknown operation")

    except ValueError:
        print("Invalid numbers")


