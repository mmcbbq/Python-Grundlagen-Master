# Schreibe eine Python-Funktion, die den Bubblesort-Algorithmus verwendet,
# um eine Liste von Zahlen in aufsteigender Reihenfolge zu sortieren.
# Der Bubblesort-Algorithmus funktioniert, indem er benachbarte Elemente vergleicht
# und sie vertauscht, wenn sie in der falschen Reihenfolge sind.
# Dieser Prozess wird so lange wiederholt, bis die gesamte Liste sortiert ist.

liste = [27, 29, 7, 76, 56]
liste = [40, 8, 63, 60, 12, 4, 13, 82, 87, 87, 87, 84, 85, 39, 57, 55, 72, 6, 46, 18, 5, 97, 78, 64, 94, 64, 62, 22, 11,
         89, 92, 53, 22, 51, 44, 49, 6, 87, 57, 20, 39, 67, 87, 49, 71, 79, 80, 94, 19, 57, 13, 71, 51, 99, 68, 31, 80,
         63, 41, 17, 25, 7, 88, 86, 29, 58, 99, 63, 28, 59, 2, 34, 15, 73, 36, 90, 9, 75, 61, 40, 1, 23, 71, 94, 75, 46,
         59, 72, 73, 63, 93, 90, 68, 7, 29, 92, 44, 74, 84, 80]
for y in range(len(liste) - 1):
    print('start aussen')
    for x in range(len(liste) - 1 - y):  # -y zur optimierung
        print('start innen')
        print(f'{liste[x]} vergleiche mit {liste[x + 1]}')
        if liste[x] > liste[x + 1]:
            zwischen = liste[x]
            liste[x] = liste[x + 1]
            liste[x + 1] = zwischen
            print(f'habe {liste[x]} und {liste[x + 1]} getauscht')
        print('ende innen')
    print('ende aussen')
    print(liste)
print(len(liste))
liste = [40, 8, 63, 60, 12, 4, 13, 82, 87, 87, 87, 84, 85, 39, 57, 55, 72, 6, 46, 18, 5, 97, 78, 64, 94, 64, 62, 22, 11,
         89, 92, 53, 22, 51, 44, 49, 6, 87, 57, 20, 39, 67, 87, 49, 71, 79, 80, 94, 19, 57, 13, 71, 51, 99, 68, 31, 80,
         63, 41, 17, 25, 7, 88, 86, 29, 58, 99, 63, 28, 59, 2, 34, 15, 73, 36, 90, 9, 75, 61, 40, 1, 23, 71, 94, 75, 46,
         59, 72, 73, 63, 93, 90, 68, 7, 29, 92, 44, 74, 84, 80]

