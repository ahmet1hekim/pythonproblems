import matplotlib.pyplot as plt 
boy=[]
kilo=[]
for i in range(10):
    print(str(i+1)+".ogrenci")
    boy.append(int( input("boy\n")))
    kilo.append(int(input("kilo\n")))
    print("\n\n")

plt.scatter(boy, kilo, label= "", color= "red",  
            marker= "*", s=30) 
plt.xlabel('boy') 
plt.ylabel('kilo') 
plt.title('boy/kilo') 

plt.show() 
