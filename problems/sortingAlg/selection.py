list = [int(x) for x in input().split(",")]
for x in range(len(list)):
    current_min=x
    for y in range(len(list)):
        if(list[y]>list[current_min]):
            current_min=y
            temp = list[x]
            list[x]=list[y]
            list[y]=temp
            temp=0
print(list)