#INPUT WILL BE ATLEAST ONE POSITIVE INTEGER
#MY SOLIUTION:->
def find_pos_int(n):
    for i in range(1,len(n)+2):
        if i not in n:
            print(i)
            break
        else:
            continue

if __name__ == '__main__':
    x=[int(a) for a in input("Enter some value: ").split(",")]
    find_pos_int(x)