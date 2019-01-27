import sys
class Node:
    def __init__(self):
        self.data=None
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None
    def add_node(self,data):
        New_node = Node()
        New_node.data = data
        New_node.next = self.head
        self.head=New_node
    def print_list(self):
        node = self.head
        if self.head==None:
            print("No Node exist in the linked list please insert first ")
        else:
            while node:
                print(node.data)
                node=node.next
if __name__ == '__main__':
    try:
        l1 = linked_list()
        while True:
            print("\t\t\t...........Menu Items..........")
            print("\t\t\t 1. to insert value in the node ")
            print("\t\t\t 2. to print the node value ")
            print("\t\t\t 3. to Exit")
            n=int(input("Enter your choice: "))
            if n==1:
                x=list(eval(i) for i in input("Enter some value that u want to insert ").split(","))
                for i in x:
                    l1.add_node(i)
            if n==2:
                l1.print_list()
            if n==3:
                sys.exit()
    except:
        print("There are some problem arise ")
