# -*- coding: utf-8 -*-
#!/usr/bin/python
import os
import io
from random import randrange, choice
import random
import sys
from this import d
from tkinter import * 
from tkinter import PhotoImage
from tkinter import messagebox
import time as t
from bbdd import *
import tkinter as tk
from tkinter import Tk, Text
from io import open
import datetime
from datetime import datetime
import time
from administracion import *


class Fichar():
    def __init__(self):
        self.nombre=''
        self.espacio2=''
        self.listado=''
        self.lista=[]
        self.fecha=''
        self.d=datetime.now().strftime('%Y-%m-%d')
        self.camila_img=['imagenes\\cam9.gif','imagenes\\cam4.gif','imagenes\\cam1.png','imagenes\\cam2.png','imagenes\\cam3.png','imagenes\\cam4.png','pruebas python\\Fichar_tiempo\\imagenes\\cam5.png','imagenes\\cam7.png','imagenes\\cam8.png']
        self.cruz_img=['imagenes\\cruz01.gif','imagenes\\cruz7.gif','imagenes\\cruz1.png','imagenes\\cruz2.png','imagenes\\cruz3.png','imagenes\\cruz4.png','pruebas python\\Fichar_tiempo\\imagenes\\cruz5.png','imagenes\\cruz6.png','imagenes\\cruz6.png','imagenes\\cruz9.png','imagenes\\cruz8.png','imagenes\\cruz9.png','imagenes\\cruz10.png','imagenes\\cruz11.png','imagenes\\cruz12.png','imagenes\\cruz13.png']
        self.javi_img=['imagenes\\javi1.png','imagenes\\javi2.png','imagenes\\javi3.png','imagenes\\javi4.png','imagenes\\javi5.png','imagenes\\javi7.png','imagenes\\javi9.png']
        self.tere_img=['imagenes\\tere1 (1).png','imagenes\\tere1 (2).png','imagenes\\tere1 (3).png']
        self.estef_img=['imagenes\\estefania (1).png','imagenes\\estefania (2).png','imagenes\\estefania (3).png','imagenes\\estefania (4).png','imagenes\\estefania (5).png','imagenes\\estefania (6).png']
        self.admin=['imagenes\\admin.png']
    
    
    
    
    def inspeccionar(self,name):
        archivo =open(str('{}.txt'.format(self.d)),'r')
        arch=archivo.readlines()
        contador=0
        for nombre in arch:
            if name in nombre:
                contador+=1
        if contador%2==0:
            #self.listado.insert('insert', f'{name} adios, que tengas un buen día'+'\n')
            archivo.close()
            return f'{name}, que tengas un buen día'
        elif contador%2!=0:
            #self.listado.insert('insert',f'{name} Bievenido al trabajo'+'\n')
            archivo.close()
            return f'{name} Bievenida al trabajo'
        
    def imagen(self,name):
        if name=='Teresa Orellana':
            lista_imagenes=self.tere_img
        elif name=='Mari Cruz Frias':
            lista_imagenes=self.cruz_img
        elif name=='Camila Lopez':
            lista_imagenes=self.camila_img
        elif name=='Estefania Ferre':
            lista_imagenes=self.estef_img
        elif name=='Javi Fiestas':
            lista_imagenes=self.javi_img
        
        else:
            print('No hay imagenes')

        mi_imagen=PhotoImage(file=random.choice(lista_imagenes))
        Label(self.raiz, image=mi_imagen, bd=0).place(x=40,y=300)
        Label.place_forget()
        self.raiz.mainloop()
    
    #captura() en interfaz() ok!    
    def captura(self):
        #self.d=datetime.now().strftime('%Y-%m-%d')
        if vespacio2.get()=='0005343291' or vespacio2.get()=='admin':
            print('administracion')
            self.espacio2=vespacio2.set('')
            self.raiz.quit()#def usuario(self):#pantalla a elegir usuario o registrarse
            c.interfaz2()
            

        else:
            if vespacio2.get()=='':
                messagebox.showinfo(message="Debes de pasar de nuevo su identificacion, el campo está vacío", title="Control de horas")
            else:
                try:
                    name2=consulta_user(vespacio2.get())
                except TypeError :
                #mysql.connector.errors.InterfaceError:
                    messagebox.showinfo(message="Usuario no registrado, consulte con Javier Fiestas", title="Conexion BBDD")
                except mysql.connector.errors.InterfaceError:
                #mysql.connector.errors.DatabaseError: 4031 (HY000): The client was disconnected by the server because of inactivity. See wait_timeout and interactive_timeout for configuring this behavior.
                    messagebox.showinfo(message="Perdida de señal...Reconectando", title="Conexion BBDD")   
                    self.raiz.destroy()
                    f.interfaz() 
                self.listado=vtexto.set(name2)
                #f.inspeccionar(name2)
                self.espacio2=vespacio2.set('')
                f.crea_fichero(name2)
                self.listado=Text(self.raiz,width=40,height=2)
                self.listado.place(x=50,y=160)
                if name2 in self.lista:
                    for i in self.lista:
                        self.listado.insert('insert', f.inspeccionar(i)+'\n')
                        self.lista.remove(name2)
                        f.imagen(name2)
                else:
                    self.lista.append(name2)
                    for i in self.lista:
                        self.listado.insert('insert', f.inspeccionar(i)+'\n')
                        self.lista.remove(name2)#aqui he puesto esto primero porque no cambiaba el mensaje de entrada o salida , ponía primero la foto
                        f.imagen(name2)
                        
    
    #crea_fichero() en captura() ok!                  
    def crea_fichero(self,name):
        #self.d=datetime.now().strftime('%Y-%m-%d')
        print(self.d+'.txt')
        self.hora=datetime.now().strftime('%H:%M')

        if os.path.exists(self.d+'.txt')==True:
            #messagebox.showinfo(message="Registro guardado", title="Control de horas")
            #print('existe, empezamos a grabar')
            self.fichero=open(str('{}.txt'.format(self.d)),'a')
            self.fichero.write("{}---> Hora: {}\n".format(name,self.hora))
            self.fichero.close()
        else:
            self.lista=[]
            messagebox.showinfo(message="Creamos nuevo fichero. feliz día", title="Control de horas")
            #print('No existe el fichero de hoy. lo creamos...')
            self.fichero=open(str('{}.txt'.format(self.d)),'a',encoding="utf-8")
            #self.fichero.write("Entradas y Salidas de los trbajadores de El Calafate.\n ")
            self.fichero.write("{}---> Hora: {}\n".format(name,self.hora))
            self.fichero.close()         
    
    



    
    #interfaz() ok!        
    def interfaz(self):#pantalla interfaz principal
      self.raiz=Tk()
      self.nombre_usuario="El Calafate"
      self.raiz.geometry("400x600+0+0")
      self.raiz.configure(background='#F2F2F2')
      #self.raiz.iconbitmap("rubik.ico")
      self.raiz.title(self.nombre_usuario)
      global vespacio2
      global vtexto
      

      vespacio2=StringVar()
      vtexto=StringVar()
      Label(self.raiz, text="Aproxime tarjeta").pack()
      self.espacio2=Entry(self.raiz,font=('italic',25),textvariable=vespacio2)
      self.espacio2.pack()
      self.espacio2.focus_set()
      Label(self.raiz, text="\n\n\n").pack() 
      self.boton1=Button(self.raiz,text="Activate",bg="#3ADF00", height=2 ,font=('italic',10),width=30,activebackground="#FA2821",command=f.captura).place(x=100,y=80)
      Label(self.raiz, text="").pack()
      Label(self.raiz,text='Trabajadores Activos').place(x=250,y=270)
      Label(self.raiz, text="").place(x=75,y=140)
   
      self.listado=Text(self.raiz,width=40,height=2)
      self.listado.place(x=50,y=160)
      
      self.raiz.mainloop()
 #------------------------------------------------------------- 
if __name__ == "__main__":
    f=Fichar()
    f.interfaz()
