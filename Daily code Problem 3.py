'''GIVEN ARRAY OF INTEGER, RETURN A NEW ARRAY SUCH THAT EACH ELEMENT AT INDEX i OF THE NEW ARRAY
 IS PRODUCT OF ALL THE NUMBERS IN THE ORIGINAL ARRAY EXCEPT THE ONE AT i'''
from functools import reduce
def sort_index(n):
    y=[]
    z=[]
    for i in range(len(n)):
        for j in range(len(n)):
            if i==j:
                pass
            else:
                y.append(n[j])
        else:
            v= reduce(lambda a,b : a*b, y)
            z.append(v)
            y=[]
    else:
        print(z)
if __name__ == '__main__':
    x = [int(a) for a in input("Enter some value ").split(",")]
    sort_index(x)

