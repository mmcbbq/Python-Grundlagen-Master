user = ['Bob', 'Eve', 'Jim', 'John', 'Tim']
# printe für alle Namen der Liste user "createuser username"
# Beispiel "createuser Bob"
for name in user:
    print(f'createuser {name}')

# Wandele die Username in lowercase um bevor du sie ausdruckst
# Beispiel "createuser bob"
print('#########################################')
for name in user:
    print('createuser', name.lower())
# Erweitere die Ausgabe um einen Zähler
# Beispiel "createuser Bob 1"
# Beispiel "createuser Eve 2"
print('#########################################')
z = 0
for name in user:
    z += 1
    print('createuser', name, z)

# Es sollen nur noch User ausgegeben werden die ein "i"" in ihrem namen haben.
print('#########################################')

for name in user:
    if 'i' in name:
        print('createuser', name)
# Tausche in jedem Namen den Buchstaben "B" gegen ein '8', 'E' gegen ein '3' 'o' gegen 0 und 'i' gegen '1' aus.
print('#########################################')
for name in user:
    print(name.replace('B', '8').replace('E', '3').replace('o', '0').replace('i', '1'))

print('#########################################')
print('#########################################')
print('#########################################')

for name in user:
    new_name = ""
    for letter in name:
        if letter == 'B':
            new_name += '8'
        elif letter == 'E':
            new_name += '3'
        elif letter == 'o':
            new_name += '0'
        elif letter == 'i':
            new_name += '1'
        else:
            new_name += letter
    print(new_name)
# Es soll folgende Ausgabe mit einer Schleife erzeugt werden
# Tip "\t"

# Bob
# 	 Eve
# 		 Jim
# 			 John
# 				 Tim
print('#########################################')
z = 0
for name in user:
    print('\t' * z, name)
    z += 1

for z, name in enumerate(user):
    print(z)
    tabstring = '\t' * z
    print(f'{tabstring}{name}')

rand_zahlen = [452, 30, 688, 177, 534, 137, 490, 387, 845, 882, 896, 798, 456, 691, 932, 978, 333, 499, 222, 775, 866,
               976, 809, 803, 970, 840, 2, 814, 638, 189, 255, 960, 199, 350, 365, 104, 396, 794, 489, 497, 380, 598,
               609, 987, 328, 314, 678, 331, 85, 426, 31, 58, 540, 124, 8, 454, 979, 744, 280, 584, 323, 665, 627, 999,
               244, 31, 764, 420, 797, 534, 121, 655, 427, 758, 131, 652, 440, 571, 408, 154, 138, 70, 798, 325, 584,
               718, 923, 398, 285, 342, 392, 206, 863, 266, 832, 746, 906, 180, 172, 183, 224, 207, 800, 349, 786, 554,
               305, 52, 871, 161, 364, 542, 944, 739, 154, 771, 732, 957, 590, 444, 870, 527, 394, 426, 199, 129, 634,
               897, 899, 407, 334, 372, 489, 498, 913, 255, 684, 813, 231, 710, 628, 578, 331, 680, 468, 111, 595, 720,
               320, 650, 667, 635, 589, 408, 41, 770, 153, 697, 506, 573, 931, 678, 292, 915, 197, 926, 991, 937, 185,
               816, 587, 555, 341, 767, 261, 930, 950, 879, 100, 521, 853, 441, 650, 429, 196, 703, 228, 911, 902, 16,
               518, 143, 528, 106, 806, 230, 82, 548, 476, 736]

# Elemente addieren: Gehe durch die Liste rand_zahlen und addiere alle Elemente [Summe]
print('#########################################')

summe = 0

for i in rand_zahlen:
    summe += i
print(summe)
# print(sum(rand_zahlen))
# Gib die Anzahl der Elemente aus ohne len oder andere eingebaute Funktionen
print('#########################################')
z = 0
for i in rand_zahlen:
    z += 1
print(z)
print(len(rand_zahlen))

# Größtes Element finden: Finde das größte Element in einer Liste von Zahlen.
print('#########################################')
g = rand_zahlen[0]
for i in rand_zahlen:
    if g < i:
        g = i
print(g)
print(max(rand_zahlen))
# Ausgabe aller Elemente *2
print('#########################################')
rand_zahlen_2 = []
for i in rand_zahlen:
    rand_zahlen_2.append(i * 2)
print(rand_zahlen_2)

# Nur Gerade Zahlen Ausgeben
print('#########################################')
for i in rand_zahlen:
    if i % 2 == 0:
        print(i)

# Gebe nur Zahlen aus die zwischen 150 und 300 sind.
print('#########################################')
for i in rand_zahlen:
    if 150 <= i <= 300:
        print(i)
# Füge alle Zahlen die kleiner als 100 sind in eine Liste kleiner100 hinzu.
print('#########################################')
kleiner100 = []
for i in rand_zahlen:
    if i < 100:
        kleiner100.append(i)

print(kleiner100)
# Sortiere alle Zahlen aus der rand_zahlen in eine nested_list
# nested_list = [[Zahlen 0-300],[Zahlen 301 - 600], [Zahlen 601-999]]
print('#########################################')
nested_list = [[], [], []]
for i in rand_zahlen:
    if 0 <= i <= 300:
        nested_list[0].append(i)
    elif 301 <= i <= 600:
        nested_list[1].append(i)
    elif 601 <= i <= 999:
        nested_list[2].append(i)
print(nested_list)

print('#########################################')
print('#########################################')
print('#########################################')
print('#########################################')

mem_mom = [33, 44, 40, 52, 60, 56, 40, 52, 60, 56]

# Info: Mittelwert = Summe / Anzahl

# Berechne den Mittelwert aller Daten "Gesamt"
z = 0
summe = 0
for i in mem_mom:
    z += 1
    summe += i
gesamt = summe / z
print(gesamt)

# Berechne den Mittelwert der ersten 5 Einträge "Vormittag"
print('############################################')
z = 0
summe = 0
for i in mem_mom[0:5]:
    z += 1
    summe += i
vormittag = summe / z
print(vormittag)

# Berechne den Mittelwert der letzten 5 "Nachmittag"
print('############################################')
z = 0
summe = 0
for i in mem_mom[5:]:
    z += 1
    summe += i
nachmittag = summe / z
print(nachmittag)

# Gib die Mittel werte in der Konsole aus
# 1. Der gesamte Mittelwert
# 2. Der größere Mittelwert. Wenn Vormittag und Nachmittag gleich sind dann zuesr Vormittag
# Beispiel
# Gesamt 49
# Nachmittag 51
# Vormittag 48
print('############################################')
print('############################################')
print('############################################')

print('Der Mittelwert ist :', gesamt)
if vormittag > nachmittag:
    print('Vormittag:', vormittag)
    print('Nachmittag:', nachmittag)
elif vormittag < nachmittag:
    print('Nachmittag:', nachmittag)
    print('Vormittag:', vormittag)

# --------------------------------
muster = [1, 2, 3, 4, 5]
# gib mithilfe der Liste muster das Muster aus
print('######################')

# 1   2   3   4   5
# 2   4   6   8  10
# 3   6   9  12  15
# 4   8  12  16  20
# 5  10  15  20  25

for reihe in muster:
    for zahl in muster:
        # if zahl*reihe < 10:
        # 	print(' ' + str(zahl * reihe), end=' ')
        # else:
        print(zahl * reihe, end='\t')
    print('')  # neue Zeile
