import pygame
from pygame.locals import *
import sys


pygame.init()


shirinanaekran = 1000
visochinanaekran = 600
cvqtnabg = (103, 191, 126)
fps = 60

screen = pygame.display.set_mode((shirinanaekran, visochinanaekran))
pygame.display.set_caption("tenis")
clock = pygame.time.Clock()

raketa_shirinanaekran = 10
raketa_visochinanaekran = 100
cvqtnaraketa = (0, 0, 0)
burzina_raketa = 7

raketa1 = pygame.Rect(50, visochinanaekran // 2 - raketa_visochinanaekran // 2, raketa_shirinanaekran, raketa_visochinanaekran)
raketa2 = pygame.Rect(shirinanaekran - 50 - raketa_shirinanaekran, visochinanaekran // 2 - raketa_visochinanaekran // 2, raketa_shirinanaekran, raketa_visochinanaekran)


radiusnatopka = 20
cvqtnatopka = (0, 0, 0)
burzinanatopka_x = 4
burzninanatopka_y = 4




topka = pygame.Rect(shirinanaekran // 2 - radiusnatopka // 2, visochinanaekran // 2 - radiusnatopka // 2, radiusnatopka, radiusnatopka)
topka_burzina_x = burzinanatopka_x
topka_burzina_y = burzninanatopka_y


cvqtnachisla = (0, 0, 0)
goleminanabukvi = 36

igrach1_tochki = 0
igrach2_tochki = 0

font = pygame.font.Font(None, goleminanabukvi)
rezultat_i1 = font.render(str(igrach1_tochki), True, cvqtnachisla)
rezultat_i2 = font.render(str(igrach2_tochki), True, cvqtnachisla)
rezultat_narisuvan_i1 = rezultat_i1.get_rect()
rezultat_narisuvan_i2 = rezultat_i2.get_rect()
rezultat_narisuvan_i1.center = (shirinanaekran // 4, 50)
rezultat_narisuvan_i2.center = (3 * shirinanaekran // 4, 50)


def rezultat_updeit():
  
    global rezultat_i1, rezultat_i2, rezultat_narisuvan_i1, rezultat_narisuvan_i2
  
    rezultat_i1 = font.render(str(igrach1_tochki), True, cvqtnachisla)
    rezultat_i2 = font.render(str(igrach2_tochki), True, cvqtnachisla)

    rezultat_narisuvan_i1 = rezultat_i1.get_rect()
    rezultat_narisuvan_i2 = rezultat_i2.get_rect()
    
    rezultat_narisuvan_i1.center = (shirinanaekran // 4, 50)
    rezultat_narisuvan_i2.center = (3 * shirinanaekran // 4, 50)


def novatopka():
    topka.center = (shirinanaekran // 2, visochinanaekran // 2)
    topka_burzina_x = burzinanatopka_x
    topka_burzina_y = burzninanatopka_y


while True:

    for event in pygame.event.get():
        if event.type == QUIT:

            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()


    if keys[K_w] and raketa1.y > 0:
        raketa1.y -= burzina_raketa
    
    if keys[K_s] and raketa1.y < visochinanaekran - raketa_visochinanaekran:
        raketa1.y += burzina_raketa
    
    if keys[K_UP] and raketa2.y > 0:
        raketa2.y -= burzina_raketa
    
    if keys[K_DOWN] and raketa2.y < visochinanaekran - raketa_visochinanaekran:
        raketa2.y += burzina_raketa

    if keys[K_1]:
        topka_burzina_x = 1
        topka_burzina_y = 1
    
    if keys[K_2]:
        topka_burzina_x = 2
        topka_burzina_y = 2

    if keys[K_3]:
        topka_burzina_x = 3
        topka_burzina_y = 3
    
    if keys[K_4]:
        topka_burzina_x = 4
        topka_burzina_y = 4

    if keys[K_5]:
        topka_burzina_x = 5
        topka_burzina_y = 5

    if keys[K_6]:
        topka_burzina_x = 6
        topka_burzina_y = 6

    if keys[K_7]:
        topka_burzina_x = 7
        topka_burzina_y = 7

    if keys[K_8]:
        topka_burzina_x = 8
        topka_burzina_y = 8
    
    if keys[K_9]:
        topka_burzina_x = 9
        topka_burzina_y = 9

   
    topka.x += topka_burzina_x
    topka.y += topka_burzina_y

   
    if topka.colliderect(raketa1) or topka.colliderect(raketa2):
        topka_burzina_x *= -1

    
    if topka.y > visochinanaekran - radiusnatopka or topka.y < 0:
        topka_burzina_y *= -1

    
    if topka.x > shirinanaekran:
        igrach1_tochki += 1
        novatopka()
   
   
        rezultat_updeit()
    elif topka.x < 0:
        igrach2_tochki += 1
      
        novatopka()
        rezultat_updeit()


    
    screen.fill(cvqtnabg)
    pygame.draw.rect(screen, cvqtnaraketa, raketa1)
    pygame.draw.rect(screen, cvqtnaraketa, raketa2)
    pygame.draw.ellipse(screen, cvqtnatopka, topka)
    pygame.draw.aaline(screen, cvqtnaraketa, (shirinanaekran // 2, 0), (shirinanaekran // 2, visochinanaekran))
    screen.blit(rezultat_i1, rezultat_narisuvan_i1)
    screen.blit(rezultat_i2, rezultat_narisuvan_i2)

    
    pygame.display.flip()
    clock.tick(fps)
