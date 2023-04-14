print('\n\033[1;33mCÁLCULO DE MÉDIA GERAL DO 3º ANO DO ENSINO MÉDIO\033[m')

# Lista de notas
notas3 = []

# Quantidade de matérias do 3º ano
quantidade_matérias3 = len(notas3)

# Soma das notas do 3º ano
soma_notas3 = sum(notas3)
print(f'\nSoma das notas do 3º ano: {soma_notas3:.1f}')
print(f'Total de matérias: {quantidade_matérias3}')

# Média geral 3º ano
média_geral3 = soma_notas3 / quantidade_matérias3

# A média geral
print(f'\nSua média geral é: {média_geral3:.2f}\n')
