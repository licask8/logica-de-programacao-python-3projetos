'''
Crie um programa que recebe um número e imprime o seu fatorial

# Método 5Q's para montar um algoritimo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema)

1. Quais são os dados de entrada necessários?
    numero
2. O que devo fazer com estes dados?
    eu devo calcular o fatorial do número que for passado para o meu programa e o exibir na tela.
3. quais são as restrições deste problema?
    - O número deve ser um valor positivo
    - O número deve ser um número inteiro 
4. qual é o resultado esperado?
    o resultado esperado é que o fatorial do número providenciado seja exibido
5. qual é a sequência de passos a ser feito para chegar no resultado esperado?
input numero
if numero > 0 
if numero = inteiro
fatorial = 1 
loop de 1 a numero
    fatorial = fatorial * numero
print        
'''
numero = int(input('Digite um número '))
if numero > 0:
    fatorial = 1
    for item in range(1,numero +1):
        fatorial = fatorial * item
print(fatorial)        

