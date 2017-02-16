# -*- coding: cp1252 -*-
import sys, pygame
class Mario(object):
    _posX=0##Posicion en x
    _posY=420##Posicion en y
    _frame=0##El frame va
    _images=[]##Todos los sprites de mario que se utilizaran para que se mueva la imahen
    _con=0##Contador para saber en que que imagen va
    _direc=True##la direccion para saber si esta llendo para adelante o hacia atras
    _salto=False##Si va a empenzar a salto
    _subida=True#Si va subiendo el es true y si baja es igual a false
    _alto=True
    _vida=True#Si aun sigue vivo 
    _posAbs=0#Posicion absoluta de mario
    _posMuerte=0#Posicion cuando mario muer
        
    def __init__(self):
        self._conMuerte=0
        self.banderaMuerte=False#Mario esta muerto
        tileset=pygame.image.load("images/Mario y Luigi.png").convert()##Cargamos la imagen 
        color = tileset.get_at((0,0))##Obtenemos el color que se encuentra en la punta superior izquierda
        tileset.set_colorkey(color)##Lo establecemos como color transparente
        self._images.append(tileset.subsurface((1,17,16,16)))##Agregados una parte de la imagen donde se encuentra el moviemientos
        self._images.append(tileset.subsurface((18,17,16,16)))        
        self._images.append(tileset.subsurface((35,17,16,16)))
        self._images.append(tileset.subsurface((69,17,16,16)))
        ##Añadimos la muerte de mario en el array
        self._images.append(tileset.subsurface((171,17,16,16)))
        self._images.append(tileset.subsurface((188,17,16,16)))
        ##Lo que realizar es hacer la imagen mas grande a todo el array de imagenes lo va duplicar
        for i in range(len(self._images)):
            self._images[i]=pygame.transform.scale2x(self._images[i])
            
    def imagenMario(self):
        if self._frame==len(self._images)-3:
            self._frame=0 
        return self._images[self._frame]        
     
    def saltar(self):
        if self._subida==True:
            self._posY-=4
            if self._direc==True:
                self._posX+=1
            else:
                self._posX-=1
            
        if self._posY<=355:
            self._subida=False
            

        if self._subida==False:
            self._posY+=4           
            if self._direc==True:
                self._posX+=1
            else:
                self._posX-=1
            
        if self._subida==False and self._posY>=420:
            self._subida=True
            self._salto=False
            self._frame=0
   
    def muerteMario(self):     
        self._conMuerte+=1##Imprime lo que parece que mario muere
        
        if self._conMuerte%8==0:
            self.banderaMuerte= not self.banderaMuerte
        
        if self.banderaMuerte==True:
            self._frame=len(self._images)-1
        else:
            self._frame=len(self._images)-2
        
        if self._posY<=455:#Lo realiza hasta llegar a 480 en Y
            self._posY=self._posY+1
        return self._images[self._frame] 

class Enemy(object):
    def __init__(self, name="goomba",pos=960,activo=False):
        self._name=name #Nombre   
        self._posX=pos   #La posiciion        
        self._posEnemy=pos                    
        self._frame=0#Elfram 
        self._images=[]#El arreglo con todas las imagenes de movimiento                 
        self._activo=activo#Si esta activo quiere decir si esta aparece en la ventana o no
        self._time=0
        self.i=0
        
        if name=="goomba":#El gomba es el buho
            self._posY=420
            self.goomba() ##si el nombre es goomba manda a llamar a goomba
            
        if name=="koopa":#Es la tortuga
            self._posY=403#Es xq es mas grande
            self.koopa()##si el nombre es goomba manda a llamar a koopa

    def goomba(self):
        self._images=[]#Tiene un array de imagenes
        tileset=pygame.image.load("images/enemies.png").convert()#manda a llamar la imagen
        color = tileset.get_at((0,0))##Obtenemos el color que se encuentra en la punta superior izquierda
        tileset.set_colorkey(color)##Lo establecemos como color transparente
        self._images.append(tileset.subsurface((4,86,16,16)))##Añadeuna seleccion de la imagen
        self._images.append(tileset.subsurface((22,86,16,16)))##Añade una seccion de la imagen
        for i in range(len(self._images)):#Hacemos que se haga mas grande la imagen
            self._images[i]=pygame.transform.scale2x(self._images[i])
   
    def animacion(self,mario,WIDTH):        
        if mario._vida==True:#Comprobamos si el mario esta vivo
            if self._name=="goomba":#Comprobamos si cual villano es 
                if self._time%18==0:#Cada vez que llega a 18 ejecuta esta porcion de codigo
                    self.i+=1
                    if self.i==2:#Para recorrer el array de los frame
                        self.i=0
                
                if mario._posX>=WIDTH/2+30 and mario._alto==False:#alto no smuestra si esta quieto o en moviemiento
                    self._posX-=3#Incrementa la velocidad de los personajes
                else:
                    self._posX-=1
                self._time+=1#El time incrementa en 1
            
            if self._name=="koopa":
                if self._time%18==0:
                    
                    self.i+=1
                    
                    if self.i==2:
                        self.i=0    
                
                if mario._posX>=WIDTH/2+30 and mario._alto==False:
                    self._posX-=3
                else:
                    self._posX-=1
                
                self._time+=1
        
                return self._images[self.i]#Se devuelve la imagen que se encuentre en el array de imagenes en la posicion i
            
        return self._images[0]#Se devuelve la imagen en posicion 0

    def koopa(self):          
        self._images=[]#Tiene un array de imagenes
        tileset=pygame.image.load("images/enemies.png").convert()#manda a llamar la imagen
        color = tileset.get_at((0,0))##Obtenemos el color que se encuentra en la punta superior izquierda
        tileset.set_colorkey(color)##Lo establecemos como color transparente
        self._images.append(tileset.subsurface((203,5,16,25)))##Añadeuna seleccion de la imagen
        self._images.append(tileset.subsurface((220,5,16,25)))##Añadeuna seleccion de la imagen      
        self._images.append(tileset.subsurface((35,17,16,25)))##Añadeuna seleccion de la imagen
        for i in range(len(self._images)):#Agrandamos la imagen
            self._images[i]=pygame.transform.scale2x(self._images[i])               
