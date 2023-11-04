"""buna baya baktim yaparken"""

def mergeSort(array):
    if(len(array)>1):
        orta = len(array)//2
        sol = array[:orta]
        sag = array[orta:]

        mergeSort(sol)
        mergeSort(sag)

        soli=0
        sagi=0
        arrayi=0

        while (soli<len(sol) and sagi <len(sag)):
            if(sol[soli]<sag[sagi]):
                array[arrayi]=sol[soli]
                soli=soli+1
            else :
                array[arrayi]=sag[sagi]
                sagi=sagi+1
            arrayi=arrayi+1

        while (soli<len(sol)):
            array[arrayi]=sol[soli]
            soli=soli+1
            arrayi=arrayi+1

        while (sagi<len(sag)):
            array[arrayi]=sag[sagi]
            sagi=sagi+1
            arrayi=arrayi+1

unsorted = [int(x) for x in input().split(",")]
mergeSort(unsorted)
print(unsorted)
        
