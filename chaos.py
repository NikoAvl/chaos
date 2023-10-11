import turtle as tl
import math
import random
import pygame


pygame.init()

class Particula:
    def __init__(self,posicion,radio,masa,color):
        self.posicion = posicion
        self.radio = radio
        self.color = color
        self.masa = masa
        self.velocidad_inicial = 0



    def mostrar(self):
        pygame.draw.circle(screen, self.color, (int(self.posicion[0]),int(self.posicion[1])),self.radio,1)
        
    
    def gravedad_planeta(self):
        gravedad = (6.672*(10**(-11)))*(masa/(radio**2))
        return gravedad
    
    def calcular_posicion():
        pass
        





#SCREEN
colors = [(0,0,0),(255,96,208),(0,32,255),(0,192,0)]
width = 600
height = 600
size = (width,height)
screen = pygame.display.set_mode(size=size)
tiempo = pygame.time.Clock()
timer_res = pygame.TIMER_RESOLUTION
dt = 0.0065

particulas = []
posicion = [0,0]
radio = 0
masa = 0

for particula in range(50):
    posicion = [random.randint(10, 590), random.randint(10, 590)]
    radio = random.randint(2,20)
    masa =  random.randint(0, 5)
    color = random.randint(0,3)
    particulas.append(Particula(posicion,radio,masa,colors[color]))


running  = True
t = 0
while running:
    screen.fill((255,255,255))

    for particula in particulas:
        particula.mostrar()
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    tiempo.tick(180)
    t += dt
    pygame.display.flip()



    