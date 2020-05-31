size = input("Enter the number of nodes in the circuit: ")
ArrOfArr = []
for i in range(0,int(size)):
    
    x = int(input(("x of point %d: ") % (i+1)))
    y = int(input(("y of point %d: ") % (i+1)))
    ArrOfArr.append([x,y])

print(ArrOfArr)