import pygame, sys
from pygame.locals import *
import Personajes
clock = pygame.time.Clock()

fin=0
def imagen(filename, transparent=False,expandir=False):##Enviamos para imagen,si no se especifica la tranparencia es falso y si la expandimos o no
        try: image = pygame.image.load(filename)##si tenemos algun error al cargar de archivos Filename = es la ruta de nuestro archivo 
        except pygame.error, message:##si existe erro con el algun mensaje a consola
                raise SystemExit, message
        image = image.convert()##va a convertir la imagen a formato interno de python para que sea mas factible para el interprete manejar a la imagen
        if transparent:## si transparente = true
                color = image.get_at((0,0))##obtener el color que se encuentra en la parte superior izquierda
                image.set_colorkey(color, RLEACCEL)## no se va  a mostrar el color 
        if expandir:
            image=pygame.transform.scale2x(image)#La hacemos crecer mas la imagen    
        return image

#mitad=False

def teclado(mario,nivel,WIDTH):
    teclado = pygame.key.get_pressed()##obtenemos la teclas que presionan
    global mitad, blink_posY ##Variables globales  
    if mario._vida==True:##Preguntamos si mario aun sigue vivo
        if teclado[K_UP] and mario._salto==False: ##Si preciona la tecla de arriba
            salto = pygame.mixer.Sound("Sonidos/Salto.wav")##Sonido salto
            salto.play()
            if mario._posX<WIDTH/2+30:
                mario._salto=True##Para cuando baje
                mario._subida=True##Hacer para abajo
            else:
                mario._salto=True
                mario._posX-=2##La posicion en x disminuye en 2     
        
        if teclado[K_RIGHT]:##Si preciona la tecla de la derecha

            if mario._posX<WIDTH/2+30:
                mario._posX+=2
            else:           
                nivel._postile-=2
                nivel._posEnemy+=1
                
            mario._alto=False     
            mario._con+=1
            mario._direc=True
            mario._posAbs+=1
               
        elif teclado[K_LEFT]:##Si preciona la tecla de la izquierda
            if mario._posX<5:
               mario._con+=1
               mario._direc=False
               mario._posAbs-=1
            else:
               mario._con+=1
               mario._posX-=2
               mario._direc=False
               mario._posAbs-=1
            
        else:
            mario._frame=0##Pinte a mario parado
            mario._alto=True##Cuando mario no se mueve
            
        if mario._con>=6:  ##Para qeu cambie de dibujo y se muestre el efecto que esta caminando      
            mario._frame+=1
            mario._con=0
            
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def colision(mario,enemigos):
    if mario._posY==400:##Vefica si el mario esta en el suelo
        for i in range(len(enemigos)):
            if mario._posX+32>enemigos[i]._posX and mario._posX-32<enemigos[i]._posX:
                enemigos[i]._activo=False
                
    elif mario._posY==420:#Verifica cual el mario esta a una determinada distastnacia del suelo
        for i in range(len(enemigos)):
            if mario._posX+32>enemigos[i]._posX and mario._posX-32<enemigos[i]._posX and enemigos[i]._activo==True:
                mario._vida=False
                mario._posMuerte=mario._posX
                return True
    return False
