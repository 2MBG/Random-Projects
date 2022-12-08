import emoji
from time import sleep

def título(mensagem):
    print(end='\n')
    tamanho = len(mensagem) + 4
    print('=' * tamanho)
    print(f'{mensagem}'.center(tamanho))
    print('=' * tamanho)


def tamanho(tam):
    '''
    -> Analisa o tamanho da pessoa de acordo com o sexo.
    :param tam: tamanho que será analisado. 
    '''
    
    # Masculino
    if sexo == 'M':
        if tam < 1.73:

            print('\n\033[1;33mAnalisando...\033[m')
            sleep(2)
            print(f'\n{nome}, a altura média masculina no Brasil é de 1,73m.')
            sleep(2)
            print('\nPortanto, você está abaixo da altura média brasileira.\n')
            sleep(2)
        
        elif tam >= 1.73 and tam <= 1.80:
            print('\n\033[1;33mAnalisando...\033[m')
            sleep(2)
            print(f'\n{nome}, a altura média masculina no Brasil é de 1,73m.')
            sleep(2)
            print('\nPortanto, você está de acordo com a altura média brasileira.\n')
            sleep(2)
        
        elif tam > 1.80:
            print('\n\033[1;33mAnalisando...\033[m')
            sleep(2)
            print(f'\n{nome}, a altura média masculina no Brasil é de 1,73m.')
            sleep(2)
            print('\nPortanto, você está acima da altura média brasileira.\n')
            sleep(2)
    
    # Feminino
    if sexo == 'F':
        if tam < 1.60:
            print('\n\033[1;33mAnalisando...\033[m')
            sleep(2)
            print(f'\n{nome}, a altura média feminina no Brasil é de 1,60m.')
            sleep(2)
            print('\nPortanto, você está abaixo da altura média brasileira.\n')
            sleep(2)
        
        elif tam >= 1.60 and tam <= 1.65:
            print('\n\033[1;33mAnalisando...\033[m')
            sleep(2)
            print(f'\n{nome}, a altura média feminina no Brasil é de 1,60m.')
            sleep(2)
            print('\nPortanto, você está de acordo com a altura média brasileira.\n')
            sleep(2)
        
        elif tam > 1.65:
            print('\n\033[1;33mAnalisando...\033[m')
            sleep(2)
            print(f'\n{nome}, a altura média feminina no Brasil é de 1,60m.')
            sleep(2)
            print('\nPortanto, você está acima da altura média brasileira.\n')
            sleep(2)


def leiaNome(name):
    '''
    -> Valida o nome informado pelo usuário.
    :param name: Nome do usuário.
    '''

    ok = False

    while not ok:
        n = str(input(name))

        if n.isnumeric() or n == '':
            print(f'\n\033[1;31mERRO! {n} é inválido, utilize apenas letras.\033[m')
        else:
            ok = True
            return n


def leiaTamanho(dados):
    '''
    -> Converte para float o tamanho informado pelo usuário.
    :param dados: tamanho informado pelo usuário.
    '''
    while True:
    
        try:
            size = str(input(dados))
        except (ValueError):
            print('\n\033[1;31mDigite um número decimal válido.\033[m')
            continue
        else:
            return float(size)


título('Analise sua altura')

while True:
    nome = leiaNome('\n\033[1;34mDigite seu nome:\033[m ').title().strip().split()[0]
    
    sexo = str(input('\n\033[1;34mSEXO: M/F?\033[m ')).upper()
    while not sexo == 'M' and not sexo == 'F':
        sexo = str(input('\n\033[1;31mOpção inválida.\033[m SEXO: M/F? ')).upper()

    altura = leiaTamanho('\n\033[1;34mQual é a sua altura?\033[m ')

    teste = str(input('\n\033[1;34mTodas as informações passadas estão corretas (S/N)?\033[m ')).upper()
    while not teste == 'S' and not teste == "N":
        print(end='\n')
        teste = str(input('\033[1;31mOpção inválida.\033[m Todas as informações passadas estão corretas (S/N)? ')).upper()

    if teste == 'S':
        tamanho(altura)

    elif teste == 'N':
        print('\n\033[1;33mAtualize as informações incorretas:\033[m')

        nome = leiaNome('\n\033[1;34mDigite seu nome:\033[m ').title().strip()
        
        sexo = str(input('\n\033[1;34mSEXO: M/F?\033[m ')).upper()
        while not sexo == 'M' and not sexo == 'F':
            sexo = str(input('\n\033[1;31mOpção inválida.\033[m SEXO: M/F? ')).upper()

        altura = leiaTamanho('\n\033[1;34mQual é a sua altura?\033[m ')

        tamanho(altura)

    print('\033[1;32m-=\033[m' * 47)
    fim = int(input('\nDigite \033[1;33m0\033[m caso queira ver algumas informações inúteis sobre sua altura ou digite \033[1;33m1\033[m para sair: '))

    if fim == 0:
        num1 = altura / 1000 # Quilômetro
        num2 = altura / 100 # Hectômetro
        num3 = altura / 10 # Decâmetro
        num4 = altura * 10 # Decímetro
        num5 = altura * 100 # Centímetro
        num6 = altura * 1000 # Milímetro

        print(f'\n{nome}, sua altura de {altura}m é equivalente à:\n')
        sleep(2)
        
        print('=' * 40)
        print(f'Quilômetros: \t{num1}\n'
              f'Hectômetros: \t{num2}\n'
              f'Decâmetros:  \t{num3}\n'
              f'Decímetros:  \t{num4:.0f}\n'
              f'Centímetros: \t{num5:.0f}\n'
              f'Milímetros:  \t{num6:.0f}'
              )
       
        print('=' * 40)
        print(end='\n')
        
        print('\033[1;32m-=\033[m' * 47)

        print('\n\033[1;33mEspero que as informações tenham sido úteis para você!\033[m', 
                emoji.emojize(':waving_hand:', language='alias'), '\n')
        break
        
    elif fim == 1:
        print('\n\033[1;33mEspero que as informações tenham sido úteis para você!\033[m', 
                emoji.emojize(':waving_hand:', language='alias'), '\n')
        break
