import random
from time import sleep

# Lista de destinos
destinos = []

destino_escolhido = random.choice(destinos)

print(f'\nSua próxima viagem será para... ', end='')
sleep(1)
print(f'{destino_escolhido}!\n')
