import sys
class create_Node:
    def __init__(self):
        self.data = None
        self.next = None
class SL_LIST:
    def __init__(self):
        self.Header = None
    def insert_item(self,data):
        node = create_Node()
        node.data = data
        if self.Header == None:
            self.Header = node
        else:
            current = self.Header
            while current.next != None:
                current = current.next
            current.next = node
    def insert_any(self,key):
        node = create_Node()
        if self.Header == None:
            print("No insertion possible ")
        else:
            element = eval(input("Enter the new node data "))
            current = self.Header
            while ((current.next != None) and (current.data != key)):
                current = current.next
            else:
                if (current.data == key):
                    node.next = current.next
                    current.next = node
                    node.data = element
                else:
                    print("Key not found please try again ")
    def display(self):
        node = self.Header
        if self.Header == None:
            print("Linked list is empty... First create list ")
        else:
            while node:
                print(node.data)
                node = node.next
if __name__ == '__main__':
    try:
        s1 = SL_LIST()
        while True:
            print("\t\t\t...........Menu Items..........")
            print("\t\t\t 1. to insert value in the node ")
            print("\t\t\t 2. insert the any value after any existing item in node ")
            print("\t\t\t 3. print the list value ")
            print("\t\t\t 4. to Exit")
            n=int(input("Enter your choice: "))
            if n==1:
                x= eval(input("Enter value that u want to insert "))
                s1.insert_item(x)
            elif n==2:
                el= eval(input("Enter any existing item in this list "))
                s1.insert_any(el)
            elif n==3:
                s1.display()
            elif n==4:
                sys.exit()
            else:
                print("You entered wrong key....Try again ")
    except:
        print("There are some problem arise ")