list_dic = [{'name': 'Melanie Reilly', 'email': 'jacksonlopez@example.com', 'anzahl': 40},
            {'name': 'Gregory Russell', 'email': 'swilliams@example.net', 'anzahl': 8},
            {'name': 'Aaron Ross', 'email': 'kevincline@example.org', 'anzahl': 99},
            {'name': 'Meredith Coleman', 'email': 'qvargas@example.com', 'anzahl': 60},
            {'name': 'Michael Salazar', 'email': 'patriciasmith@example.net', 'anzahl': 12},
            {'name': 'Patricia Davis', 'email': 'hernandezlindsay@example.net', 'anzahl': 4},
            {'name': 'Albert Smith', 'email': 'andrea66@example.com', 'anzahl': 13},
            {'name': 'James Young', 'email': 'hphillips@example.com', 'anzahl': 82},
            {'name': 'Jennifer Mahoney', 'email': 'natashabaxter@example.net', 'anzahl': 87},
            {'name': 'John Smith', 'email': 'cherylhoward@example.org', 'anzahl': 87},
            {'name': 'David Cook', 'email': 'jlopez@example.org', 'anzahl': 87},
            {'name': 'Arthur Wang', 'email': 'slong@example.net', 'anzahl': 84},
            {'name': 'Charles Delgado', 'email': 'marshallanna@example.org', 'anzahl': 85},
            {'name': 'Jose Dickerson', 'email': 'buchanandanielle@example.org', 'anzahl': 39},
            {'name': 'Jose Cardenas', 'email': 'jennifer37@example.com', 'anzahl': 57},
            {'name': 'Amy Hall', 'email': 'perrydean@example.net', 'anzahl': 55},
            {'name': 'Maria Fernandez', 'email': 'mmckinney@example.com', 'anzahl': 72},
            {'name': 'Julie Arellano', 'email': 'hicksricky@example.net', 'anzahl': 6},
            {'name': 'Alexis Baker', 'email': 'johnathan86@example.org', 'anzahl': 46},
            {'name': 'Ricky Jones', 'email': 'taylorleslie@example.org', 'anzahl': 18},
            {'name': 'Mr. Thomas Hardy Jr.', 'email': 'savannahnorton@example.com', 'anzahl': 5},
            {'name': 'Kristen Vaughan', 'email': 'ericgomez@example.net', 'anzahl': 97},
            {'name': 'Robin Tanner', 'email': 'katelynjackson@example.net', 'anzahl': 78},
            {'name': 'Megan Bates', 'email': 'ogolden@example.net', 'anzahl': 64},
            {'name': 'Kimberly Lucas', 'email': 'mackjennifer@example.org', 'anzahl': 94},
            {'name': 'Taylor Hudson', 'email': 'ihouston@example.com', 'anzahl': 64},
            {'name': 'Teresa Palmer', 'email': 'andrea21@example.org', 'anzahl': 62},
            {'name': 'Michael Miller', 'email': 'bhood@example.org', 'anzahl': 22},
            {'name': 'Walter Gibbs', 'email': 'ishields@example.com', 'anzahl': 11},
            {'name': 'Christine Smith', 'email': 'stephanie96@example.net', 'anzahl': 89},
            {'name': 'Scott Brown', 'email': 'robert16@example.com', 'anzahl': 92},
            {'name': 'Brad Thompson', 'email': 'scottjohn@example.net', 'anzahl': 53},
            {'name': 'Crystal Myers', 'email': 'mirandashannon@example.com', 'anzahl': 22},
            {'name': 'Charlene Page', 'email': 'dvillanueva@example.com', 'anzahl': 51},
            {'name': 'Kent Richardson', 'email': 'annethompson@example.com', 'anzahl': 44},
            {'name': 'Gloria Johnson', 'email': 'kfoster@example.net', 'anzahl': 49},
            {'name': 'Tracie Ross', 'email': 'roygay@example.org', 'anzahl': 6},
            {'name': 'David Clark', 'email': 'torresaaron@example.org', 'anzahl': 87},
            {'name': 'Richard Simon', 'email': 'diane09@example.net', 'anzahl': 57},
            {'name': 'Matthew Wilson', 'email': 'stephanie20@example.net', 'anzahl': 20},
            {'name': 'Adam Ayers', 'email': 'hodgerichard@example.net', 'anzahl': 39},
            {'name': 'Sandra Cole', 'email': 'sherry92@example.net', 'anzahl': 67},
            {'name': 'Leslie Short', 'email': 'sarah82@example.org', 'anzahl': 87},
            {'name': 'Natalie Torres', 'email': 'ccook@example.net', 'anzahl': 49},
            {'name': 'Michelle Davis', 'email': 'kelseycrawford@example.org', 'anzahl': 71},
            {'name': 'Lindsay Schroeder', 'email': 'taylorchristine@example.org', 'anzahl': 79},
            {'name': 'Gina Berg', 'email': 'michael75@example.net', 'anzahl': 80},
            {'name': 'Lori David', 'email': 'robertpatterson@example.org', 'anzahl': 94},
            {'name': 'Suzanne Underwood', 'email': 'charles49@example.net', 'anzahl': 19},
            {'name': 'Rhonda Chen', 'email': 'mfischer@example.com', 'anzahl': 57},
            {'name': 'Alicia Gray', 'email': 'troy65@example.org', 'anzahl': 13},
            {'name': 'Robert Sanchez', 'email': 'jacob91@example.com', 'anzahl': 71},
            {'name': 'Ashley Best', 'email': 'roberthuerta@example.net', 'anzahl': 51},
            {'name': 'Stanley Perry', 'email': 'carlarandolph@example.net', 'anzahl': 99},
            {'name': 'Shelia Ortiz', 'email': 'wbaker@example.com', 'anzahl': 68},
            {'name': 'Stacy Wilson', 'email': 'laura79@example.com', 'anzahl': 31},
            {'name': 'Steven Orr', 'email': 'ehodge@example.com', 'anzahl': 80},
            {'name': 'Richard Smith', 'email': 'tracy23@example.net', 'anzahl': 63},
            {'name': 'Rachel York', 'email': 'reginald97@example.org', 'anzahl': 41},
            {'name': 'Travis Guerrero', 'email': 'idaniels@example.net', 'anzahl': 17},
            {'name': 'Sandra Hanson', 'email': 'michelle91@example.net', 'anzahl': 25},
            {'name': 'Michael Rubio', 'email': 'lmendez@example.com', 'anzahl': 7},
            {'name': 'Jose Burton', 'email': 'kellydaniel@example.net', 'anzahl': 88},
            {'name': 'George Wells', 'email': 'allisonvirginia@example.net', 'anzahl': 86},
            {'name': 'Joseph Hernandez', 'email': 'joel56@example.org', 'anzahl': 29},
            {'name': 'Jason Schwartz', 'email': 'kennethgeorge@example.org', 'anzahl': 58},
            {'name': 'Michael Carter', 'email': 'heather82@example.org', 'anzahl': 99},
            {'name': 'Jermaine White', 'email': 'hectormartinez@example.org', 'anzahl': 63},
            {'name': 'David Tran', 'email': 'zhardy@example.com', 'anzahl': 28},
            {'name': 'Timothy Pace', 'email': 'bpugh@example.com', 'anzahl': 59},
            {'name': 'Alexander Sweeney', 'email': 'kelseyortiz@example.net', 'anzahl': 2},
            {'name': 'Christopher Lewis', 'email': 'woodjulia@example.net', 'anzahl': 34},
            {'name': 'Christopher Brown', 'email': 'browndebra@example.com', 'anzahl': 15},
            {'name': 'Brenda Lucas', 'email': 'tfoley@example.org', 'anzahl': 73},
            {'name': 'Kenneth Bernard', 'email': 'bernardkaren@example.org', 'anzahl': 36},
            {'name': 'Stephanie Johnson', 'email': 'joshuathomas@example.com', 'anzahl': 90},
            {'name': 'Karen Ramos', 'email': 'caitlin47@example.net', 'anzahl': 9},
            {'name': 'Michael Webb', 'email': 'lindsay78@example.org', 'anzahl': 75},
            {'name': 'Deborah Nelson', 'email': 'steven72@example.net', 'anzahl': 61},
            {'name': 'Mrs. Janet Hicks', 'email': 'crawfordkyle@example.net', 'anzahl': 40},
            {'name': 'Cassie Bonilla', 'email': 'jenniferbird@example.org', 'anzahl': 1},
            {'name': 'Isaac Johnson', 'email': 'jameswilliams@example.net', 'anzahl': 23},
            {'name': 'Allison Tucker', 'email': 'rick76@example.org', 'anzahl': 71},
            {'name': 'Sara Garrett', 'email': 'odonnellpatrick@example.net', 'anzahl': 94},
            {'name': 'Lauren Anderson', 'email': 'james40@example.org', 'anzahl': 75},
            {'name': 'Jessica Harris', 'email': 'jenkinsalexander@example.org', 'anzahl': 46},
            {'name': 'Dale Fry', 'email': 'jsanchez@example.org', 'anzahl': 59},
            {'name': 'Jackson Wilson', 'email': 'martin70@example.com', 'anzahl': 72},
            {'name': 'Shannon Padilla', 'email': 'ryan71@example.org', 'anzahl': 73},
            {'name': 'Kara Olson', 'email': 'ihughes@example.org', 'anzahl': 63},
            {'name': 'Jessica Garcia', 'email': 'william41@example.org', 'anzahl': 93},
            {'name': 'Erin Meyer', 'email': 'amyporter@example.net', 'anzahl': 90},
            {'name': 'Mary Snyder', 'email': 'silvapaul@example.net', 'anzahl': 68},
            {'name': 'Amber Barber', 'email': 'zmorris@example.net', 'anzahl': 7},
            {'name': 'Thomas Garcia', 'email': 'laurie05@example.org', 'anzahl': 29},
            {'name': 'Dr. Ann Patton', 'email': 'ykelly@example.org', 'anzahl': 92},
            {'name': 'Erin Navarro', 'email': 'anthonyhebert@example.org', 'anzahl': 44},
            {'name': 'Joshua Browning', 'email': 'william87@example.net', 'anzahl': 74},
            {'name': 'Logan Stevens', 'email': 'ryanbradley@example.net', 'anzahl': 84},
            {'name': 'Matthew Barry', 'email': 'annerowe@example.com', 'anzahl': 80}]

