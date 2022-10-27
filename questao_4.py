# const = 20
# sequencia = []
# for numero in range(1, 20):
#     numero = input('Insira aqui um número da sequência: ')
#     sequencia.append(numero)


# print(sequencia)
seq_atual = 0
maior_seq = 0

numero_atual = 0
numero_anterior = 0
for numero in range(1, 11):
    numero_atual = int(input('Insira aqui um número da sequência: '))
    if numero_atual >= numero_anterior:
        seq_atual += 1
        if seq_atual > maior_seq:
            maior_seq = seq_atual
    else:
        seq_atual = 1
    numero_anterior = numero_atual
    print(seq_atual, maior_seq)
if seq_atual == maior_seq:

print(f'A maior sequência de números crescentes possui {maior_seq} números.')