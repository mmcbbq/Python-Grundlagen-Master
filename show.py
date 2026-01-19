list1 = [22, 27, 317]
list2 = [71, 6, 47]
list3 = [19, 14, 34]
nested_list = [list1, list2, list3]

summe = 0

for liste in nested_list:
	zwischen_summe = 0
	for zahl in liste:
		summe += zahl
		zwischen_summe += zahl
	print(zwischen_summe)
print(summe)

students = ['Ali', 'Mehmet', 'Ali', 'Philipp', 'Sven', 'Alexander', 'Matrix', 'Mohamad', 'Peter', 'Alexander', 'Sascha',
			'Darius', 'Elsa', 'Coskun', 'Grigorius', 'Kaycee', 'Carsten', 'Bader', 'Athanasios']

for name in students:
	for buchstabe in name:
		print(buchstabe, end='')
	print()
