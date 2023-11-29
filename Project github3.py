n = int(input('escolha o valor: '))
n2 = n
limite = 50
cont = 0
while True:
    if n2 >=limite:
        n2 -=limite
        cont +=1
    else:
        if cont >0:
            print(f'{cont} notas de {limite}')
        if limite ==50:
            limite =20
        elif limite ==20:
            limite=10
        cont = 0
        if n2 ==0:
            break