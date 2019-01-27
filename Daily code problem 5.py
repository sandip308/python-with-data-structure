""" cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4"""
def cons(a,b):
    def car(f1):
        print("The car value is=",f1)
    def cdr(f2):
        print("The cdr value is=",f2)
    return car(a),cdr(b)
if __name__ == '__main__':
    a,b = int(input("Enter two value ")),int(input())
    z = cons(a,b)