n1 = int(input('digite um numero: '))
n2 = int(input('digite outro: '))
n3 = int(input('digite mais um: '))
n4 = int(input('digite o ultimo: '))
n5 = (n1,n2,n3,n4)
print(f'o numero 9 apareceu \033[1;32m{n5.count(9)}\033[m vezes')
if n5.count(3) >=1:
    print(f'o valor 3 apareceu na \033[1;32m{n5.index(3)+1}\033[m casa')
for n in n5:
    if n %2 ==0:
        print(n)