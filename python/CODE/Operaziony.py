import sys

def add(a, b):
    return (int(a)+int(b))

def mult(a, b):
    return (int(a) * int(b))

def pow(a, b):
    return (int(a)**int(b))

def divide(a, b):
    if (int(b) == 0):
        print("***Error: Division by zero!***\n")
        return
    if  (int(a) == 0):
        return 0
    else:
        return float(int(a)/int(b))

def menu():
    print("What do you want to do?\n")
    print("1:\tAdd 2 numbers\n2:\tMultiply 2 numbers\n3:\tPower of number A to exponent B\n4:\tExit\n")
    choice = input("Your choice? [1 - 2 - 3 - 4]\n")
    print("\n")
    return choice


if __name__ == '__main__':
    
    ciois = menu()
    while (int(ciois) != 4):
        if (int(ciois) == 1):
            i = input("Input your first operand:\t")
            j = input("Input your first operand:\t")
            print("\n\t\tResult: ", add(i,j))
            print("\n\n")
            print("Continue the execution? Input 1 to continue, 0 to exit\n")
            ciois = input("Your choice? [0: Exit - 1: Continue]\t")
            if (int(ciois) == 1):
                ciois = menu()
            elif (int(ciois) == 0):
                ciois = sys.exit()

        elif (int(ciois) == 2):
            i = input("Input your first operand:\t")
            j = input("Input your first operand:\t")
            print("\nResult: ", mult(i,j))
            print("\n\n")
            print("Continue the execution? Input 1 to continue, 0 to exit\n")
            ciois = input("Your choice? [0: Exit - 1: Continue]\t")
            if (int(ciois) == 1):
                ciois = menu()
            elif (int(ciois) == 0):
                ciois = sys.exit()

        elif (int(ciois) == 3):
            i = input("Input your Base:\t")
            j = input("Input your Exponent:\t")
            print("\n\t\tResult: ", pow(i,j))

            print("\n\n")
            print("Continue the execution? Input 1 to continue, 0 to exit\n")
            ciois = input("Your choice? [0: Exit - 1: Continue]\t")
            if (int(ciois) == 1):
                ciois = menu()
            elif (int(ciois) == 0):
                ciois = sys.exit()

        elif (int(ciois) == 4):
            sys.exit()
        else:
            print("\n\n\t\t\t***Input not valid***")
    
    