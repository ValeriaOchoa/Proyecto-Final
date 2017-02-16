import sys, pygame
from time import clock
from Tkinter import *
import Util 
import Personajes
import Escenario

#Tamaño de la ventana
WIDTH = 960##Ancho
HEIGHT = 480##largo

global puntaje,ventana,v2
puntaje= 1
ventana = Tk() ## ventana de presentacion
v2 = Toplevel(ventana)## crea una nueva ventana a partir de la ventana principal

final=False

##Funcion para inicializar todos los valores neccesario en nuestro juego como son la ventana de python, tamaÃ±o y el objeto del tiempo
def Initialize():
    global clock, screen, nivel#Asignamos las variables globales
    pygame.init() # inicializo el modulo   
    screen = pygame.display.set_mode((WIDTH, HEIGHT))#Le damos dimensiones a la pantalla del juego 
    pygame.display.set_caption("Super Mario Bros")# Titulo de la Ventana
    clock = pygame.time.Clock()#Creamos un objeto Clock que puede ser usado para gestionar el tiempo o la velocidad del juego

##Funcion para cargar el contenido necesario
def LoadContent():
    global mario, nivel,fondo, enemigos,perdiste,ganaste#Asignamos las variables globales
    mario = Personajes.Mario()#Accedemos a la clase de mario
    nivel= Escenario.Mapa()##Carga todo los componente para escenario llamando al archivo scenario y la clase mapa
    nivel.cargarMapa("Nivel1")##Cargamos el mapa
    fondo = Util.imagen("images/clouds.png", False, True)##Cargamos un fonde de nuves
    perdiste= Util.imagen("images/perdiste.png",False,True)
    perdiste = pygame.transform.scale(perdiste, (960, 480))
    ganaste= Util.imagen("images/mario_win.jpeg",False,True)
    ganaste= pygame.transform.scale(ganaste, (960, 480))
    enemigos=[]##Declaramos un arreglo
    enemigos.append(Personajes.Enemy("goomba",250,True))##Creamos enemigos y mandamos a llamr a la clase enemigo    
    enemigos.append(Personajes.Enemy("koopa",500,True))#Lo que enviamos es la posicion del enemigo la posicion en el mapa en el eje de las cordenadas y si va a estar activo o pasivo 
    enemigos.append(Personajes.Enemy("goomba",750))    
    enemigos.append(Personajes.Enemy("koopa",1000))
    enemigos.append(Personajes.Enemy("goomba",1250))   
    enemigos.append(Personajes.Enemy("koopa",1500))

def Updates():
    global mario
    Util.teclado(mario,nivel, WIDTH)##Revisamos el teclado
        
    Util.colision(mario, enemigos)

def Draw():
    global time, nivel,hecho#Variables globales
    nivel._posfondo-=0.3
    screen.blit(fondo,(nivel._posfondo,0))
    for i in range(nivel._MapaH ):##Creamos un buble for anidado para recorrer la matriz de las posiciones de nuestras imagenes para que vaya avanzando de 32 en 32 el mapa
        for j in range(nivel._MapaW):
            pos=nivel._matrizMapa[i][j]-1
            screen.blit(nivel._mapaImagenes[pos],(j*32+nivel._postile,i*32) )
        
    #Dibujar Mario
    if mario._vida==True:#Si mario aun no colisiona con los enemigos
        if mario._salto==False:##Si esta saltando
            if mario._direc==True:##Si esta en alguna direccion derecha para que tenga el efeto que se esta moviendo
                screen.blit(mario.imagenMario(),(mario._posX,mario._posY))
            else:
                mario_inv=pygame.transform.flip(mario.imagenMario(),True,False);##usamos para cuadno el mario va haciia la izquierda
                screen.blit(mario_inv,(mario._posX,mario._posY))##La muestra en la pantalla
        else :        
            mario.saltar()##El mario esta saltando 
            if mario._direc==True:##Si esta con direccion hacia la izquierda 
                screen.blit(mario._images[3],(mario._posX,mario._posY))##Realiza el efecto del salto con su respectiva imagen
            else:
                mario_inv=pygame.transform.flip(mario._images[3],True,False);##Si realiza el efecto del hacia la izquierda es una imagen diferente
                screen.blit(mario_inv,(mario._posX,mario._posY))##La carga en la pantalla        
        
        #Dibujar Enemigos
        for enemy in enemigos:##Un for para recorrer todo los enemigo que le pusimos al juego
            if enemy._activo==True: ##Si el enemigo esta activo estara en la pantalla  
                screen.blit(enemy.animacion(mario,WIDTH),(enemy._posX,enemy._posY))##la mostrara en la pantalla con el moviemiento se envia a mario y a with es el ancho de la pantalla    
            else:
                if mario._posAbs<=enemy._posX-500:#Si mario poscion absoluta se encuentra a 500 pixeles a el se cambia a true:
                    enemy._activo=True
    #Muerte de mario
    else:
        screen.blit(mario.muerteMario(),(mario._posX,mario._posY))
        if mario._posY>=455:

            if final==True:
                screen.fill(0)#Pintar toda la pantalla en negro
                screen.blit(ganaste,(0,0))
                hecho=False
                sonido= pygame.mixer.Sound("Sonidos/gana.wav")
                sonido.play();
            elif final==False:
                screen.fill(0)#Pintar toda la pantalla en negro
                screen.blit(perdiste,(0,0))#Pintamos la imagen de perdida
                hecho=False
                sonido= pygame.mixer.Sound("Sonidos/muertemario.wav")
                sonido.play();
             
    pygame.display.flip()#Actualizar la pantalla
  
