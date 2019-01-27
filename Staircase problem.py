def staircase(step):
    if step ==1:
        return 1
    elif step ==2:
        return 2
    elif step ==3:
        return 3
    else:
        return (staircase(step-1) + staircase(step-2))
if __name__ == '__main__':
    x = int(input("Enter the staircase number "))
    print("No of the step is: ",staircase(x))

