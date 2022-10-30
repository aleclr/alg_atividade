def sequencia_crescente_e_constante():

    #declaração variáveis da sequência crescente
    seq_crescente_atual = 0
    maior_seq_crescente = 0
    soma_atual = 0
    soma_maior = 0
    empate_crescente = False

    #declaração variáveis da sequência constante
    seq_constante_atual = 0
    maior_seq_constante = 0
    empate_constante = False
    identificador_atual = 0
    identificador_maior = 0

    #declaração variáveis genéricas
    numero_atual = 0
    numero_anterior = 0

    #TROQUE O RANGE PARA UM NUMERO MENOR, PARA FACILITAR OS TESTES
    for numero in range(1, 151):
        numero_atual = int(input('Insira aqui um número da sequência: '))

        #SE O NUMERO INSERIDO FOR MAIOR QUE O ANTERIOR:
        if numero_atual > numero_anterior:
            #reseta sequencia constante e identificador
            seq_constante_atual = 1
            identificador_atual = numero_atual
            #computa sequencia crescente
            seq_crescente_atual += 1
            soma_atual += numero_atual
            if seq_crescente_atual > maior_seq_crescente:
                maior_seq_crescente = seq_crescente_atual
                soma_maior = soma_atual
                empate_crescente = False
            elif seq_crescente_atual == maior_seq_crescente:
                #atualiza a maior soma de sequencia crescente, para o critério de desempate
                if soma_atual > soma_maior:
                    soma_maior = soma_atual
                empate_crescente = True

        #SE O NUMERO INSERIDO FOR IGUAL AO ANTERIOR:
        elif numero_atual == numero_anterior:
            #reseta sequencia crescente e soma
            seq_crescente_atual = 1
            soma_atual = numero_atual
            #computa sequencia constante
            seq_constante_atual += 1
            identificador_atual = numero_atual
            if seq_constante_atual > maior_seq_constante:
                maior_seq_constante = seq_constante_atual
                identificador_maior = identificador_atual
                empate_constante = False
            elif seq_constante_atual == maior_seq_constante:
                #atualiza o maior identificador de sequencia constante, para o critério de desempate
                if identificador_atual > identificador_maior:
                    identificador_maior = identificador_atual
                empate_constante = True

        #SE O NUMERO INSERIDO FOR MENOR QUE O ANTERIOR:
        else:
            #reseta sequencia crescente e soma
            seq_crescente_atual = 1
            soma_atual = numero_atual
            #reseta sequencia constante e identificador
            seq_constante_atual = 1
            identificador_atual = numero_atual
        #atualiza o loop
        numero_anterior = numero_atual
        print(seq_crescente_atual,seq_constante_atual)
    
    #OUTPUTS:
    if empate_crescente:
        print(f'A maior sequência de números crescentes possui {maior_seq_crescente} números!')
        print(f'Como houveram mais de uma sequência com {maior_seq_crescente} números, pelo critério de desempate, o total da soma da sequência vencedora é {soma_maior}.')
    else:
        print(f'A maior sequência de números crescentes possui {maior_seq_crescente} números.')
    if empate_constante:
        print(f'A maior sequência de números constantes possui {maior_seq_constante} números!')
        print(f'Como houveram mais de uma sequência com {maior_seq_constante} números, pelo critério de desempate, a sequência de números constantes de valor {identificador_maior} é a vencedora.')
    else:
        print(f'A maior sequência de números constantes possui {maior_seq_constante} números.')
    

sequencia_crescente_e_constante()