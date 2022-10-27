salario_fixo = int(input('Informe o salário fixo: '))
vendas = int(input('Informe o total das vendas efetuadas: '))
bonus = 0

if vendas > 1500:
    bonus = (1500 * 0.05) + ((vendas - 1500) * 0.07)
    salario_total = salario_fixo + bonus
elif vendas == 1500:
    bonus = 1500 * 0.05
    salario_total = salario_fixo + bonus
else:
    bonus = vendas * 0.05
    salario_total = salario_fixo + bonus

print(f'O salário total do vendedor é de R$ {salario_total}')