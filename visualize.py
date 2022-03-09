import pygame,sys
import random
from draw import drawlist
#from bubble import bubb

WIDTH = 800
HEIGHT =600

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
sort = False
complete = False

def genList(min_val,max_val):
    lst = []
    for _ in range(100):
        lst.append(random.randint(min_val,max_val))
    return lst

def bubb(array):
    outList = []
    print(array)
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            done_idx = len(array)-1-i
            if array[j+1]<array[j]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                drawlist(array,{j:"red",j+1:"yellow"},screen,getWidth,getHeight,done_idx,sort,complete) 
                yield True   

    return array     

max_node_height = HEIGHT-200
mylist=genList(5,50)
max_value = max(mylist)
#drawList = mylist[0]
Count = 0
Ind = 0

factor = max_node_height/max_value

def getHeight(item):
    if(item == max_value):
        return 400
    else:
        return factor*item
def getWidth():
    return WIDTH//len(mylist)




length = len(mylist)        
print(length)

sort_algo_gen = bubb(mylist)
while True:
    screen.fill((200,200,100))
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sort = True  
            if event.key == pygame.K_ESCAPE:
                pygame.quit()      
    
    #print(Ind)
    if sort:
        try:
            next(sort_algo_gen)
        except StopIteration:
            sort = False  
            complete = True  
    else:
        drawlist(mylist,{},screen,getWidth,getHeight,-1,sort,complete)  
    #pygame.time.delay(20)
    pygame.time.Clock().tick(60)
    pygame.display.update()