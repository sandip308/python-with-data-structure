#RETURN FIRST OCCOURANCE OF STRING
def return_string(n):
    counts={}
    for x in n:
        if x in counts:
            return x
        else:
            counts[x]=1
    else:
        return None
if __name__ == '__main__':
    x= input("Enter a string ")
    print(return_string(x))