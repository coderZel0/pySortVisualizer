import pygame


B_Gradients=[(0,171,240),(25,189,255),(55,198,255)]
R_Gradients=[(230,0,38),(230,0,76),(230,0,115)]

def drawlist(lst,posColors,surface,width,height,idx,sort=False,comp=False):
    for index,value in enumerate(lst):
        color = B_Gradients[index % 3]
        if index>idx and sort:
            color = R_Gradients[index % 3]
        if comp:
            color = R_Gradients[index % 3] 
        if index in posColors:
            color = posColors[index]

        pygame.draw.rect(surface,color,(index*width(),600-height(value),width(),height(value)))  
