vendedor = input()

salario_fixo = input()
salario_fixo = float(salario_fixo)

total_vendas = input()
total_vendas = float(total_vendas)

bonus = total_vendas * 0.15
salario_final = salario_fixo + bonus

print(f'TOTAL = R$ {salario_final:.2f}')
