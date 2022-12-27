# -*- coding: utf-8 -*-
#!/usr/bin/python

from datetime import datetime
    
def suma_horas(hora1,hora2):#creo que hay que importarlo con int
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

def restar_hora(hora1,hora2):
        formato = "%H:%M"
        h1 = datetime.strptime(hora1, formato)
        h2 = datetime.strptime(hora2, formato)
        resultado = h1 - h2
        return str(resultado)



def crea_dic_antiguo_fichero(fecha):
        diccionario = {}
        archivo=open(fecha,'r')
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

def total_horas_archivo_Antiguo(fecha):
        arch=open(fecha,'a',encoding="utf-8")
        arch.write(f'\n\n---------Total horas trabajadores--------\n\n')
        diccionario_completo=crea_dic_antiguo_fichero(fecha)
        for name,hora in diccionario_completo.items():
            if len(hora)==1 or len(hora)==3:
                #arch=open(str('{}.txt'.format(fecha)),'a')
                arch.write(f'{name} tiene una entrada a las {hora} ,pero no tiene hora de salida\n')
            elif len(hora)==4:
                #arch=open(str('{}.txt'.format(fecha)),'a')
                arch.write(f'{name}----> {suma_horas(restar_hora(hora[1],hora[0]),restar_hora(hora[3],hora[2]))}\n')
            elif len(hora)==2:
                #arch=open(str('{}.txt'.format(fecha)),'a')
                #open(archivo_dia,'a',encoding="utf-8")
                arch.write(f'{name}----> {restar_hora(hora[1],hora[0])}\n')
            else:
                print('ok')
        print(diccionario_completo)
        arch.write(f'''Registro Horas Trabajadores
        Vegetariano el calafate S.L.
        CIF: B93480127 Calle Andrés Perez, 6 29008 Málaga
        fecha: {fecha[:-4]}
        Real Decreto-ley 8/2019, de 8 de marzo, «la empresa garantizará el registro diario de jornada,
        que deberá incluir el horario concreto de inicio y finalización de la jornada de trabajo de 
        cada persona trabajadora»
            ''')    
        arch.close()


lista=['C:\\Users\\hp\\Desktop\\python\\p\\octubre\\2022-10-29_.txt']
def pon_sello(lista):
    for i in lista:
        print(total_horas_archivo_Antiguo(i))
pon_sello(lista)
#ar=open('C:\\Users\\hp\\Desktop\\python\\p\\octubre\\2022-10-03_.txt',"r")
#print(ar.read())
