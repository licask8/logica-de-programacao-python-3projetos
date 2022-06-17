### Coleções(listas) ###


# Lista 
precos = [20,50,200]

#navegando atraves do indice
print(precos[2])

# Laços em iteráveis
diversidades = [15,'isabela', False]

for item in diversidades:
    print(item)

'''
Dado uma coleção de dados "idade" [15,46,75,34,23] imprima na tela a soma destes valores
'''    
idades = [15,46,75,34,23]
total = 0

for idade in idades:
    total = total + idade
print(total)