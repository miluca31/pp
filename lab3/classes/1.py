class MyClass():
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input("Enter a string: ") #Get a string from console input.

    def printString(self):
        print(self.str.upper()) #Print the string in upper case.

a = MyClass()

a.getString()
a.printString()