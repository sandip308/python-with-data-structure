#RETURN FIRST OCCOURANCE OF STRING
def return_string(n):
    for i in range(0,len(n)):
        for j in range(i+1,len(n)):
            if n[i] == n[j]:
                return n[i]
    else:
        return None
if __name__ == '__main__':
    x=input("Enter a string ")
    print(return_string(x))