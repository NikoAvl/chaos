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
        self.velocidad = [0,0] 

        

    
        

    def gravedad_planeta(self,masa,distancia):
        G = (6.67*math.e-11*(6.68*math.e-12)**3/(5*math.e-31*(1.15*math.e-5)**2))
        gravedad = G*(masa/(distancia**2)) #elevo la masa para que no sea diminuta 
        return gravedad
    
    def aplicar_fuerza_gravitatoria(self,particula_dos):
        distancia_x = particula_dos.posicion[0] - self.posicion[0] #(x₂-x₁)²
        distancia_y = particula_dos.posicion[1] - self.posicion[1] #(y₂-y₁)²
        distancia = max(math.sqrt(distancia_x**2 + distancia_y**2), 1) # √(x₂-x₁)² + (y₂-y₁)²
        direccion = [distancia_x / distancia, distancia_y    / distancia] 

        fuerza_gravitatoria = self.gravedad_planeta(particula_dos.masa, distancia)

        self.velocidad[0] += direccion[0] * fuerza_gravitatoria / self.masa
        self.velocidad[1] += direccion[1] * fuerza_gravitatoria / self.masa
        print(self.velocidad)

    def actualizar_posicion(self):
        # Actualizar la posición según la velocidad
        self.posicion[0] += self.velocidad[0]
        self.posicion[1] += self.velocidad[1]

        

    def mostrar(self):
        pygame.draw.circle(screen, self.color, (int(self.posicion[0]),int(self.posicion[1])),self.radio,1)
        





#SCREEN
colors = [(0,0,0),(255,96,208),(0,32,255),(0,192,0)]
width = 600
height = 600
size = (width,height)
screen = pygame.display.set_mode(size=size)
tiempo = pygame.time.Clock()
timer_res = pygame.TIMER_RESOLUTION
dt = 0.1

particulas = []
posicion = [0,0]
radio = 0
masa = 0

for particula in range(2):
    posicion = [random.randint(10, 590), random.randint(10, 590)]
    radio = random.randint(2,20)
    masa =  random.randint(10, 50)
    color = random.randint(0,3)
    particulas.append(Particula(posicion,radio,masa,colors[color]))


running  = True
t = 0
while running:
    

    for particula in particulas:
        for particula_dos in particulas:
            if particula_dos != particula:
                particula.aplicar_fuerza_gravitatoria(particula_dos)
    
    for particula in particulas:
        particula.actualizar_posicion()

    screen.fill((255,255,255))

    for particula in particulas:
        particula.mostrar()  # Dibuja cada partícula

    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    tiempo.tick(60)
    t += dt
    pygame.display.flip()


pygame.quit()


    