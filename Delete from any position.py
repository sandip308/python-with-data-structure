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
    def delete_any(self,key):
        ptr = self.Header
        if self.Header == None:
            print("No node exist ")
        else:
            if ptr.data == key:
                self.Header = self.Header.next
                ptr.next == None
            else:
                while ((ptr.next != None) and (ptr.data != key)):
                    ptr1 = ptr
                    ptr = ptr.next
                if ptr.data == key:
                    ptr1.next = ptr.next
                    ptr.next = None
                else:
                    print("Key not found ... Try again ")
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
            print("\t\t\t 2. delete any value from the node ")
            print("\t\t\t 3. print the list value ")
            print("\t\t\t 4. to Exit")
            n=int(input("Enter your choice: "))
            if n==1:
                x= eval(input("Enter value that u want to insert "))
                s1.insert_item(x)
            elif n==2:
                el= eval(input("Enter any existing item in this list "))
                s1.delete_any(el)
            elif n==3:
                s1.display()
            elif n==4:
                sys.exit()
            else:
                print("You entered wrong key....Try again ")
    except:
        print("There are some problem arise ")

