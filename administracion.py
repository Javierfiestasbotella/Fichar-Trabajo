# -*- coding: utf-8 -*-
#!/usr/bin/python
import getpass
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import tkinter as tk
from bbdd import *
from main import *
from datetime import datetime


class Cuestionario:
    def __init__(self):
        self.id=''
        self.nombre=''
        self.d=datetime.now().strftime('%Y-%m-%d')
    def ingresar_usuario(self):
        sql = "INSERT INTO trabajadores (numero,user) VALUES (%s,%s)"
        val = (vid.get(),vnombre.get())
        cursor.execute(sql, val)
        c.borrar_campos()
        messagebox.showinfo(cursor.rowcount, "registro insertado")  
        #cursor.close()
        
        conexion.commit()
        #conexion.close()
        
    
    ##### funciones nuevas
    def inspeccionar(self,name,archivo):
        archivo =open(archivo,'r')
        arch=archivo.readlines()
        contador=0
        for nombre in arch:
            if name in nombre:
                contador+=1
        if contador%2==0:
            print(f'{name} adios, que tengas un buen día')
        else:
            print(f'{name} Bievenido al trabajo')
        archivo.close()





    #funciona
    def suma_horas(self,hora1,hora2):#creo que hay que importarlo con int
        formato = "%H:%M:%S"
        lista = hora2.split(":")
        hora=int(lista[0])
        minuto=int(lista[1])
        segundo=int(lista[2])
        from datetime import datetime, timedelta
        h1 = datetime.strptime(hora1, formato)
        dh = timedelta(hours=hora) 
        dm = timedelta(minutes=minuto)          
        ds = timedelta(seconds=segundo) 
        resultado1 =h1 + ds
        resultado2 = resultado1 + dm
        resultado = resultado2 + dh
        resultado=resultado.strftime(formato)
        return str(resultado)

