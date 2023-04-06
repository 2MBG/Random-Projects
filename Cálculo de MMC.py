def calcular_mmc(a, b):
    '''
    -> A função calcular_mmc recebe dois números a e b como parâmetros. 
       A função então encontra o maior número entre a e b e inicia um loop para testar todos os múltiplos deste número.
       Se o número atual for divisível por ambos a e b, ele é o MMC e a função retorna o valor.
       Caso contrário, o loop continua testando o próximo múltiplo até que o MMC seja encontrado.
    '''

    # Encontrar o maior número entre a e b
    maior_número = max(a, b)
    
    # Iniciar um loop para testar todos os múltiplos do maior número
    while True:
        if maior_número % a == 0 and maior_número % b == 0:
            # Se o número atual é divisível por ambos a e b, ele é o MMC
            mmc = maior_número
            break
        maior_número += 1
    return mmc


a = 34
b = 22
mmc = calcular_mmc(a, b)
print(f'\nO MMC de {a} e {b} é {mmc}\n')

# help(calcular_mmc)
