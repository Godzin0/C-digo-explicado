from random import choice
#Aqui está importando as propriedades da biblioteca "random" para pegar uma coisa aleatória.#

movimentos = ['cara', 'coroa']
#aqui ta atribuindo a variáver "movimentos" os atributos cara e coroa#

movimento_geral = choice(movimentos)
jogada_AI_1 = choice(movimentos)
movimentos.remove(jogada_AI_1)
jogada_AI_2 = choice(movimentos)
#Aqui ta definindo com o choice se vai ser cara ou coroa, depois a AI 1 escolhe se é cara ou coroa com o choice também, depois o mesmo com a AI 2 (Lembrando que o "remove" tira a 
# possibilidade que o mesmo movimento seja escolhido 2 vezes.

print(f'AI 1 escolheu {jogada_AI_1}')
print(f'AI 2 escolheu {jogada_AI_2}')
print(f'\nCaiu {movimento_geral}')
#aqui ta printando pra mostrar o que cada AI escolheu, e depois o que está certo#

if jogada_AI_1 == movimento_geral:
    print('\nAI 1 acertou')
    print('AI 2 errou')
elif jogada_AI_2 == movimento_geral:
    print('\nAI 2 acertou')
    print('AI 1 errou')
    #aqui ta abrindo um if pra mostrar se está certo ou não. então Se a AI1 estiver certa,a AI2 está errada e vice versa.