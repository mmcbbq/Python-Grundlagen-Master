# Berechne die Summe aller Zahlen von 1 - 500
print('Aufgabe 1')
print('#######################')

# Schreib eine Schleife die folgendes Muster ausgibt
# *
# **
# ***
# ****
# *****




print('Aufgabe 2')
print('#######################')
#
# # Schreib eine Schleife die folgendes Muster ausgibt
# # *****
# # ****
# # ***
# # **
# # *
print('Aufgabe 3')
print('#######################')
#
# # Schreib eine Schleife, die folgendes Muster ausgibt
# # 1
# # 12
# # 123
# # 1234
# # 12345


print('Aufgabe 4')
print('#######################')
#
# # Schreib eine Schleife, die folgendes Muster ausgibt
# # 5
# # 45
# # 345
# # 2345
# # 12345


print('Aufgabe 5')
print('#######################')

# # Schreib eine Schleife, die folgendes Muster ausgibt
# # 12345
# # 1234
# # 123
# # 12
# # 1
print('Aufgabe 6')
print('#######################')
#
# # Der user soll zwei Zahlen angeben.
# # Bei der Eingabe von 6 und 2 soll folgendes Muster ausgegeben werden
# #
print('Aufgabe 7')
print('#######################')
#
# #     **
# #     **
# #     **
# #     **
# #     **
# #     **
#
# #     ******
# #     ******
#
# #     *
# #     **
# #     ***
# #     ****
# #     *****
# #     ******
# #
#
#
# #     ******
# #     *****
# #
# # Bei
# # 7
# # und
# # 4
# #
# # ****
# # ****
# # ****
# # ****
# # ****
# # ****
# # ****
# #
# # *******
# # *******
# # *******
# # *******
# #
# # *
# # **
# # ***
# # ****
# # *****
# # ******
# # *******
# #
# # *******
# # ******
# # *****
# # ****
#
#
# # ### fizzbuzz
# # Schreiben Sie ein Programm, das die Zahlen von 1 bis 100 ausgibt.
# # Bei jeder Zahl, die durch 5 teilbar ist, soll "fizz" ausgegeben werden
# # und bei jeder Zahl, die durch 7 teilbar ist,
# # soll "buzz" ausgegeben werden.
# # Wenn die Zahl sowohl durch 7 als auch durch 5 teilbar ist,
# # soll "fizzbuzz" ausgegeben werden.
# # Der Modulo-Operator ermittelt den Rest bei Division.
# # Somit ist eine Teilbarkeit einfach dann erreicht,
# # wenn die Modulo-Operation (%, MOD) den Rest 0 liefert.
print('Aufgabe 8')
print('#######################')
#
print('Aufgabe 9')
print('#######################')
#
# # Schreib eine Schleife, die folgendes Muster ausgibt
# # OXOXOXOX
# # XOXOXOXO
# # OXOXOXOX
# # XOXOXOXO
# # OXOXOXOX
# # XOXOXOXO
# # OXOXOXOX
# # XOXOXOXO

y = 10000
zeichen = 'x'
for x in range(y):

    for i in range(y):
        if (i+x) % 2 == 0:
            zeichen = 'x'
        else:
            zeichen = 'o'
        print(zeichen,end='')
    print('')