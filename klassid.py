import pygame
import random


class Triangle(pygame.sprite.Sprite):
    '''
    Playeri klass. Selle abil tehakse sprite, mida saab nooltega juhtida.
    '''
    def __init__(self, x, y): # X ja Y koordinaadid
        super().__init__()
        self.x = x
        self.y = y

        #Playeri pilt ja väiksemaks scale'mine
        self.image = pygame.image.load('triangle.png')
        self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        
        self.rect.x = self.x
        self.rect.y = self.y


class Mine(pygame.sprite.Sprite):
    '''
    Miinide klass, mis kontrollib miinide tegevust.
    '''
    def __init__(self, x, y): # X ja Y koordinaadid
        super().__init__()
        self.x = x
        self.y = y

        #Miiinide pilt ja väiksemaks scale'mine
        self.image = pygame.image.load('mine.png')
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        
        self.rect.x = self.x
        self.rect.y = self.y
        
    def reset_pos(self):
        #Antakse x'le ja y'le suvaline väärtus arvude vahelt.
        self.rect.y = random.randrange(0, 100)
        self.rect.x = random.randrange(0, 800)
             
    def update(self, pikkus, kordus):
        # Mine'de kiirus.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.rect.y == 0
                elif event.key == pygame.K_SPACE:
                    self.rect.y += 5
        #Mine'de kiiruste suurendamine vastavalt korduste arvule
        if pikkus < 11:
            self.rect.y == 0
        elif kordus >= 10 and kordus < 20:
            self.rect.y += 6
        elif kordus >= 20:
            self.rect.y += 8
        else:
            self.rect.y += 5
        #Kui mine liiga alla satub, viiakse ta üles tagasi.
        if self.rect.y > 600:
            self.reset_pos()
