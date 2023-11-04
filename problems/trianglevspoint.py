def area(cor1,cor2,cor3):
    
    ar = (1/2)*(cor1[0]*(cor2[1]-cor3[1])+cor2[0]*(cor3[1]-cor1[1])+cor3[0]*(cor1[1]-cor2[1]))
    if(ar>0):
        return ar 
    elif(ar<=0):
        return -ar

cor1 = [int(x) for x in input().split(",")]
cor2 = [int(x) for x in input().split(",")]
cor3 = [int(x) for x in input().split(",")]
point = [int(x) for x in input().split(",")]

if(area(cor1,cor2,cor3)==(area(cor1,cor2,point)+area(cor2,cor3,point)+area(cor1,cor3,point))):
   print("in")
else:
    print("out")    
    