import pygame
import sys
from random import randint
from button import Button
from random import randint
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_w,
    K_s,
    QUIT,
)
SCREEN_HEIGHT=800
SCREEN_WIDTH=600

size= (SCREEN_HEIGHT,SCREEN_WIDTH)
pygame.init()
font=pygame.font.SysFont(r"res\font\JMH Typewriter.ttf",50)
screen =pygame.display.set_mode(size)
background=pygame.image.load(r"res\img\rect.png")
background=pygame.transform.scale(background,size)

screen.blit(background,(0,0))

frame=pygame.time.Clock()

class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super(Player1,self).__init__()
        self.surf=pygame.Surface((5,70))
        self.surf.fill((255,0,0))
        self.rect=self.surf.get_rect(
            center=(
                10,285
            )
        )
       # self.rect=((10,285))
    def update(self,pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0,-10)
        if pressed_keys[K_s]:
            self.rect.move_ip(0,10)

        if self.rect.top < 0:
            self.rect.top=0
        if self.rect.bottom > 600:
            self.rect.bottom=600            

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super(Player2,self).__init__()
        self.surf=pygame.Surface((5,70))
        self.surf.fill((255,0,0))

        self.rect=self.surf.get_rect(
            center=(
                790,285
            )
        )
       # self.rect=((10,285))
    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,10)

        if self.rect.top < 0:
            self.rect.top=0
        if self.rect.bottom > 600:
            self.rect.bottom=600 

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball,self).__init__()
        self.surf=pygame.Surface((40,40))
        self.surf.fill((0,0,0))

        
        pygame.draw.circle(self.surf,(255,255,255),(20,20),20)

        self.velocity=[randint(5,10),randint(-10,10)]
        self.rect=self.surf.get_rect(
            center=(
                380,280
            )
        )

    def update(self):
        self.rect.x+=self.velocity[0]
        self.rect.y+=self.velocity[1]    
        
    def bounce(self):
        self.velocity[0]*=-1
        self.velocity[1]=randint(-10,10)
     
def win( a, b):
    screen.fill((0,0,0))
    text1=font.render(str("Player 1 is winner!"),1,"white")
    text2=font.render(str("Player 2 is winner"),1,"white")
    text1_rect=text1.get_rect(center=(400,200))
    text2_rect=text2.get_rect(center=(400,200))
    if(a==10):
        screen.blit(text1,text1_rect)
        
        print(a)
    if(b==10):
        screen.blit(text2,text2_rect)
        
        print(b)
    #screen.blit(text,(200,20))    
    #pygame.time.wait(1000)        
    pygame.display.flip()
    pygame.time.wait(2000)
def play():
    player1=Player1()
    player2=Player2()
    ball=Ball()
    all_sprites=pygame.sprite.Group()
    all_sprites.add(player1)
    all_sprites.add(player2)
    all_sprites.add(ball)
    scoreA=9
    scoreB=0
    while True:
        
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()


        pressed_keys=pygame.key.get_pressed()
        player1.update(pressed_keys)
        player2.update(pressed_keys)
        ball.update()
        if(ball.rect.x>=760):
            scoreA+=1
            ball.velocity[0]*=-1 
            ball.surf.get_rect(center=(380,280))
            ball.rect.x=380
            ball.rect.y=280
            player1.rect.x=5
            player1.rect.y=265
            player2.rect.x=785
            player2.rect.y=265
            pygame.time.wait(1000)

        if(ball.rect.x<=0):
            scoreB+=1
            ball.velocity[0]*=-1
            ball.surf.get_rect(center=(380,280)) 
            ball.rect.x=380
            ball.rect.y=280
            player1.rect.x=5
            player1.rect.y=265
            player2.rect.x=785
            player2.rect.y=265
            pygame.time.wait(1000)
        if(ball.rect.y>=560 or ball.rect.y <=0):
                 ball.velocity[1]*=-1 
        if pygame.sprite.collide_rect(player1,ball) or pygame.sprite.collide_rect(ball,player2):
             ball.bounce()
             #font = pygame.font.Font(None,74)
             #text=font.render("BOUNCE",1,"white")
             #screen.blit(text,(200,200))         
        for j in range (0,601,50):
            pygame.draw.line(screen, "white", [795/2, j], [795/2,j+30], 1)
        for entity in all_sprites:
            screen.blit(entity.surf,entity.rect)
       # font = pygame.font.Font(font,74)
        text=font.render(str(scoreA),1,"white")
        screen.blit(text,(200,20))
        text = font.render(str(scoreB),1,"white")
        screen.blit(text,(600,20))
        if scoreA==10 or scoreB==10:

           win(scoreA,scoreB)
           menu()
            
        pygame.display.flip()
        frame.tick(30)

def menu():
    screen.fill("black")
    running =True
    while running:

        MENU_MOUSE_POS=pygame.mouse.get_pos()
        MENU_TEXT=font.render("MAIN MENU",True,(255,255,255))
        MENU_RECT=MENU_TEXT.get_rect(center=(400,100))
        screen.blit(MENU_TEXT,MENU_RECT)
    
        PLAY_BUTTON=Button(image=pygame.image.load(r"res\img\rect.png"), pos=(400,200),text_input="PLAY",font=font,base_colour="red",hovering_colour="green")
        QUIT_BUTTON=Button(image=pygame.image.load(r"res\img\rect.png"), pos=(400,400),text_input="QUIT",font=font,base_colour="red",hovering_colour="green")
        
        for button in [PLAY_BUTTON,QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sys.exit()    

        pygame.display.flip()
        frame.tick(60)


menu()