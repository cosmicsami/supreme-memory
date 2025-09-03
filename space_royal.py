import pygame,pyautogui,time
from pygame.locals import *
pygame.font.init()
pygame.mixer.init()
WIDTH,HEIGHT=pyautogui.size()
space=pygame.display.set_mode((WIDTH,HEIGHT))
bg=pygame.transform.scale(pygame.image.load("space 2.png"),(WIDTH,HEIGHT))
sw,sh=WIDTH//20,HEIGHT//10
ys=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("1.png"),(sw,sh)),-90)
rs=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("2.png"),(sw,sh)),-90)
border=pygame.Rect(WIDTH/2-10,0,20,HEIGHT)

def pl1_go(keypress,pl_1):
    if keypress[pygame.K_w]and pl_1.y>0:
        pl_1.y-=3
    if keypress[pygame.K_a]and pl_1.x>0:
        pl_1.x-=3
    if keypress[pygame.K_s]and pl_1.y<HEIGHT-pl_1.height:
        pl_1.y+=3
    if keypress[pygame.K_d]and pl_1.x<border.x-pl_1.width:
        pl_1.x+=3
                
def pl2_go(keypress,pl_2):
    if keypress[pygame.K_UP]and pl_2.y>0:
        pl_2.y-=3
    if keypress[pygame.K_LEFT]and pl_2.x>border.x+border.width:
        pl_2.x-=3
    if keypress[pygame.K_DOWN]and pl_2.y<HEIGHT-pl_2.height:
        pl_2.y+=3
    if keypress[pygame.K_RIGHT]and pl_2.x<WIDTH-pl_2.width:
        pl_2.x+=3        

def handlebullets(pl_1,bullet1,pl_2,bullet2):
    for i in bullet1:
        i.x+=5
        if i.x<WIDTH:
            bullet1.remove(i)
        if i.colliderect(pl_2):
            bullet1.remove(i)    
def draw(pl_1,pl_2,bullet1,bullet2) :
    space.blit(bg,(0,0))
    space.blit(ys,(pl_1.x,pl_1.y))
    space.blit(rs,(pl_2.x,pl_2.y))
    pygame.draw.rect(space,"blue",border)
    for i in bullet1:
        pygame.draw.rect(space,"red",i)
    for s in bullet2:
        pygame.draw.rect(space,"red",s)
    pygame.display.update()



def main():
    pl_1=pygame.Rect(50,HEIGHT/2,sw,sh)
    pl_2=pygame.Rect(WIDTH-100,HEIGHT/2,sw,sh)
    bullet1=[]
    bullet2=[]
    while 1 :
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_e:
                    bullet=pygame.Rect(pl_1.x+pl_1.width/2,pl_1.y+pl_1.height/2,10,5)
                    bullet1.append(bullet)
                if event.key==pygame.K_RSHIFT:

                    bullet=pygame.Rect(pl_2.x+pl_2.width/2,pl_2.y+pl_2.height/2,10,5)
                    bullet2.append(bullet)

        draw(pl_1,pl_2,bullet1,bullet2)
        keypress=pygame.key.get_pressed()
        pl1_go(keypress,pl_1)
        pl2_go(keypress,pl_2)
main()            

