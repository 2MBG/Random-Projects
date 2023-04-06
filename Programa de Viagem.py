import random
from time import sleep

destinos = ['Monte Verde', 'Gramado', 'Paranapiacaba', 'Machu Picchu',
            'Foz do Iguaçu', 'Moscou', 'São Petersburgo', 'Belo Horizonte', 
            'São Paulo', 'Curitiba', 'João Pessoa', 'Ilhabela', 'Chapada Diamantina']

destino_escolhido = random.choice(destinos)

print(f'\nSua próxima viagem será para... ', end='')
sleep(1)
print(f'{destino_escolhido}!\n')
