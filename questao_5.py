n = int(input('Digite o valor de N, maior ou igual a 50: '))

def calculo_h(n):
    count = 2
    numerador = 0
    denominador = 1
    soma = 1
    while count <= n:
        numerador = (count * 2) - 1
        denominador = count
        divisao = numerador/denominador
        if (count % 2) == 0:
            # print(f'soma_antes = %.2f' %(soma))
            soma += divisao
            # print(f'soma_depois = %.2f' %(soma))
        else:
            # print(f'subtracao_antes = %.2f' %(soma))
            soma -= divisao
            # print(f'subtracao_depois = %.2f' %(soma))
        count += 1
        # print(count)

    print(f'A soma total da sequência H é {soma}')

def calculo_s(n):
    count = 2
    numerador = 0
    denominador = 1
    soma = 1
    while count <= n:
        numerador = count
        denominador = count*count
        divisao = numerador/denominador
        if (count % 2) == 0:
            #print(f'soma_antes = %.2f' %(soma))
            soma -= divisao
            #print(f'soma_depois = %.2f' %(soma))
        else:
            #print(f'subtracao_antes = %.2f' %(soma))
            soma += divisao
            #print(f'subtracao_depois = %.2f' %(soma))
        count += 1
        #print(count)
    print(f'A soma total da sequência S é {soma}')

def calculo_p(n):
    soma = 2
    is_primo = True
    primo = 3
    count = 2
    numerador = 0
    denominador = 1
    while count <= n:
        while is_primo == False:
            primo += 1
            is_primo = True
            for teste_primo in range(2, int((primo/2)+1)):
                if primo % teste_primo == 0:
                    is_primo = False
        # print(primo)
        numerador = primo
        denominador = ((count * 2) - 1) ** 3
        soma += numerador/denominador
        count += 1
        is_primo = False
    
    print(f'A soma total da sequência P é {soma}')

calculo_h(n)
calculo_s(n)
calculo_p(n)