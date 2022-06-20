''''
Projeto - medidor de velocidade

Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua. Crie um programa que recebe do úsuario um valor que representa a velocidade e com base nessa velocidade diga se ele tomou uma multa leve, grave ou gravissima.
Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa",caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exiba "levou multa gravíssima".

# Método 5Q's para montar um algoritimo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema)

1. Quais são os dados de entrada necessários?
    -velocidade
2. O que devo fazer com estes dados?

3. quais são as restrições deste problema?

4. qual é o resultado esperado?

5. qual é a sequência de passos a ser feito para chegar no resultado esperado?
'''

velocidade_maxima = 80
velocidade_usuario = int(input("Digite sua velocidade? "))
if velocidade_usuario <= velocidade_maxima:
    print('Não levou multa')
elif velocidade_usuario > velocidade_maxima and velocidade_usuario <= velocidade_maxima + 10:
    print('Levou multa leve')
elif velocidade_usuario > velocidade_maxima + 11 and velocidade_usuario <= velocidade_maxima +20:
    print('Levou multa grave')
elif velocidade_usuario > velocidade_maxima + 20:
    print('Levou multa gravissima')
