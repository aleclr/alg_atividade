# def questao4_comlista():
#     const = 20
#     sequencia = []
#     seq_atual = 0
#     maior_seq = 0
#     count = 0
#     for numero in range(1, 10):
#         numero = int(input('Insira aqui um número da sequência: '))
#         sequencia.append(numero)
#     for numero in sequencia:
#         if count < len(sequencia):
#             if sequencia[count+1] >= sequencia[count]:
#                 seq_atual += 1
#                 if seq_atual > maior_seq:
#                     maior_seq = seq_atual
#             else:
#                 seq_atual = 1
#             count += 1
#         else:
#             print(seq_atual, maior_seq)

#SOLUÇÃO SEM UTILIZAR LISTAS
def questao4_semlista():
    seq_atual = 0
    maior_seq = 0
    soma_atual = 0
    soma_maior = 0

    numero_atual = 0
    numero_anterior = 0
    empate = False
    for numero in range(1, 11):
        numero_atual = int(input('Insira aqui um número da sequência: '))
        if numero_atual >= numero_anterior:
            seq_atual += 1
            soma_atual += numero_atual
            print(f'a soma atual é {soma_atual}')
            print(f'a maior soma é {soma_maior}')
            if seq_atual > maior_seq:
                maior_seq = seq_atual
                soma_maior = soma_atual
                empate = False
            elif seq_atual == maior_seq:
                if soma_atual > soma_maior:
                    soma_maior = soma_atual
                empate = True
        else:
            seq_atual = 1
            soma_atual = numero_atual    
        numero_anterior = numero_atual
        print(seq_atual, maior_seq)
        print(empate)
    if empate:
        print(f'A maior sequência de números crescentes possui {maior_seq} números!')
        print(f'Como houveram mais de uma sequência com {maior_seq} números, pelo critério de desempate, o total da soma da sequência vencedora é {soma_maior}.')
    else:
        print(f'A maior sequência de números crescentes possui {maior_seq} números.')

questao4_semlista()