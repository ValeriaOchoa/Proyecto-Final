import sys, pygame
from pygame.locals import *
from time import clock
 
#Tamaño  la pantalla
WIDTH = 900
HEIGHT = 500

MposX =300
MposY =318

cont=6
direc=True
i=0
 
bajada=False
salto = False
tiempo=180##el tiempo del juego que va aser de 3 minutos para pasar el nivle


def Initialize():
    global screen, clock,xixf,Rxixf
    pygame.init()    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mario")
    clock = pygame.time.Clock()
    xixf={}
    Rxixf={}
    xixf[0]=(0,0,20,41)
    xixf[1]=(22,0,25,41)
    xixf[2]=(47,0,25,41)
    xixf[3]=(73,0,20,41)
    xixf[4]=(93,0,27,41)
    xixf[5]=(120,0,27,41)
    Rxixf[0]=(122,0,22,41)
    Rxixf[1]=(96,0,25,41)
    Rxixf[2]=(74,0,22,41)
    Rxixf[3]=(50,0,23,41)
    Rxixf[4]=(24,0,26,41)
    Rxixf[5]=(0,0,25,41)
   
 
def LoadContent():
    global fondo, mario,mario_inv,enemig 
    fondo = imagen("imagenes/fondo.png")            
    mario = imagen("imagenes/sprites_mario.png",True)  
    mario_inv=pygame.transform.flip(mario,True,False);
    fondo = pygame.transform.scale(fondo, (1000, 400))
    
 
def Updates():   
    teclado()    
    #Escenario
    sprite_M()  
    #Enemigo()
    #Coliciones()
    

def Draw():
    global salto,salto_Par, salto,bajada_Par,bajada
    screen.blit(fondo, (0, 0))
    global MposX,MposY
    if direc==True and salto==False :
        screen.blit(mario, ( MposX, MposY),(xixf[i]))
   
    if direc==False and salto==False :
        screen.blit(mario_inv, ( MposX, MposY),(Rxixf[i]))
       
       
       #salto normal y Parabolico
    if salto==True:            
           
        if direc==True:
            screen.blit(mario, ( MposX, MposY),(xixf[4]))
        if direc==False:
            screen.blit(mario_inv, ( MposX, MposY),(Rxixf[4]))  
           
        if bajada==False:
            MposY-=4              
               
        if bajada==True:
            MposY+=4              
           
        if MposY<=186:
            bajada=True
           
        if MposY>=318:
            bajada=False
            salto=False
        #==============================  

    
    #pygame.display.flip()
   
#=================IMAGEN====================================
def imagen(filename, transparent=False):##Enviamos para imagen,si no se especifica la tranparencia es falso
        try: image = pygame.image.load(filename)##si tenemos algun error al cargar de archivos Filename = es la ruta de nuestro archivo 
        except pygame.error as message:##si existe erro con el algun mensaje a consola
                raise SystemExit(message)
        image = image.convert()##va a convertir la imagen a formato interno de python para que sea mas factible para el interprete manejar a la imagen
        if transparent:## si transparente = true
                color = image.get_at((0,0))##obtener el color que se encuentra en la parte superior izquierda
                image.set_colorkey(color, RLEACCEL)## no se va  a mostrar el color 
        return image
 
#======================TECLADO===================================
def teclado():
    global cont, direc,salto,MposX
    teclado = pygame.key.get_pressed()
    if teclado[K_UP]:
       salto=True
       sonido= pygame.mixer.Sound("Sonidos/salto.wav")
       sonido.play();
       
       
    if teclado[K_RIGHT]:
        if MposX<=810:
            MposX+=2
        cont+=1
        direc=True
  
           
        
    elif teclado[K_LEFT]:
        if MposX>10:
            MposX-=2
            print(MposX)
        cont+=1
        direc=False
     
    else :
         cont=6
         
    # Cerrar la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
         
#===================SPRITE===============================
def sprite_M():
    global cont  
    p=6
    global i
    if cont==p:
        i=0
    if cont==p*2:
        i=1
    if cont==p*3:
        i=2
    if cont==p*4:
        i=3
    if cont==p*5:
        i=4
    if cont==p*6:
       i=5
       cont=0

    
def main():
    Initialize()
    LoadContent()
    pygame.mixer.music.load("Sonidos/Mario.mp3")#llamada a la musica
    pygame.mixer.music.play(-1)
    enemigos=[]
    enemigos.append(250)
    fuente1 = pygame.font.SysFont("Arial",20,True,False)
    vidas=3
    puntaje=1

    while True:
        time = clock.tick(60)
        Updates()
        Draw()
        LoadContent()
        
        segundos=tiempo-pygame.time.get_ticks()/1000
        segundos=int(segundos)##transformamos la imagen a int
        segundos="Timpo: "+str(segundos)##la transformamos a texto para poderla imprimir en pantalla
        contador=fuente1.render(segundos,0,(0,0,230))##imprimimos nuestro contador de tiempo
        vid="Vidas: "+str(vidas)
        vids=fuente1.render(vid,0,(0,0,230))
        puntaje=puntaje+0.1
        ##puntaje=int(puntaje)
        punt="Puntaje: "+str(puntaje)
        punts=fuente1.render(punt,0,(0,0,230))
        screen.blit(vids,(100,5))##Imprime el tiempo del jueg
        screen.blit(contador,(0,5))##Imprime el tiempo del jueg
        screen.blit(punts,(200,5))##Imprime el tiempo del jueg

        pygame.display.flip()
        
 
main()
