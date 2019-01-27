Q={}
from math import *
def place(row,col):
    for i in range(1,row):
        if Q[i]==col:
            return False
        else:
            if (abs(i-row) == abs(Q[i]-col)):
                return False
    return True
def NQueen(row,n):
    for col in range(1,n+1):
        if (place(row,col)):
            Q[row] = col
            if row == n:
                display(n)
            else:
                NQueen(row+1,n)
c=0
def display(n):
    global c
    c=c+1
    print("\n Solution {}".format(c),end="\n\n")
    for i in range(1,n+1):
        print("{}".format(i),end="\t\t")
    for i in range(1,n+1):
        print("{}".format(i))
        for j in range(1,n+1):
            if Q[i]==j:
                print("Q",end="\t\t")
            else:
                print("-",end="\t\t")
if __name__ == '__main__':
    try:
        x = int(input("Enter the no of Queen "))
        NQueen(1,x)
    except SyntaxError:
        print("Please enter integer value ")
