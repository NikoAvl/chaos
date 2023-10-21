import turtle as tl
import math
import random
import pygame


pygame.init()

class Particula:
    def __init__(self,posicion,radio,masa,color,velocidad):
        self.posicion = posicion
        self.radio = radio
        self.color = color
        self.masa = masa
        self.velocidad = velocidad
        

        

    
        

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
    
    def rebotar(self,particula,particula_dos):
        e = 0.8 #coeficiente de restitucion 
        v1_p1_x = (e * particula.velocidad[0]) + ((1 - e) * particula_dos.velocidad[0])
        v1_p1_y = (e * particula.velocidad[1]) + ((1 - e) * particula_dos.velocidad[1])

        v2_p2_x = (e * particula_dos.velocidad[0]) + ((1 - e) * particula.velocidad[0])
        v2_p2_y = (e * particula_dos.velocidad[1]) + ((1 - e) * particula.velocidad[1])

        

        particula.velocidad[0],particula.velocidad[1] = v1_p1_x*-1,v1_p1_y*-1
        particula_dos.velocidad[0],particula_dos.velocidad[1] = v2_p2_x*-1,v2_p2_y*-1

       



        
    def actualizar_posicion(self):
        # Actualizar la posición según la velocidad
        self.posicion[0] += self.velocidad[0]
        self.posicion[1] += self.velocidad[1]
        

    def mostrar(self):
        pygame.draw.circle(screen, self.color, (int(self.posicion[0]),int(self.posicion[1])),self.radio,0)
        
def distancia_particulas(particula,particula_dos):
    distancia_x = (abs(particula_dos.posicion[0])) - (abs(particula.posicion[0])) #(x₂-x₁)²
    distancia_y = (abs(particula_dos.posicion[1])) - (abs(particula.posicion[1])) #(y₂-y₁)²
    distancia = max(math.sqrt((distancia_x**2) + (distancia_y**2)), 1) # √(x₂-x₁)² + (y₂-y₁)²
    
    return distancia





#SCREEN
colors = [(0,0,0),(255,96,208),(0,32,255),(0,192,0)]
width = 1200
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

for particula in range(3):
    posicion = [random.randint(0, 600), random.randint(0, 600)]
    radio = random.randint(10,40)
    masa =  radio**4
    color = random.randint(0,3)
    velocidad = [random.uniform(-0.3,0.3), random.uniform(-0.3,0.3)]
    print(velocidad[0],velocidad[1])
    particulas.append(Particula(posicion,radio,masa,colors[color],velocidad))



running = True
t = 0
colisiones = set()  

while running:
    # Limpiar el conjunto de colisiones recientes al comienzo de cada ciclo
    colisiones.clear()

    # Aplicar la fuerza gravitatoria
    for particula in particulas:
        for particula_dos in particulas:
            if particula_dos != particula:
                particula.aplicar_fuerza_gravitatoria(particula_dos)

    # Calcular colisiones y aplicar rebotes
    for i in range(len(particulas)):
        for j in range(i + 1, len(particulas)):
            particula = particulas[i]
            particula_dos = particulas[j]
            distancia = distancia_particulas(particula, particula_dos)

            if distancia < particula.radio + particula_dos.radio:
                # Las partículas están colisionando
                if (particula, particula_dos) not in colisiones:
                    particula.rebotar(particula, particula_dos)
                    colisiones.add((particula, particula_dos))

    # Actualizar la posición de las partículas
    for particula in particulas:
        particula.actualizar_posicion()

    screen.fill((255, 255, 255))

    for particula in particulas:
        particula.mostrar()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tiempo.tick(60)
    t += dt
    pygame.display.flip()

pygame.quit()