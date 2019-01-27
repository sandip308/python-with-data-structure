def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def find_gcd(l,n):
    result = l[0]
    for i in range(n):
        result = gcd(l[i],result)
    return result
if __name__ == '__main__':
    try:
        x=list(int(a) for a in input("Enter some values ").split(','))
        p= sorted(x,reverse=False)
        n=len(p)
        print(find_gcd(p,n))
    except TypeError:
        print("Please enter integer value ")
    except:
        print("There are some problem ")
