# -*- coding: cp1252 -*-
import base64
import StringIO
import json
import gzip
import pygame
from pygame.locals import *

class Mapa(object):
    _tileH=0##Mamaño ancho del title
    _tileW=0#Ancho del mapa
    _MapaW=0#Ancho del mapa    
    _MapaH=0#Alto del mapa
    _transparentcolor=-1##Color transparente
    _matrizMapa=[]##Matriz todos lso titles
    _mapaImagenes=[]##Almacenan todas las imegenes
    _postile=0#Posicion del title
    _posfondo=0
    _posEnemy=0
    _blink_posY=215
      
    def cargarMapa(self,Nivel):
        f = open("maps/"+Nivel+".json", "r")##Cargamos un archivo tipo json que tendra un array va tener un array con la posicion de los tiles
        data = json.load(f)
        f.close()
        i=0
        for item in data["layers"]:  ##Un bucle para recorrer todos los layers          
            self.layers(item)
            
        for item in data["tilesets"]:##Para recorrer la informacion
            self.tilesets(item)
            i+=1
       
    def layers(self, layer):  ##Cargamos los layers
        
        self._MapaW= layer["width"]##Ancho del mapa 
        self._MapaH=layer["height"]##Largo del mapa
        
        #Obtener Mapa           
        mapa=layer["data"]  ##Es donde se encuentra la informacion  
        
        #Decodificar
        mapa = base64.decodestring(mapa)
        
        #descomprimir    
        cadena=gzip.zlib.decompress(mapa);##Nos da una matriz de caracteres
        
        # Convertir caracteres a numeros
        salida = []
        for idx in xrange(0, len(cadena), 4):
            val = ord(str(cadena[idx])) | (ord(str(cadena[idx + 1])) << 8) | \
            (ord(str(cadena[idx + 2])) << 16) | (ord(str(cadena[idx + 3])) << 24)
            salida.append(val)
        matrizTemp=[]
        #Convertir el array en una matriz
        for i in range(0, len(salida), self._MapaW):
            matrizTemp.append(salida[i:i+self._MapaW])
        self._matrizMapa=matrizTemp[:]##La almacena en la matriz mapa que es nuestra varible de entorno
       
    def tilesets(self,tileset):
        self._tileW=tileset["tilewidth"]
        self._tileH=tileset["tileheight"]        
        imgTemp=tileset["name"]
        try :
            self._transparentcolor=tileset["transparentcolor"]
        except :
            pass
        try:
            img=pygame.image.load("images/"+imgTemp+".png").convert()
        except pygame.error, message:
                raise SystemExit, message
        if self._transparentcolor!=-1:
            alpha=self._transparentcolor        
            alpha = alpha.lstrip('#')
            lv = len(alpha)
            alpha=tuple(int(alpha[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))                            
            img.set_colorkey(alpha, RLEACCEL)
        self.array_Tileset(img)##Invoca a la funcion Tileset que sirve para que la imagen se hagan en partes y la almacenen cuadro por cuadro 
     
    def array_Tileset(self,img):##Lo separa cuadro por cuadro
        for i in range(30):##Creamos un buble con lo alto y los ancho
            for j in range(27):##Creamos un buble con lo alto y los ancho vamos a cortar cada titley los vamos a almacenar en una lista qeu se llame hojas tiles
                self._mapaImagenes.append(img.subsurface((j*18,i*18,self._tileW,self._tileH)))##Nuestra varible de entorno para almacenar cuadro por cuadro a nuestro vector de entorno        
        for i in range(len(self._mapaImagenes)):##Le asignamos una escala para hacer que los cuadrados se hagan mas grandes
            self._mapaImagenes[i]=pygame.transform.scale2x(self._mapaImagenes[i])    
