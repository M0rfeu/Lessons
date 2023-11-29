n = 1
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
while n !=5:
    n = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos numeros\n[5] Encerrar programa\n\033[1;32mOpção: \033[m'))
    if n ==1:
        print(n1+n2)
    if n ==2:
        print(n1*n2)
    if n ==3:
        if n1 >n2:
            print('O numero {} é maior que o numero {}'.format(n1,n2))
        if n1 <n2:
            print('O numero {} é maior que o numero {}'.format(n2,n1))
        if n1 ==n2:
            print('Ambos os numeros são iguais')
    if n ==4:
        n1 = int(input('digite o primeiro numero: '))
        n2 = int(input('digite o segundo numero: '))
    if n !=1 and n !=2 and n !=3 and n !=4 and n !=5:
        print('Opção inválida, tente novamente!')
print('fim do programa')