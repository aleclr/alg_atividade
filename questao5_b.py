n = int(input('Digite o valor de N, maior ou igual a 50: '))
count = 2
numerador = 0
denominador = 0
soma = 1
while count <= n:
    numerador = count
    denominador = count*count
    divisao = numerador/denominador
    if (count % 2) == 0:
        #print(f'soma_antes = %.2f' %(soma))
        soma += divisao
        #print(f'soma_depois = %.2f' %(soma))
    else:
        #print(f'subtracao_antes = %.2f' %(soma))
        soma -= divisao
        #print(f'subtracao_depois = %.2f' %(soma))
    count += 1
    #print(count)

print(f'A soma total da sequência é {soma}')