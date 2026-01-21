# Aufgabe: In einem sortierten Array soll ein Suchwert gefunden werden.
#
# Eingabe:
#
# Das zu durchsuchende Array, von links nach rechts mit aufsteigend sortierten Werten gefüllt. Die gleichen Werte dürfen mehrfach vorkommen.
# Der Suchwert.
# Ausgabe:
#
# Wenn der Suchwert gefunden wurde, die Position des Suchwertes im Array.
# Wenn der Suchwert mehrmals im Array vorkommt, ist nicht festgelegt, welche der möglichen Positionen ausgegeben wird.
# Wenn der Suchwert nicht gefunden wurde, ein entsprechender Fehlercode, möglicherweise ergänzt durch die Position, an der der Suchwert stehen würde.
# Ablauf:
#
# Der Suchbereich umfasst anfangs das komplette Array.
# Ist der Suchbereich leer, wurde der Suchwert nicht gefunden. Die Suche ist erfolglos beendet.
# Die Mitte des Suchbereichs wird berechnet und der dort befindliche Wert mit dem Suchwert verglichen.
# Ist der Suchwert gleich dem Vergleichswert, ist die Suche erfolgreich beendet. Die Position der Mitte wird ausgegeben.
# Ist der Suchwert kleiner als der Vergleichswert, kann sich der Suchwert nur in der linken Hälfte befinden. Der rechte Rand des Suchbereichs wird auf die Position links von der Mitte eingeschränkt.
# Ist der Suchwert größer als der Vergleichswert, kann sich der Suchwert nur in der rechten Hälfte befinden. Der linke Rand des Suchbereich wird auf die Position rechts von der Mitte eingeschränkt.
# Die Suche wird mit dem verkleinerten Suchbereich ab Schritt 2 wiederholt.
# Bei diesem Ablauf wird die Länge des Suchbereichs in jedem Schritt halbiert. Spätestens wenn der Suchbereich auf ein einzelnes Element geschrumpft ist, ist die Suche beendet. Dieses eine Element ist entweder das gesuchte Element, oder das gesuchte Element kommt nicht vor; dann ist als Ergebnis bekannt, wohin es einsortiert werden müsste.
#
# Der Algorithmus zur binären Suche kann mittels Iteration oder Rekursion implementiert werden. Um ihn verwenden zu können, müssen die Daten bereits sortiert und in einer Datenstruktur vorliegen, in der direkt auf das n-te Element zugegriffen werden kann. Auf einer einfachen verketteten Liste würde die Effizienz verloren gehen (siehe aber Skip-Liste).


sort_list = [4, 8, 12, 13, 39, 40, 60, 63]
suche = 99
# liste = [40, 8, 63, 60, 12, 4, 13, 82, 87, 87, 87, 84, 85, 39, 57, 55, 72, 6, 46, 18, 5, 97, 78, 64, 94, 64, 62, 22, 11, 89, 92, 53, 22, 51, 44, 49, 6, 87, 57, 20, 39, 67, 87, 49, 71, 79, 80, 94, 19, 57, 13, 71, 51, 99, 68, 31, 80, 63, 41, 17, 25, 7, 88, 86, 29, 58, 99, 63, 28, 59, 2, 34, 15, 73, 36, 90, 9, 75, 61, 40, 1, 23, 71, 94, 75, 46, 59, 72, 73, 63, 93, 90, 68, 7, 29, 92, 44, 74, 84, 80]
# print(sorted(liste))
sort_list = [1, 2, 4, 5, 6, 6, 7, 7, 8, 9, 11, 12, 13, 13, 15, 17, 18, 19, 20, 22, 22, 23, 25, 28, 29, 30, 31, 34, 36, 39, 39, 40, 40, 41, 44, 44, 46, 46, 49, 49, 51, 51, 53, 55, 57, 57, 57, 58, 59, 59, 60, 61, 62, 63, 63, 63, 63, 64, 64, 67, 68, 68, 71, 71, 71, 72, 72, 73, 73, 74, 75, 75, 78, 79, 80, 80, 80, 82, 84, 84, 85, 86, 87, 87, 87, 87, 87, 88, 89, 90, 90, 92, 92, 93, 94, 94, 94, 97, 99, 99]
# check

while True:
    mitte = (len(sort_list)) // 2
    print(f'mitte index {mitte} ')

    if len(sort_list) == 0:
        print('nicht weil')
        break
    elif suche == sort_list[mitte]:
        print('gefunden')
        break
    elif len(sort_list) == 1:
        print('nicht da')
        break
    elif suche > sort_list[mitte]:
        print('rechte seite')
        sort_list = sort_list[mitte + 1:]
    elif suche < sort_list[mitte]:
        print('linke seite')
        sort_list = sort_list[:mitte]

