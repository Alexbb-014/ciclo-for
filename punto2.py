print('cuanto se debe regar en diversos cultivos')
papa = 0
yuca = 0 
zanahoria = 0
cultivosStr = int(input('selecione el cultivo que va regar --> \n1. Papas\n2. yuca \n3. zanahorias\n-->'))
if  cultivosStr == 1:
    for i in range(3):
        litros_papaInt = int(input('cuantos litros regó -->'))
        papa += litros_papaInt
    print('total de litros regados esta semana son', papa)
elif cultivosStr == 2:
    for i in range(3):
        litros_yucaInt = int(input('cuantos litros regó -->'))
        yuca += litros_yucaInt
    print('total de regados esta semana son',yuca)
elif cultivosStr == 3:
    for i in range(3):
        litros_zanahoriaInt = int(input('cuantos litros regó -->'))
        zanahoria += litros_zanahoriaInt
    print('total de litros regados esta semana son',zanahoria)
    