def main():
    Initialize()##Inicializamos vari
    LoadContent()##Cargamos todo el contenido
    tiempo=60
    puntaje=0
    pun=0
    fuente1 = pygame.font.SysFont("arcade",30,True,False)
    global time,final,hecho
    pygame.mixer.music.load("Sonidos/fondo.mp3")##Cargamos sonido de fondo
    pygame.mixer.music.play(-1)##Lo repetimos indefinidaveces
    hecho = True
    while hecho == True:
        time = clock.tick(60)#Que este el 60 milisegundos 
        Updates()#Llamamos a la funcion update
        
        Draw()

        if mario._vida==False:#Si el mario no tiene al atributo vida activado se para la musica de fondo
            pygame.mixer.music.stop()
        if mario._posAbs>550 and mario._posAbs<570 and mario._posY==420:
            mario._vida=False
            
        if mario._posAbs>948 and mario._posAbs<980 and mario._posY==420:
            mario._vida=False

        if mario._vida==True:
            if mario._posAbs==1200:
                  pun=pun+auxti
                  mario._vida=False
                  final=True
            creartxt()
            grabartxt(pun)
            leertxt()
            segundos=tiempo-pygame.time.get_ticks()/1000#tomamos el tiempo que tenemos y lo restamos con los segundo
            segundos=int(segundos)##transformamos los puntos en enteros
            auxti=segundos
            if segundos<0:
               mario._vida=False
            segundos="Tiempo: "+str(segundos)##la transformamos a texto para poderla imprimir en pantalla
            contador=fuente1.render(segundos,0,(255,87,51))##Le asignamos una fuente para imprimir
           
        puntaje=pun#Igualamos los puntos aux a el puntaje
        puntaje=int(puntaje)
        puntaje="Puntaje: "+str(puntaje)##la transformamos a texto para poderla imprimir en pantalla
        puntaje=fuente1.render(puntaje,0,(255,87,51))##Le asignamos una fuente para imprimir
        pun=pun+0.1
           
        screen.blit(contador,(0,0))##Imprime el tiempo del jueg
        screen.blit(puntaje,(150,0))##Imprime el tiempo del jueg
        pygame.display.flip()##Actualizamos la pantalla

def pantalla_inicial():
    ventana.title("Super Mario Bros =)")
    canvas = Canvas(ventana,width = 1000, height= 680) ## se crea la pantalla paara la presentacion 
    fondo = PhotoImage(file = "Images/fondo_mario.gif") ## se carga a imagen 
    lblImagen = Label(ventana,image = fondo).place(x = 0, y = 0) ## imagen se transforma a label y se la coloca en el fondos
    juego = PhotoImage(file = "Images/boton-jugar.gif")## se carga a imagen
    boton_juego = Button(ventana,image = juego,command= ventana.destroy).place(x = 750, y = 330)## se carga el boton con la imagen cargada anteriormente, el comando y la posicion
    puntos = PhotoImage(file = "Images/puntaje.gif")
    boton_puntos = Button(ventana,image = puntos,command= puntajes()).place(x = 750, y = 450)
    salir = PhotoImage(file = "Images/boton-salir.gif")
    boton_salir = Button(ventana,image = salir,command= exit).place(x = 750, y = 580)

    canvas.pack()
    ventana.mainloop()

def creartxt(): ## se crea un archivo txt para guardar los puntajes
    nuevo = open('puntajes.txt','w')
    nuevo.close()
def grabartxt(pun):
    nuevo = open('puntajes.txt','a')
    nuevo.write("Puntaje:_____________" + str(pun)+"\n")
    nuevo.close()

def leertxt():
    nuevo = open('puntajes.txt','r')
    linea = nuevo.readline()
    while linea!="":
        #print linea
        linea = nuevo.readline()
    nuevo.close()
    
def puntajes():  
    v2.title("PUNTAJES")
    etiqueta = Label(v2,text="PUNTAJES",font="Arial 15 bold",
                     fg = "purple4", ## color de la fuente
                     bg= "White") ## fondo de la etiqueta
    etiqueta.grid(row=1,column=1)
    archivo_puntajes = open('puntajes.txt') ## abre el archivo
    puntajes = archivo_puntajes.read() ## lee el archivo 

    etiqueta2 = Label(v2,text = puntajes,font="Arial 14 bold", ## texto
                      fg="Black") ## color de texto
    etiqueta2.grid(row = 2,column = 1) ## ubicacion de la etiqueta
    
    boton_atras = Button(v2,text="Atrás",font="Calibri 15 bold", ## creacion de un boton atras para volver a la pantalla de presentación
                    fg = "white", ## color de la fuente
                    bg= "magenta3", ## color del fondo
                    command = v2.destroy)
    boton_atras.grid(row=3,column=1)## ubicacion del boton
    
pantalla_inicial()
main()##Mandamos a llamar la funcion principla
