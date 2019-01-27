'''Given a list of number and a number K, return whether any two numbers from the list add up to K'''
def sum(n,k):
    p=[]
    for x in range(len(n)):
        flag=0
        s = k - n[x]
        z = get_index(n,x)
        if s in z:
            flag=1
            p.append(s)
            p.append(n[x])
            break
        else:
            continue
    if flag==1:
        return p
    else:
        return False
def get_index(n,x):
    p=[]
    for i in range(len(n)):
        if x==i:
            pass
        else:
            p.append(n[i])
    else:
        return p
if __name__ == '__main__':
    x = [int(a) for a in input("Enter some value ").split(",")]
    y= int(input("Enter the sum "))
    z=sum(x,y)
    if z== False:
        print("No match found ")
    else:
        print("Match found ")
        print("The elements are: ",z)