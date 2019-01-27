import sys
if __name__ == '__main__':
    try:
        l1 = []
        while True:
            print("\t\t\t...........Menu Items..........")
            print("\t\t\t 1. to insert value in the node ")
            print("\t\t\t 2. remove the value from Node ")
            print("\t\t\t 3. to Search the element in the node ")
            print("\t\t\t 4. to replace the element ")
            print("\t\t\t 5. to print the elements")
            print("\t\t\t 6. to Exit")
            n=int(input("Enter your choice: "))
            if n==1:
                x=eval(input("Enter value that u want to insert: "))
                pos=int(input("Enter the position: "))
                l1.insert(pos,x)
            elif n==2:
                try:
                    if l1==[]:
                        print("List are empty...please insert some value ")
                    else:
                        print("You have two option to remove the node elements")
                        print("\t i) By the element name ...Press Y/y")
                        print("\t ii) By the position....Press N/n ")
                        v=input("Please press your choice: ")
                        if v=='Y' or v=='y':
                            elm=eval(input("Enter the element value or name: "))
                            l1.remove(elm)
                        elif v=='N' or v=='n':
                            ind=int(input("Please enter the element position: "))
                            l1.pop(ind)
                        else:
                            print("Please enter valid switch ")
                except ValueError:
                    print("Element not found on these Node")
                except IndexError:
                    print("Enter the valid index ")
            elif n==3:
                if l1==[]:
                    print("List are empty...please insert some value ")
                else:
                    elment=eval(input("Enter the element value or name"))
                    try:
                        pos=l1.index(elment)
                        print("Item found at position number: ",pos)
                    except ValueError:
                        print("Element not found ")
            elif n==4:
                try:
                    if l1==[]:
                        print("List are empty...please insert some value ")
                    else:
                        el = eval(input("Enter the element value or name"))
                        inde = int(input("At what position u want to replace ?"))
                        l1.pop(inde)
                        l1.insert(pos,el)
                except ValueError:
                    print("Element not found ")
                except IndexError:
                    print("Please enter valid index")
            elif n==5:
                if l1==[]:
                    print("List are empty ")
                else:
                    print("The elements are:")
                    for i in range(len(l1)):
                        print(l1[i])
            elif n==6:
                sys.exit()
            else:
                print("Please enter valid number")
    except:
        print("There are some problem arise ")

