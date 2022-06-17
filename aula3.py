### Laços de Repetição + Listas

from lib2to3.pgen2.token import NUMBER


for palavra in range(1,10):
    print(palavra)

for item in range(0,21,2):
    print(item)    

nomes = ['gustavo', 'lucas', 'igor', 'irineu']

for nome in nomes:
    print(nome)

# Ploblema 1 a N - Imprime os valores de 1 a N

valor_maximo = int(input('Digite o valor máximo'))
valor_inicial = 1

for numero in range(valor_inicial, valor_maximo +1):
    print(numero)