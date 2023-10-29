def leser():
	input = []
	f = open('2019 aufgabe 1/input/blumen0.txt')
	zeilen = f.readlines()
	for zeile in zeilen:
		input.append(zeile.rstrip('\n'))
	f.close()
	return input
leser()