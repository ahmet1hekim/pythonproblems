"koordinatlar 0dan basliyacak sekilde calisiyor"

from PIL import Image
from  numpy import asarray
img = Image.open('/home/alex/Documents/problems/reddott/1.png').convert('RGB')
imgarr = asarray(img)

red = [255,0,0]

for x in range(len(imgarr)):
    for y in range (len(imgarr[0])):
        if(imgarr[x][y].tolist()== red):
            print("RED")
            print(x,",",y)
             
            
    

    