#Juan Carlos Espinoza Porlles 2K Proyecto laberinto
import pygame
import sys

pygame.init()

# 1 es pared, 0 camino, 2 princesa
MATRIZ = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Pantalla
celda = 60 # tamaño de cada cuadro para que se vea mejor
ancho = 10 * celda
alto = 10 * celda
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Mario rescatando a la Princesa")

# Carga de imagenes
mario_img = pygame.image.load("mario.jpg")
mario_img = pygame.transform.scale(mario_img, (celda, celda))

princesa_img = pygame.image.load("princesa.jpg")
princesa_img = pygame.transform.scale(princesa_img, (celda, celda))

# Cargamos el la pared del laberinto (labrillo)
ladrillo_img = pygame.image.load("bloqueladrillo.png")
ladrillo_img = pygame.transform.scale(ladrillo_img, (celda, celda))

final_img = pygame.image.load("marioyprincesa.jpg")
# Portada del final
final_img = pygame.transform.scale(final_img, (400, 400))

# Mario inicio
mario_x = 0
mario_y = 1

ganaste = False
jugando = True

# Bucle para que no se cierre el programa
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
            pygame.quit()
            sys.exit()
        
        # Movimiento 
        if event.type == pygame.KEYDOWN and ganaste == False:
            if event.key == pygame.K_UP:
                if MATRIZ[mario_y - 1][mario_x] != 1:
                    mario_y = mario_y - 1
            if event.key == pygame.K_DOWN:
                if MATRIZ[mario_y + 1][mario_x] != 1:
                    mario_y = mario_y + 1
            if event.key == pygame.K_LEFT:
                if mario_x > 0: # para que no se salga
                    if MATRIZ[mario_y][mario_x - 1] != 1:
                        mario_x = mario_x - 1
            if event.key == pygame.K_RIGHT:
                if mario_x < 9:
                    if MATRIZ[mario_y][mario_x + 1] != 1:
                        mario_x = mario_x + 1

            # Lleda al final (Princesa)
            if MATRIZ[mario_y][mario_x] == 2:
                ganaste = True

    pantalla.fill((255, 255, 255)) # fondo blanco
    
    if ganaste == False:
        # Laberinto
        for f in range(10):
            for c in range(10):
                x = c * celda
                y = f * celda
                if MATRIZ[f][c] == 1:
                    # Cada 1 sera el ladrillo del laberinto
                    pantalla.blit(ladrillo_img, (x, y)) 
                if MATRIZ[f][c] == 2:
                    pantalla.blit(princesa_img, (c*celda, f*celda))
        
        # Usamos blit para comer la imagen de mario y ponerla encima (esto tambien lo hacemos con los ladrillos de laberinto y otros)
        pantalla.blit(mario_img, (mario_x*celda, mario_y*celda))
    
    else:
        # Pantalla de ganar
        pantalla.blit(final_img, (100, 50))
        # Final
        mifuente = pygame.font.SysFont("Arial", 20)
        mensaje = mifuente.render("Felicidades, rescataste a la princesa", True, (255, 0, 0))
        pantalla.blit(mensaje, (150, 500))

    pygame.display.update()