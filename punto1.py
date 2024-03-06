total_distanciaInt = 0

etapas = int(input('numero de estapas -->'))

for i in range(etapas):
    distancia = int(input("Distancia da etapa:"))
    total_distanciaInt += distancia

print('la distancia total es', total_distanciaInt)
print('el numero de etapas es'+ str(etapas)  +'etapas')
