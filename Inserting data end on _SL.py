import sys
class Node:
    def __init__(self):
        self.data=None
        self.next=None
class insert_end:
    def __init__(self):
        self.head=None
    def insert_last(self,data):
        node=Node()
        node.data = data
        if self.head==None:
            self.head=node
        else:
            current=self.head
            while current.next != None:
                current=current.next
            current.next = node

    def print_list(self):
        node = self.head
        if self.head == None:
            print("Please...first enter some values ")
        else:
            while node:
                print(node.data)
                node = node.next
if __name__ == '__main__':
    try:
        i1 = insert_end()
        while True:
            print("\t\t\t...........Menu Items..........")
            print("\t\t\t 1. to insert value in the node ")
            print("\t\t\t 2. to print the node value ")
            print("\t\t\t 3. to Exit")
            n=int(input("Enter your choice: "))
            if n==1:
                x= eval(input("Enter value that u want to insert "))
                i1.insert_last(x)
            elif n==2:
                i1.print_list()
            elif n==3:
                sys.exit()
            else:
                print("You entered wrong key....Try again ")
    except:
        print("There are some problem arise ")

