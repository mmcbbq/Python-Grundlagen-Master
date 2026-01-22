# Das ProblemDu stehst vor einem Hochhaus mit 100 Stockwerken. Du hast zwei identische Kristallkugeln. Du sollst
# herausfinden, ab welchem Stockwerk (dem "kritischen Stockwerk") die Kugeln zerbrechen, wenn man sie aus dem Fenster
# wirft.
# Wenn eine Kugel beim Wurf nicht zerbricht, kannst du sie wiederverwenden.
# Wenn sie zerbricht, ist sie weg.Du musst das kritische Stockwerk mit der minimalen Anzahl an Würfen finden.
import random

kritisch = random.randint(0, 100)
haus = list(range(101))
kritisch = 49
ball_1 = True
ball_2 = True

wurf_aus = len(haus)//2
start_ball_2 = 0

print(kritisch)
print(wurf_aus)
versuche = 0
while ball_1:
    versuche += 1
    if wurf_aus >= kritisch:
        ball_1 = False
        print('Kugel kaputt')
    else:
        start_ball_2 = wurf_aus + 1
        rest = len(haus) - wurf_aus
        wurf_aus = wurf_aus + (rest // 2)
        print(f'Ich werfe gleich aus {wurf_aus}')

for etage in range(start_ball_2, 101):
    versuche += 1
    if etage == kritisch:
        ball_2 = False
        print(f'Die {etage} ist die krtische {kritisch} versuche: {versuche}')
        break


print('Ball 2 ')