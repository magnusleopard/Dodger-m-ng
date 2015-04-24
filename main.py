import random
import pygame, sys
import klassid
import muutujad

def reset():
    for mine in all_sprites:
        if isinstance(mine, klassid.Mine):
            mine.kill()
    for i in range(10):
        mine = klassid.Mine(random.randrange(0, 800),random.randrange(0, 100))
        all_sprites.add(mine)
    all_sprites.add(alfa_mine)
   
def skoor(score):
    label = myfont.render("Score: "+ str(muutujad.kordus), 1,muutujad.black)
    screen.blit(label, (100, 100))

pygame.init()

myfont = pygame.font.SysFont("monospace", 15)
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
pygame.key.set_repeat(1,10)
pygame.display.set_caption("Dodger")

tervist = myfont.render("Press SPACE to begin.", 10, muutujad.green)
tervist1 = myfont.render("Press R to reset.", 10, muutujad.green)
kinni = myfont.render("Press SPACE to exit.", 10, muutujad.green)

#Teeme grupid
triangle_sprite = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

#Loome mine'd
for i in range(10):
    mine = klassid.Mine(random.randrange(0, 800),random.randrange(0, 100))
    all_sprites.add(mine)
    
#Lisame sprite'd gruppidesse    
alfa_mine = klassid.Mine(-100,random.randrange(0, 100)) #Alfa mine on selleks, et kordus töötaks korralikult.
all_sprites.add(alfa_mine)
triangle = klassid.Triangle(400, 555)
triangle_sprite.add(triangle)

beginning = True
running = False
over = False

#Esimene lõpmata kordus, mis läheb tööle, kui programm tööle panna.
while beginning:
    screen.fill(muutujad.white)
    all_sprites.draw(screen)
    triangle_sprite.draw(screen)
    screen.blit(tervist, (300, 400))
    screen.blit(tervist1, (310, 425))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            beginning = False
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #Kui vajutatakse space, siis lõpetatakse loop ning pandakse käima "running" loop.
                tervist = myfont.render("Press SPACE to begin.!", 10, muutujad.black)
                tervist1 = myfont.render("Press R to reset.", 10, muutujad.black)
                beginning = False
                running = True
    pygame.display.flip()

#Põhiloop, mis töötab mängu ajal.
while running:
    screen.fill(muutujad.white)
    skoor(muutujad.score)

    #Kui player saab miiniga pihta, loop lõpetatakse.
    if len(all_sprites) < 11:
        mine.rect.y == 0
        running = False
        over = True
        
    #Miin väljaspool väljakut, et kordus korralikult töötaks.
    if alfa_mine.rect.y >= 595:
        muutujad.kordus += 1
        alfa_mine.rect.y = 0
        
    #Kui player läheb mine-i vastu, kaob mine ära ja mäng seiskub.    
    if pygame.sprite.spritecollide(triangle, all_sprites, dokill = True):
        print("You had one job...")

    #Juhtimine ja kinni panek.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if triangle.rect.x <= 0:
                    triangle.rect.x = 0
                else:
                    triangle.rect.x -= muutujad.samm
            elif event.key == pygame.K_RIGHT:
                if triangle.rect.x >= 780:
                    triangle.rect.x = 780
                else:
                    triangle.rect.x += muutujad.samm
            elif event.key == pygame.K_UP:
                if triangle.rect.y <= 0:
                    triangle.rect.y = 0
                else:
                    triangle.rect.y -= muutujad.samm
            elif event.key == pygame.K_DOWN:
                if triangle.rect.y >= 580:
                    triangle.rect.y = 580
                else:
                    triangle.rect.y += muutujad.samm
            elif event.key == pygame.K_r:
                muutujad.kordus = 0
                reset()
        
    all_sprites.update(len(all_sprites), muutujad.kordus)
    triangle_sprite.draw(screen)
    all_sprites.draw(screen)
    
    pygame.display.flip() 
    clock.tick(100)

#Loop, mis läheb tööle, kui mängija kaotab. Kõik sprite-d lõpetavad töö.
while over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                over = False            
    lose = myfont.render("Game over!", 1, muutujad.green)
    screen.blit(lose, (350, 400))
    screen.blit(kinni, (305, 425))
    pygame.display.flip()
pygame.quit()
