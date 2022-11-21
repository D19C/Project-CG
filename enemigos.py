import pygame
import random


class Enemi():
    def __init__(self,ventana,px,py,bandera,velo,cuentaPasose,toca) -> None:
        self.ventana=ventana
        self.px = px
        self.py = py
        self.velo = velo
        self.bandera = bandera
        self.cuentaPasose = cuentaPasose
        self.toca = toca
        self.caminar_ene = [pygame.transform.scale(pygame.image.load('recursos/sprites/female_ene/Walk (1).png'),(100,100)),
        pygame.transform.scale(pygame.image.load('recursos/sprites/female_ene/Walk (2).png'),(100,100)),
        pygame.transform.scale(pygame.image.load('recursos/sprites/female_ene/Walk (3).png'),(100,100)),
        pygame.transform.scale(pygame.image.load('recursos/sprites/female_ene/Walk (4).png'),(100,100))] 
    
    def ene(self):
        self.ventana.blit(pygame.transform.flip(self.caminar_ene[self.cuentaPasose//1],True,False), (self.px, self.py))
        self.px -= self.velo-1
        # self.velo += random.randint(0,4)
        # print(self.velo)
        # if self.velo > 25:
        #     self.velo = 10
        # print(self.velo)
        self.cuentaPasose = self.cuentaPasose + 1
        # print(self.cuentaPasose)
        if self.cuentaPasose > 3:
            self.cuentaPasose = 0
        if self.px < -100:
            self.px = 1100
            self.toca += 1
            # print(self.toca)
        

    def choque(self,cir_per):
        self.cir_z = pygame.draw.circle(self.ventana,(0,0,255),(self.px+40,self.py+50),20)
        # print("mx: ",self.px)
        # print("my: ",self.py)
        if cir_per.colliderect(self.cir_z):
            return True

        

            
            
           


