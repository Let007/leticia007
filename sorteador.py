import random

print("Bem vindo ao organizador de sorteio!\n")
print("Você irá informar os nomes dos participantes, uma quantidade par, e nós iremos sortear as chaves automáticamente!\n")

participantes = input("Digite o nome dos participantes separando por ',' (Ex. Fulano, Ciclano): ").replace("","")
#replace é utilizado para trocar algo vazio por um caracter ou um conjunto de caracter
participantes_lista = participantes.split(",")

def sortear_torneio (participantes_lista):
  n_chaves = len(participantes_lista) / 2
  c = 1

  while c < n_chaves+1:
    participantes1 = random.choice(participantes_lista)
    participantes_lista.remove(participantes1)
    participantes2 = random.choice(participantes_lista)
    participantes_lista.remove(participantes2)
    print(f"Chave {c}: {participantes1} vs {participantes2}")
    c += 1

if len(participantes_lista) % 2 == 1:
  participantes_lista += [input("Digite mais um participante: ")]
  sortear_torneio(participantes_lista)
else:
  sortear_torneio(participantes_lista)