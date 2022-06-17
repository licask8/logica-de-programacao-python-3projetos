''''
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no inicio do programa seja chutado corretamente 

O programa deve informar se o chute foi, acima, abaixo ou igual ao valor aleatório gerado no ínicio do programa



# Método 5Q's para montar um algoritimo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema)

1. Quais são os dados de entrada necessários?
    número aleatório gerado de 1 a 10
    chute do usuario

2. O que devo fazer com estes dados?
    comparar o chute do usuario com o numero gerado e informar se o chute foi, abaixo, acima ou igual ao numero gerado 

3. quais são as restrições deste problema?
    o usuário deve informar um numero entre 1 a 10

4. qual é o resultado esperado?
    O programa deve informar se o chute foi, acima, abaixo ou igual ao valor aleatório gerado no ínicio do programa

5. qual é a sequência de passos a ser feito para chegar no resultado esperado?
input valor_aleatorio de 1 a 10
input chute
if valor_aleatorio > chute:
    print "Chute foi maior que o valor esperado"
if valor_aleatorio < chute:
    print "Chute foi menor que o valor esperado"
if chute = valor_aleatorio:
    print "Acertou! "        
'''
import random

numero_aleatorio = int(random.randint(1,10))
acertou = False

while acertou == False:
    chute = int(input('Digite  um valor de 1 a 10: '))    
    if chute > numero_aleatorio:
        print('Chute foi maior que o valor esperado')
    elif chute < numero_aleatorio:
        print('Chute foi menor que o valor esperado')  
    elif chute == numero_aleatorio:
        acertou = True
        print('Acertou! ')  
        
    

           