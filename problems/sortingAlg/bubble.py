list =[int(x) for x in input().split(",")]
for y in range(len(list)-1):
    for x in range(len(list)-1):
        if(list[x]>list[x+1]):
            temp = 0
            temp = list[x]
            list[x]=list[x+1]
            list[x+1]=temp
print(list)    