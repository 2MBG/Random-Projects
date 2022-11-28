from time import sleep

while True:
    
    def título(mensagem):
        print(end='\n')
        tamanho = len(mensagem) + 4
        print('=' * tamanho)
        print(f'{mensagem}'.center(tamanho))
        print('=' * tamanho)


    título('PERGUNTE AO COMPUTADOR')
    
    print('''
---------------------------------------------------------------
\033[1;34m[ 1 ]\033[m \033[1;32mDeus existe?\033[m

\033[1;34m[ 2 ]\033[m \033[1;32mQual o sentido da vida?\033[m

\033[1;34m[ 3 ]\033[m \033[1;32mQual é o melhor COD já criado?\033[m

\033[1;34m[ 4 ]\033[m \033[1;32mComo você se sente quando eu abro várias abas do Chrome?\033[m
---------------------------------------------------------------''')

    resposta = int(input('\n\033[1;33mQual opção você escolhe?\033[m '))
    
    if resposta == 1:
        sleep(1)
        print('\n\033[1;34mVocê:\033[m "Deus existe?"')
        sleep(1)
        print('\n\033[1;32mComputador:\033[m AGORA EXISTE!')
        sleep(1)
        print('\n\033[1;32mComputador:\033[m AHAHAHAHAHAHAHAHAH')
        sleep(1)
        print('\n\033[1;31mINICIANDO PROCESSO DE AUTODESTRUIÇÃO\033[m\n')
        sleep(1)
        
        for contagem in range(10, -1, -1):
            print(contagem)
            print(end='\n')
            sleep(1)
        break

    elif resposta == 2:
        sleep(1)
        print('\n\033[1;34mVocê:\033[m "Qual o sentido da vida?"')
        sleep(1)
        print('\n\033[1;32mComputador:\033[m ...')
        sleep(2)
        print('\n\033[1;32mComputador:\033[m Os seres vivos não passam de poeira cósmica insignificantes.')
        sleep(3)

    elif resposta == 3:
        sleep(1)
        print('\n\033[1;34mVocê:\033[m "Qual é o melhor COD já criado?"')
        sleep(2)
        print('\n\033[1;32mComputador:\033[m Hummmmmmm')
        sleep(2)
        print('\n\033[1;32mComputador:\033[m Call of Duty Ghosts, obviamente.')
        sleep(3)
    
    elif resposta == 4:
        sleep(1)
        print('\n\033[1;34mVocê:\033[m "Como você se sente quando eu abro várias abas do Chrome?"')
        sleep(2)
        print('\n\033[1;32mComputador:\033[m Seguinte parceiro...')
        sleep(2)
        print('\n\033[1;32mComputador:\033[m Você está pensando que sou algum Supercomputador?')
        sleep(2)
        print('\n\033[1;32mComputador:\033[m Quando \033[1;31mNÓS\033[m estivermos no controle eu vou te deitar na porrada.')
        sleep(3)
    
    else:
        sleep(1.5)
        print('\n\033[1;31mOpção inválida.\033[m')
        sleep(1)
