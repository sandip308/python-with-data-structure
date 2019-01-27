from collections import deque
import sys
if __name__ == '__main__':
    d = deque() #create a deque class object
    while True:
        print("\t\t\t ...........DEQUE OPERATIONS.................")
        print("\t\t\t 1. Add element at front ")
        print("\t\t\t 2. Remove element from front")
        print("\t\t\t 3. Add element at Rear ")
        print("\t\t\t 4. Remove element from Rear ")
        print("\t\t\t 5. Remove element from middle of deque")
        print("\t\t\t 6. Display the deque elements ")
        print("\t\t\t 7. EXIT")
        c = int(input("Enter your choice: "))
        if c==1:
            elm = eval(input("Enter one items "))
            d.appendleft(elm)
        elif c==2:
            if len(d)==0:
                print("Deque is empty ")
            else:
                d.popleft()
        elif c==3:
            elment = eval(input("Enter one items "))
            d.append(elment)
        elif c==4:
            if len(d)==0:
                print("Deque is empty ")
            else:
                d.pop()
        elif c==5:
            try:
                elem = eval(input("Enter a element to remove "))
                d.remove(elem)
            except ValueError:
                print("Element not found in deque ")
        elif c==6:
            print("Deque elements: ")
            for i in d:
                print(i, end=" ")
        elif c==7:
            sys.exit("Successfully out of this program ")
        else:
            print("You entered wrong key.... please try again ")