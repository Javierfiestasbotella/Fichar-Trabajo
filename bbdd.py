# -*- coding: utf-8 -*-
import mysql.connector
import getpass
from tkinter import messagebox

dbConnect={
    'host':'lldk499.servidoresdns.net',
    'user':'qadr270',
    'password':'Calafate1123',
    'database':'qadr270',
    
}
conexion=mysql.connector.connect(**dbConnect)
cursor=conexion.cursor()

#Consultar tabla de la bbdd consulta la base de datos actual
def consultar_ddbb():
    global resultado
    global bd
    sql="Select * from trabajadores"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    #print(resultado)
    peticion=''
    for datos in resultado:
        peticion+=f'Numero identificativo--> {datos[0]}\nName--> {datos[1]}\n\n'
    messagebox.showinfo(message=peticion)

def registrar(numero):
    global e2
    #introducir nuevo usuario
    global resultados
    global usuario_usu
    #validar si existe en numero en la bbdd
    sql="Select * from trabajadores"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    usuario_usu=input("digame su usuario: ")
    
    #Inserta Registros
    sqlInsertar="insert into trabajadores(NUMERO,USER)values(%s,%s)"
    cursor.execute(sqlInsertar,(numero,usuario_usu))
    conexion.commit()
    messagebox.showinfo(message="Usuario introducido en la Base de datos del Calafate", title="Conexion BBDD")

#consulter_user(n) en fichar_horario>captura() ok!    
def consulta_user(n):
    global resultado
    sql="Select *from trabajadores where NUMERO=%s"
    cursor.execute(sql,(n,))
    resultado=cursor.fetchone()
    conexion.commit()
    #cursor.close()
    return resultado[1]
    #print( resultado[1])
    
#----------------------
#crea ok

def consultar_bbdd(n):
    global resultado
    global bd
    sql="Select * from trabajadores Where id={}".format(n)
    cursor.execute(sql)
    resultado=cursor.fetchall()
    for datos in resultado:
        nombre=datos[1]
        bd=str(datos[1])+"\n"
        bd='Nombre--> {}\n'.format(datos[1])
        messagebox.showinfo(message=bd)   


#borra ok
def borrar(n):
    conexion=mysql.connector.connect(**dbConnect)
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM trabajadores  WHERE  id={}".format(n))    
    messagebox.showinfo(cursor.rowcount, "registro borrado de la bbdd") 
    conexion.commit()

def inicio_de_sesion():
    global usuario_usu
    global resultado
    usuario_usu=input("Escriba su Usuario: ")
    prueba=consulta_user(usuario_usu)
    while prueba!=resultado[1]:
        messagebox.showinfo(message="Usuario no registrado, compruebe su usuario:", title="Inicio Usuario")
        inicio_de_sesion()
        #prueba=consulta_user(usuario_usu)
    #t.sleep(1)
    #messagebox.showinfo(message="Usuario correcto", title="Inicio Usuario")
    nombre=getpass.getpass("Escriba su contraseña: ")
    while nombre!=resultado[2]:

        messagebox.showinfo(message="Lo siento vuelve a intentarlo", title="Inicio Usuario")
        inicio_de_sesion()
    #messagebox.showinfo(message="contraseña correcta", title="Inicio Usuario")
    print("Bienvenido {} eres nuestro usuario nº {} y tienes el nivel:{}".format(resultado[1],resultado[0],resultado[3]))

def imp():
    print('CONEXION OK')


