import math

def dividers(number):
    allDividers =[]
    if (math.sqrt(number).is_integer()):
        allDividers.append(int(math.sqrt(number)))

    for x in range(math.floor(math.sqrt(number))-1):
        if(number%(x+1)==0):
            allDividers.append(int(x+1))
            allDividers.append(int(number/(x+1)))
    return allDividers        

print(dividers(int(input("sayi\n"))))