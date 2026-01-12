# Erstelle eine list tic
tic = []
# Füge tic eine Liste mit den werten 'l','l','l' hinzu
# Füge tic eine 2. liste mir den werten 'k','k','k' hinzu
# Füge tic eine 3. liste mir den werten 'b','b','b' hinzu
tic.append(['l', 'l', 'l'])
tic.append(['k', 'k', 'k'])
tic.append(['b', 'b', 'b'])
print(tic)
# Printe jede unterliste in einer Zeile aus
# ['l', 'l', 'l']
# ['k', 'k', 'k']
# ['b', 'b', 'b']
print(tic[0])
print(tic[1])
print(tic[2])
print('------------------------------')
# ändere die liste wie folgt ab
# ['x', 'l', 'l']
# ['k', 'x', 'k']
# ['b', 'b', 'x']
tic[0][0] = 'x'
tic[1][1] = 'x'
tic[2][2] = 'x'
print(tic[0])
print(tic[1])
print(tic[2])
# ändere die liste wie folgt ab
# ['x', 'o', 'o']
# ['x', 'x', 'o']
# ['o', 'x', 'o']
print('------------------------------')
tic[0][1], tic[0][2] = 'o', 'o'
tic[1][0], tic[1][-1] = 'x', 'o'
tic[2][0], tic[2][1], tic[2][2] = 'o', 'x', 'o'
print(tic[0])
print(tic[1])
print(tic[2])
# ändere die liste wie folgt ab
# ['o', 'o', 'o']
# ['x', 'x', 'o']
# ['o', 'x', 'o']
print('------------------------------')
tic[0][0] = 'o'
print(tic[0])
print(tic[1])
print(tic[2])
# schriebe ein Programm das 2 Zahlen zwischen 1 und 3 und einem Buchstaben vom user fordert
# Anschliessend soll der Wert mit der Pos der zwei Zahlen mit den Buchstaben überschrieben werden
# und die Liste wie in der vorherigen Aufgabe ausgegeben werden
 #y
# 1['o', 'o', 'o']
# 2['x', 'x', 'o']
# 3['o', 'x', 'o']
#    1    2    3  x
x_wert = int(input('x wert Zahl 1-3:\n'))
y_wert = int(input('y wert Zahl 1-3:\n'))
zeichen = input('Zeichen:\n')
# if y_wert == 1:
#     y_wert = 2
# elif y_wert == 2:
#     y_wert= 1
# elif y_wert == 3:
#     y_wert = 0


tic[y_wert - 1][x_wert - 1] = zeichen
print('---------------------------------------')
print(tic[0])
print(tic[1])
print(tic[2])

# Beispiel Zahl1 = 3 Zahl2 = 2 Buchstabe = p
# 1['o', 'o', 'o']
# 2['x', 'x', 'p']
# 3['o', 'x', 'o']

# Zähle alle "o" in der mittleren Liste
zaehler = 0
if tic[1][0] == 'o':
    zaehler += 1
if tic[1][1] == 'o':
    zaehler += 1
if tic[1][2] == 'o':
    zaehler += 1
print(zaehler)

# Schreib eine If anweisung die 'Sieg' ausgibt wenn das Zeiche auf pos 1.1 das selbe ist wie auf pos 2.2 und 3.3

if tic[0][0] == tic[1][1]:
    if tic[0][0] == tic[2][2]:
        print('Sieg')
else:
    print('kein Sieg')

if tic[0][0] == tic[1][1] and tic[0][0] == tic[2][2]:
    print('Sieg mit and')
else:
    print('kein Sieg mit and')

if tic[2][0] == tic[1][1] and tic[2][0] == tic[0][2]:
    print('Sieg unten nach oben')
else:
    print('kein Sieg')

