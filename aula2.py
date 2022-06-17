            ### Condicionais ###

# if, elif e else

'''
E ae Elielson, bora dar uma saóda hoje? 
Se eu terminar meu trabalho aqui, eu consigo.
'''

trabalho_terminado = True
if trabalho_terminado == True:
    print('Opa! Bora dar uma saída.')
else:
    print('Não posso sair agora')  



'''
Ei, Você consegue me ajudar a mover essas caixas lá para fora hoje a tarde?
Se eu estiver livre, sim. Mas se não der pede meu irmão para te ajudar
'''

estou_livre = False
if estou_livre == True:
    print('Ok,. posso te ajudar hoje sim!')
else:
    print('Peça o meu irmão para te ajudar')    



'''
Eu cheguei atrasado na aula, ainda posso entrar?
Se essa não for sua terceira vez chegando atrasado, então pode sim, caso contrário irá tomar uma suspensão
'''

numero_de_atrasos = 2 
if numero_de_atrasos >= 3:
    print('Você está suspenso')
elif numero_de_atrasos == 1:
    print('Pode entrar, porém caso tome mais 2 faltas, irá ser suspenso')
elif numero_de_atrasos == 2:
    print('Pode entrar, porèm caso tome mais 1 falta, irá ser suspenso')
else:
    print('Pode entrar')    