#in python semicolons are used for separation not termination
def printDetails(ID, name, *varArg):
    print("ID - ", ID);
    print("Name - ", name);
    for arg in varArg:
        print(arg);
printDetails(1, "Naveen", "IIT Bombay", "M. Tech CSE")
