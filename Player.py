import pygame
from pygame.locals import *
import enemigos
import piloto
import numpy as np
from PIL import Image
import sys
import os


myDir = os.getcwd()
sys.path.append(myDir) 
class Jugar:
    def __init__(self,x,px,py,ancho,velocidad):
        self.x = x
        self.px = px
        self.py = py
        self.ancho = ancho
        self.velocidad = velocidad

    def main(self):
        #print(I.size)
        I = Image.open("recursos/fondos/Jugar/jugarP.png")
        pygame.init()
        principal_img = pygame.image.load("recursos/fondos/Jugar/jugarP.png")
        ventana = pygame.display.set_mode(I.size)
        ventana.blit(principal_img,(0,0))
        pygame.display.set_caption('Play')
        pygame.display.update()
        clock=pygame.time.Clock()
        Jugar.personaje(ventana,self)

    def personaje(ventana,self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                    ins = enemigos.Enemi(ventana,900,340,True,10,0,0) 
                    ins2 = piloto.Pilot(ventana,1500,178,True,10,0,0) 
                    Jugar.camina(self,ventana,ins,ins2)

    def camina(self,ventana,ins,ins2):
        caminar = [pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (1).png'),(100,100)),
				 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (2).png'),(100,100)),
				 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (3).png'),(100,100)),
				 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (4).png'),(100,100)),
				 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (5).png'),(100,100)),
				 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (6).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (7).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (8).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (9).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (10).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (11).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (12).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (13).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (14).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (15).png'),(100,100))]

        salta = [pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (1).png'),(100,100)),
				 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (2).png'),(100,100)),
				 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (3).png'),(100,100)),
				 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (4).png'),(100,100)),
				 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (5).png'),(100,100)),
				 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (6).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (7).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (8).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (9).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (10).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (11).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (12).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (13).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (14).png'),(100,100)),
                 pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (15).png'),(100,100))]
        

        camina = Jugar(0,94,335,30,5)

        



        # Control de FPS
        reloj = pygame.time.Clock()

        # Variables salto
        salto = False
        # Contador de salto
        cuentaSalto = 10

        # Variables dirección
        izquierda = False
        derecha = False

        # Pasos
        cuentaPasos = 0
        # Movimiento
        def recarga_pantalla(cuentaPasos):
            fondo = pygame.image.load("recursos/fondos/Jugar/jugar.png")
            # Fondo en movimiento
            x_relativa = camina.x % fondo.get_rect().width
            ventana.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
            if x_relativa < 999:
                ventana.blit(fondo, (x_relativa, 0))
            camina.x -= 5
            

            # Movimiento a la derecha
            if derecha:
                ventana.blit(caminar[cuentaPasos//1], (camina.px, camina.py))
            # Movimiento a la izquierda
            elif izquierda:
                ventana.blit(pygame.transform.flip(caminar[cuentaPasos//1],True,False), (camina.px, camina.py))
            elif derecha and izquierda == False and salto == False :
                ventana.blit(caminar[cuentaPasos // 1], (camina.px, camina.py))

        ejecuta = True

        # Bucle de acciones y controles
        
        while True:
            cir_per = pygame.draw.circle(ventana,(0,0,255),(camina.px+40,camina.py+50),20)
            ins.ene()
            ins2.ene()
            # FPS
            reloj.tick(20)
            # Bucle del juego
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    vent(0)

            # Opción tecla pulsada
            keys = pygame.key.get_pressed()
            # Contador de pasos
            if cuentaPasos + 1 >= 15:
                cuentaPasos = 0
            # Tecla - Moviemiento a la izquierda
            elif keys[pygame.K_LEFT] and camina.px > camina.velocidad:
                camina.px -= camina.velocidad-1
                izquierda = True
                derecha = False
                cuentaPasos += 1

            # Tecla - Moviemiento a la derecha
            elif keys[pygame.K_RIGHT] and camina.px < 900 - camina.velocidad - camina.ancho:
                camina.px += camina.velocidad
                izquierda = False
                derecha = True
                cuentaPasos += 1

            elif keys[pygame.K_ESCAPE]:
                vent(0)

            # Personaje quieto
            else:
                izquierda = False
                derecha = True
                cuentaPasos += 1

            # Tecla SPACE - Salto
            if not salto:
                if keys[pygame.K_UP]:
                    salto = True
                    izquierda = False
                    derecha = False
                    cuentaPasos = 0
                    
            else:
                if cuentaSalto >= -10:
                    camina.py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
                    ventana.blit(salta[cuentaPasos // 1], (camina.px, camina.py))
                    cuentaSalto -= 1
                else:
                    cuentaSalto = 10
                    salto = False
            
            # print("bx: ",camina.px)
            # print("by: ",camina.py)
            if ins.choque(cir_per) == True:
                vent(0)
            if ins2.choque_pilot(cir_per) == True:
                vent(0)
            # Actualización de la ventana
            pygame.display.update()
            #Llamada a la función de actualización de la ventana
            recarga_pantalla(cuentaPasos)



        


def credit(self):
    I = Image.open("recursos/fondos/creditos/creditos.png")
    #print(I.size)while True:
    pygame.init()
    ventana = pygame.display.set_mode(I.size)
    principal_img = pygame.image.load("recursos/fondos/creditos/creditos.png")
    ventana.blit(principal_img,(0,0))
    pygame.display.set_caption('Creditos')
    pygame.display.update()
    clock=pygame.time.Clock()
    while True:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                pygame.quit()
            if eventos.type==pygame.MOUSEBUTTONDOWN:
                (x,y) = pygame.mouse.get_pos()
                if x>=987 and y>=580 and x<=1294 and y<=734:
                    vent(self)

def vent(self):
    I = Image.open("recursos/fondos/principal/fondo.png")
    #print(I.size)
    pygame.init()
    ventana = pygame.display.set_mode(I.size)
    principal_img = pygame.image.load("recursos/fondos/principal/fondo.png")
    ventana.blit(principal_img,(0,0))
    pygame.display.set_caption('Game plataform')
    pygame.display.update()
    clock=pygame.time.Clock()
    while True:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                pygame.quit()
            if eventos.type==pygame.MOUSEBUTTONDOWN:
                (x,y) = pygame.mouse.get_pos()
                if x>=987 and y>=580 and x<=1294 and y<=734:
                    sys.exit()
                if x>=558 and y>=580 and x<=867 and y<=734:
                    credit(self)
                if x>=104 and y>=580 and x<=408 and y<=734:
                    Jugar.main(self)




