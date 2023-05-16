import pygame 
import sys
from pygame.locals import *

img_galaxy = pygame.image.load("image_gl/galaxy.png")
img_sship = pygame.image.load("image_gl/starship.png")
img_weapon = pygame.image.load("image_gl/bullet.png")

bg_y = 0

#location of starship
ss_x = 480
ss_y = 360

#location of missile
MISSILE_MAX = 200
msl_no = 0
msl_f = [False]*MISSILE_MAX
msl_x = [0]*MISSILE_MAX
msl_y = [0]*MISSILE_MAX

#move starship and make bullet
def move_starship(scrn, key):
    global ss_x
    global ss_y

#the class attribution such as pygame.K_UP indicates the number of the key tapple
    if key[pygame.K_UP] == 1:
        ss_y = ss_y - 20
        if ss_y < 80:
            ss_y = 80
    if key[pygame.K_DOWN] == 1:
        ss_y = ss_y + 20
        if ss_y > 640:
            ss_y = 640
    if key[pygame.K_RIGHT] == 1:
        ss_x = ss_x + 20
        if ss_x > 920:
            ss_x = 920
    if key[pygame.K_LEFT] == 1:
        ss_x = ss_x - 20
        if ss_x < 40:
            ss_x = 40
    if key[K_z] == 1:
        set_missile()
    
    scrn.blit(img_sship, [ss_x-37, ss_y-48])

#set missile
def set_missile():
    """
    global msl_f, msl_x, msl_y
    if msl_f == False:
        msl_f = True
        msl_x = ss_x
        msl_y = ss_y - 50
    """
    global msl_no
    msl_f[msl_no] = True
    msl_x[msl_no] = ss_x
    msl_y[msl_no] = ss_y - 50
    msl_no = (msl_no+1)%MISSILE_MAX

def move_missile(scrn):
    #global msl_y, msl_f
    for i in range(MISSILE_MAX):
        if msl_f[i] == True:
            msl_y[i] = msl_y[i] - 36
            scrn.blit(img_weapon, [msl_x[i]-10,msl_y[i]-32])
            if msl_y[i] < 0:
                msl_f[i] = False

def main():
    global bg_y

    #initialize pygame
    pygame.init()
    pygame.display.set_caption("Touhou")
    # set screen size
    screen = pygame.display.set_mode((960,720))
    clock = pygame.time.Clock()

#main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    screen == pygame.display.set_mode((960,720), pygame.FULLSCREEN)
                if event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((960,720))
        
        screen.blit(img_galaxy, [-320, 0]) 


        key = pygame.key.get_pressed()
        move_starship(screen, key)
        move_missile(screen)
        


        #update screen
        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()

