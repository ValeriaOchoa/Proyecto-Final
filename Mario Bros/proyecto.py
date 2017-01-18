import pygame 
from pygame.locals import*

#La funcion principal main
def main():
    pygame.init() # inicializo el modulo
    #Le damos dimensiones a la pantalla del juego 
    pantalla=pygame.display.set_mode((1920,1080))
    pygame.display.set_caption("Modulo Music")#sonido
    fondo = pygame.image.load("fondo.png")##imagen del fondo
    Imagen = pygame.image.load("Mario.png")
    coordX = 300
    coordY = 200
    Coordenadas = (coordX, coordY)
    posXfondo = 0
    posYfondo = 0
    Blanco = (253,254,254) ## color de fondo
    pygame.display.set_caption("Mario Bros") # Titulo de la Ventana
    fuente1 = pygame.font.SysFont("Arial",20,True,False)
    info=fuente1.render("Tiempo",0,(25,25,25))##Guarda la informacion para que infrima la palabra de tiempo
    salir=False##lo inicializamos en false para que cumpla la funcion del while
    reloj1=pygame.time.Clock()
    pygame.mixer.music.load("Mario.mp3")#llamada a la musica
    pygame.mixer.music.play(1)
    blanco=(255,255,255)#crear el color blanco
    tiempo=180##el tiempo del juego que va aser de 3 minutos para pasar el nivle
    incrementoX = 0
    incrementoY = 0
    for eventos in pygame.event.get(): ## SONIDO
        if eventos.type == pygame.QUIT:
            exit()
        if eventos.type == pygame.KEYDOWN:
            if eventos.key == pygame.K_p:
                pygame.mixer.music()
        reloj1.tick(0.5)
    while salir!=True:
       
##        pygame.display.update()
       # Manejador de eventos
        for evento in pygame.event.get():
        # Pulsación de la tecla escape
           if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    sys.exit()
                elif evento.key == pygame.K_RIGHT:
                    incrementoX = 5
                elif evento.key == pygame.K_DOWN:
                    incrementoY = 5
                elif evento.key == pygame.K_LEFT:
                    incrementoX = -5
                elif evento.key == pygame.K_UP:
                    incrementoY = -5
           if evento.type == pygame.KEYUP:
               incrementoX = 0
               incrementoY = 0

        coordX = coordX + incrementoX
        coordY = coordY + incrementoY

        Coordenadas = (coordX, coordY)



        
        #recorro todos los eventos producidos
        for event in pygame.event.get():
            # si el evento es cerrar la ventana 
            if event.type == pygame.QUIT:
                salir=True
        reloj1.tick(20)#operacion para que todo corra a 20fpp
        pantalla.fill(blanco)##muestra la pantalla en blano
        pantalla.blit(info,(5,5))##Imprimiir la palabra tiempo en panatalla
        segundos=tiempo-pygame.time.get_ticks()/1000
        segundos=int(segundos)##transformamos la imagen a int
        segundos=str(segundos)##la transformamos a texto para poderla imprimir en pantalla
        contador=fuente1.render(segundos,0,(0,0,230))##imprimimos nuestro contador de tiempo
        pantalla.fill(Blanco)
        pantalla.blit(fondo,(posXfondo,posYfondo)) ## posicion del fondo
        pantalla.blit(contador,(300,5))##Imprime el tiempo del juego
        pantalla.blit(Imagen, Coordenadas) 
        pygame.display.update() #actualizo el display
           
    pygame.quit()##sale de la ventana


    
main() 

