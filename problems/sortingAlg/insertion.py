list = [int(x) for x in input().split(",")]
for x in range(len(list)):
    a=x
    while(a>0 and list[a-1]>list[a]):
        temp =0
        temp = list[a]
        list[a]=list[a-1]
        list[a-1]=temp
        a=a-1
print(list)