# list_dic = [{'name': 'Melanie Reilly', 'email': 'jacksonlopez@example.com', 'anzahl': 40},
# 			{'name': 'Gregory Russell', 'email': 'swilliams@example.net', 'anzahl': 8},
# 			{'name': 'Aaron Ross', 'email': 'kevincline@example.org', 'anzahl': 63},
# 			{'name': 'Meredith Coleman', 'email': 'qvargas@example.com', 'anzahl': 63},
# 			{'name': 'Michael Salazar', 'email': 'patriciasmith@example.net', 'anzahl': 12}
# ]
#
for y in range(len(list_dic) - 1):

    for x in range(len(list_dic) - 1 - y):
        print(list_dic[x]['anzahl'], list_dic[x + 1]['anzahl'])
        if list_dic[x]['anzahl'] > list_dic[x + 1]['anzahl']:
            zw = list_dic[x]
            list_dic[x] = list_dic[x + 1]
            list_dic[x + 1] = zw
for z in list_dic:
    print(z)

for y in range(len(list_dic) - 1):
    for x in range(len(list_dic) - 1 - y):
        if list_dic[x]['anzahl'] > list_dic[x + 1]['anzahl']:
            zw = list_dic[x]
            list_dic[x] = list_dic[x + 1]
            list_dic[x + 1] = zw
        elif list_dic[x]["anzahl"] == list_dic[x + 1]["anzahl"]:
            if list_dic[x]['name'] > list_dic[x + 1]['name']:
                list_dic[x], list_dic[x + 1] = list_dic[x + 1], list_dic[x]

for z in list_dic:
    print(z)