#print(suma_horas('05:30','03:15'))

    def restar_hora(self,hora1,hora2):
        formato = "%H:%M"
        h1 = datetime.strptime(hora1, formato)
        h2 = datetime.strptime(hora2, formato)
        resultado = h1 - h2
        return str(resultado)


    def crea_dic(self):
        diccionario = {}
        archivo=open(str('{}.txt'.format(self.d)),'r')
        #open(arch,'r')
        lineas = archivo.readlines()
        for linea in lineas:
            name = linea[:4]
            hora = linea[-6:-1]
            if diccionario == {}:
                diccionario[name] = [hora]
            elif name in diccionario.keys():
                diccionario[name].append(hora)
            else:
                diccionario[name] = [hora]
        archivo.close()
        return diccionario

    def total_horas(self):
        arch=open(str('{}.txt'.format(self.d)),'a',encoding="utf-8")
        arch.write(f'\n\n---------Total horas trabajadores--------\n\n')
        #self.d=datetime.datetime.now().strftime('%Y-%m-%d_')
        diccionario_completo=c.crea_dic()
        for name,hora in diccionario_completo.items():
            if len(hora)==1 or len(hora)==3:
                arch=open(str('{}.txt'.format(self.d)),'a')
                arch.write(f'{name} tiene una entrada a las {hora} ,pero no tiene hora de salida\n')
            elif len(hora)==4:
                arch=open(str('{}.txt'.format(self.d)),'a')
                arch.write(f'{name}----> {c.suma_horas(c.restar_hora(hora[1],hora[0]),c.restar_hora(hora[3],hora[2]))}\n')
            elif len(hora)==2:
                arch=open(str('{}.txt'.format(self.d)),'a')
                #open(archivo_dia,'a',encoding="utf-8")
                arch.write(f'{name}----> {c.restar_hora(hora[1],hora[0])}\n')
            else:
                print('ok')
        arch.write(f'''Registro Horas Trabajadores
        Vegetariano el calafate S.L.
        CIF: B93480127 Calle Andrés Perez, 6 29008 Málaga
        fecha: {self.d}
        Real Decreto-ley 8/2019, de 8 de marzo, «la empresa garantizará el registro diario de jornada,
        que deberá incluir el horario concreto de inicio y finalización de la jornada de trabajo de 
        cada persona trabajadora»
            ''') 
        messagebox.showinfo(message="Cierre realizado ¡¡¡Correctamente!!!", title="Cierre Diario") 
        arch.close()
    ######funciones para una fecha cualquiera
    


    ##### fin de funciones nuevas
    def acerca_de(self):
        messagebox.showinfo(message="Cuestionario de conexion con BBDD en Mysql:\n------------\nBBDD:\n       Conectar: crea la BBDD, en caso contrario, avisa. \n      Salir: Sale del programa cuestionario. \n------------\nBorrar: Borra los campos escritos\n------------\nCRUD:\n       Crea: Crea usuario\n        Lee: Lee los datos del usuario por su id.\n     Actualizar:Actualiza datos de usuario por su id.\n      Borra: borra el usuario por su id.\n------------\nAyuda:\n        Acerca de: Istrucciones de la app.\n        Licencia: Licencia de la app.", title="Instrucciones")

    def licencia(self):
        messagebox.showinfo(message="APP Control horario: Vegetariano El Calafate S.L.\n-------\nProgramador:  Fº Javier Fiestas Botella\nLenguaje: Python10.0\nAñon 2022 version septiembre001", title="Licencia")

    def borrar_campos(self):
        self.id=vid.set('')
        self.nombre=vnombre.set('')
     
    def salir(self):
        self.raiz2.destroy()
        self.raiz2.quit()
        #f.interfaz()
        


   
    def borrar_usuario(self):
        #global resultado
        #sql="Select *from trabajadores where NUMERO=%s"
        cursor.execute("DELETE FROM trabajadores  WHERE  NUMERO={}".format(vid.get()))
        self.id=vid.set('')
        c.borrar_campos()   
        messagebox.showinfo(cursor.rowcount, "registro borrado de la bbdd") 
        conexion.commit()

        
    def actualizar_usuario(self):
        sql='''UPDATE trabajadores SET user=%s WHERE numero=%s'''
        val =(vnombre.get(),vid.get())
        cursor.execute(sql,val)
        cursor.fetchone()
        c.borrar_campos()
        messagebox.showinfo(cursor.rowcount, "registro actualizado") 
        conexion.commit()
        

    def conectar(self):
        pass
            
    def lee_usuario(self):#acabado en fichar horarios
        try:
            global resultado
            sql="Select *from trabajadores where NUMERO=%s"
            cursor.execute(sql,(vid.get(),))
            resultado=cursor.fetchone()
            #conexion.commit()
            #cursor.close()
            messagebox.showinfo(message=f'El trabajador con número: {vid.get()} pertenece a--> {resultado[1]}')
        
        except TypeError:
            messagebox.showinfo('El usuario con Id-> {} no existe\n o ha sido borrado'.format(int(vid.get())))
        except ValueError:
            messagebox.showinfo(message='Si quieres ver los datos de un usuario, \n  debes introducir un Id con numeros enteros positivos', title='Cuidado!!!')

    def interfaz2(self):
        #self.raiz2=Toplevel(self.raiz)
        self.raiz2=Tk()
        self.nombre_usuario="Admin El Calafate"
        self.raiz2.geometry("280x300+0+0")
        #self.raiz.iconbitmap("rubik.ico")
        self.raiz2.title(self.nombre_usuario)
        
        self.fondo=PhotoImage(width=213,height=248)
        self.lblFondo=Label(self.raiz2).place(x=0, y=220)
        
        # Crear el menu principal
        global vnombre
        global vid 
        vnombre=StringVar()
        vid=StringVar()
        def hola():
            print( "Hola!")
        menubarra = Menu(self.raiz2)
      

        # Crea un menu desplegable y lo agrega al menu barra
        menuarchivo = Menu(menubarra, tearoff=0)
        menuarchivo.add_command(label="Ver trabajadores", command=consultar_ddbb)
        menuarchivo.add_separator()
        menuarchivo.add_command(label="Salir", command=c.salir)
        menubarra.add_cascade(label="BBDD", menu=menuarchivo)

        # Crea dos menus desplegables mas
        menueditar = Menu(menubarra, tearoff=0)
        menueditar.add_command(label="Borrar campos", command=c.borrar_campos)
        menubarra.add_cascade(label="Borrar", menu=menueditar)
        
        menuayuda = Menu(menubarra, tearoff=0)
        menuayuda.add_command(label="Crear", command=c.ingresar_usuario)
        menuayuda.add_command(label="Leer", command=c.lee_usuario)
        menuayuda.add_command(label="Actualizar", command=c.actualizar_usuario)
        menuayuda.add_command(label="Borrar", command=c.borrar_usuario)
        menubarra.add_cascade(label="CRUD", menu=menuayuda)

        menuayuda2 = Menu(menubarra, tearoff=0)
        menuayuda2.add_command(label="CIERRE", command=c.total_horas)
        menuayuda2.add_command(label="Acerca de...", command=c.acerca_de)
        menubarra.add_cascade(label="Opciones Avanzadas", menu=menuayuda2)
        
        self.etiqueta_id=Label(self.raiz2,text="Id").place(x=30, y=20) 
        self.espacio0=Entry(self.raiz2,justify=RIGHT,textvariable=vid)
        self.espacio0.place(x=130, y=20,)
        self.espacio0.focus_set()
        

        self.etiqueta_nombre=Label(self.raiz2,text="Nombre").place(x=30, y=50)
        self.espacio1=Entry(self.raiz2,justify=RIGHT,textvariable=vnombre).place(x=130, y=50)  
        #Label(self.raiz).pack()
        self.raiz2.config(menu=menubarra)
        self.raiz2.mainloop()



c= Cuestionario()
    #c.ingresar_usuario()
#c.interfaz2()
