import random
n = cont = 0
c = random.randint(1,10)
while True:
    n = int(input('digite um numero: '))
    n2 = str(input('Par ou Impar? [P/I]')).upper().strip()[0]
    print(f'-'*60)
    print(f'Você digitou {n} enquanto o computador escolheu {c}')
    if n + c % 2 == 0:
        print(f'O total deu: {n+c} e o resultado foi \033[1;32mPar\033[m')
        if n2 =='P':
            print(f'\033[1;32mParabéns, você ganhou!\nContinue jogando\033[m')
            cont +=1
    if n + c % 2 != 0:
        print(f'O total deu: {n+c} e o resultado foi \033[1;32mImpar\033[m')
        if n2 =='I':
            print(f'\033[1;32mParabéns, você ganhou!\nContinue jogando\033[m')
            cont +=1
    if n+c %2 ==0 and n2 =='I' or n+c %2 !=0 and n2 == 'P':
        print(f'\033[1;31mQue pena, você perdeu!\033[m')
        break
    print(f'-'*60)
if cont ==0:
    print(f'Você não obteve vitória alguma')
if cont == 1:
    print(f'Você obteve {cont} vitória')
if cont >1:
    print(f'Você obteve {cont} vitórias seguidas')
print('programa encerrado')