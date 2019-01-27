import sys
# QUEUE IS SAME AS STACK BUT WHEN WE INSERT VALUE IN QUEUE WE USE append function INSTEAD OF insert FUNCTION
class stack:
    def __init__(self):
        self.st = []
    def isempty(self):
        return self.st ==[]
    def get_index(self):
        self.c= -1
        self.c+=1
        return self.c
    def push(self,value):
        return self.st.insert(self.get_index(),value)
    def pop(self):
        if self.isempty():
            return -1
        else:
            return self.st.pop(self.get_index())
    def Topmost(self):
        return self.st[self.get_index()]
    def display(self):
        return self.st
if __name__ == '__main__':
    s = stack()
    while True:
        print("\t\t\t ..............MENU ITEMS.....................")
        print("\t\t\t 1. to PUSH elements")
        print("\t\t\t 2. to POP elements")
        print("\t\t\t 3. to know the TOPMOST element ")
        print("\t\t\t 4. to display the elements in this class")
        print("\t\t\t 5. to EXIT")
        n = int(input("Enter your choice: "))
        if n==1:
            x=eval(input("Enter the value that u want to push "))
            s.push(x)
        elif n==2:
            elm = s.pop()
            if elm==-1:
                print("Stack is empty ")
            else:
                print("The pop element is: ",elm)
        elif n==3:
            print("The topmost element is: ",s.Topmost())
        elif n==4:
            x = []
            x= s.display()
            for i in range(len(x)):
                print(x[i])
        elif n==5:
            sys.exit("Successfully out of the program ")
        else:
            print("You entered wrong key... please try again ")

