import pygame
import random


class Pilot():
    def __init__(self,ventana,px,py,bandera,velo,cuentaPasose,toca) -> None:
        self.ventana=ventana
        self.px = px
        self.py = py
        self.velo = velo
        self.bandera = bandera
        self.cuentaPasose = cuentaPasose
        self.toca = toca
        self.caminar_ene = [pygame.transform.scale(pygame.image.load('recursos/sprites/aereo/Fly (1).png'),(80,80)),
        pygame.transform.scale(pygame.image.load('recursos/sprites/aereo/Fly (2).png'),(80,80)),
        pygame.transform.scale(pygame.image.load('recursos/sprites/aereo/Shoot (1).png'),(80,80)),
        pygame.transform.scale(pygame.image.load('recursos/sprites/aereo/Shoot (2).png'),(80,80)),
        pygame.transform.scale(pygame.image.load('recursos/sprites/aereo/Shoot (3).png'),(80,80)),
        pygame.transform.scale(pygame.image.load('recursos/sprites/aereo/Shoot (4).png'),(80,80)),
        pygame.transform.scale(pygame.image.load('recursos/sprites/aereo/Shoot (5).png'),(80,80))] 
    
    def ene(self):
        self.ventana.blit(pygame.transform.flip(self.caminar_ene[self.cuentaPasose//1],True,False), (self.px, self.py))
        self.px -= self.velo-1
        # self.velo += random.randint(0,2)
        # print(self.velo)
        # if self.velo > 30:
        #     self.velo = 15
        # print(self.velo)
        self.cuentaPasose = self.cuentaPasose + 1
        # print(self.cuentaPasose)
        if self.cuentaPasose > 3:
            self.cuentaPasose = 0
        if self.px < -500:
            self.px = 1200
            self.toca += 1
            # print(self.toca)
        

    def choque_pilot(self,cir_per):
        self.cir_p = pygame.draw.circle(self.ventana,(0,0,255),(self.px+40,self.py+50),20)
        # print("mx: ",self.px)
        # print("my: ",self.py)
        if cir_per.colliderect(self.cir_p):
            return True

        

            
            
           


