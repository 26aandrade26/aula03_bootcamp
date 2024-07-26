from random import randint
from time import sleep
from operator import itemgetter

resultados = dict ()
for i in range (1,5):
    resultados[f'Jogador {i}'] = randint(1,6)

ranking = list()

print("Valores sorteados: ")

for k,v in resultados.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)

ranking = sorted(resultados.items(), key=itemgetter(1),reverse=True)
#print(ranking)
print("-" * 30)
print("  == RANKING DOS JOGADORES ==")
for i, v in enumerate(ranking):
    print(f"  {i+1}º lugar: {v[0]} com {v[1]}.")
    sleep(1)