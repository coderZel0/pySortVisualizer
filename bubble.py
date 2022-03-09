def bubb(array):
    outList = []
    print(array)
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j+1]<array[j]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
        print(array)        
        outList.append(array)  

    return outList            


