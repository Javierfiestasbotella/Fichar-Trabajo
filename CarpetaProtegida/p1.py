lista=[2,1,-4,-2,0,4,-3,3]
lista_diferencias=list()
for i in range(1,len(lista)):
    if lista[i]<0:
        #lista[i]*=-1
        diferencia=lista[i]-lista[i-1]
        if diferencia<0:
            lista_diferencias.append(diferencia*-1)
        else:
            lista_diferencias.append(diferencia)

    else:
        diferencia=lista[i]-lista[i-1]
        if diferencia<0:
            lista_diferencias.append(diferencia*-1)
        else:
            lista_diferencias.append(diferencia)
print(lista_diferencias)
print(max(lista_diferencias))
