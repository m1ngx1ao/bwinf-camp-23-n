from input_leser import leser
zeilen = leser()

def hole_wuensche(): 
	wuensche = []
	for wunsch in range(2, len(zeilen)):
		w = zeilen[wunsch].split(" ")
		w[2] = int(w[2])
		wuensche.append(w)
	return wuensche

def hole_nachbar(koor : int, beet: list[str]) -> list[str]:
	if koor == 0:
		return [beet[1], beet[2]]
	if koor == 1:
		return [beet[0], beet[2], beet[3], beet[4]]
	if koor == 2:
		return [beet[0], beet[1], beet[4], beet[5]]
	if koor == 3:
		return [beet[1], beet[4], beet[6]]
	if koor == 4:
		return [beet[1], beet[2], beet[3], beet[5], beet[6], beet[7]]
	if koor == 5:
		return [beet[2], beet[4], beet[7]]
	if koor == 6:
		return [beet[3], beet[4], beet[7], beet[8]]
	if koor == 7:
		return [beet[4], beet[5], beet[6], beet[8]]
	if koor == 8:
		return [beet[6], beet[7]]
	assert False

def hole_punktzahl(beet: list[str]) -> int:
	wuensche = hole_wuensche()
	punktzahl = 0
	for wunsch in wuensche:
		for blume_index in range(0, len(beet) - 1):
			if wunsch[0] == beet[blume_index]:
				nachbarn = hole_nachbar(blume_index, beet)
				for nachbar in nachbarn:
					if wunsch[1] == nachbar:
						punktzahl += wunsch[2]
	return punktzahl

def mache_beet() -> list[str]:
	moeglichen_farben = ["rot", "tuerkis", "rosa", "gelb", "blau", "orange", "gruen"]
	anzahl_farben = int(zeilen[0])
	farben_beet = []
	anzahl = 0
	index = 0
	for wunsch in hole_wuensche():
		for _ in range(2):
			if anzahl <= anzahl_farben:
				if wunsch[index] not in farben_beet:
					farben_beet.append(wunsch[index])
					anzahl += 1
				index = 1 - index
	for moegliche_farbe in moeglichen_farben:
		if anzahl <= anzahl_farben:
			if moegliche_farbe not in farben_beet:
				farben_beet.append(moegliche_farbe)
				anzahl += 1
	beet = [None, None, None, None, None, None, None, None, None, None]
	bestes_beet = []
	beste_punktzahl = 0
	for farbe in farben_beet:
		beet[0] = farbe
		for farbe in farben_beet:
			beet[1] = farbe
			for farbe in farben_beet:
				beet[2] = farbe
				for farbe in farben_beet:
					beet[3] = farbe
					for farbe in farben_beet:
						beet[4] = farbe
						for farbe in farben_beet:
							beet[5] = farbe
							for farbe in farben_beet:
								beet[6] = farbe
								for farbe in farben_beet:
									beet[7] = farbe
									for farbe in farben_beet:
										beet[8] = farbe
										for farbe in farben_beet:
											beet[9] = farbe
											richtige_farben = True
											for farbe in farben_beet:
												if farbe not in beet:
													richtige_farben = False
													break
										if hole_punktzahl(beet) > beste_punktzahl and richtige_farben:
											beste_punktzahl = hole_punktzahl(beet)
											bestes_beet = beet
											print(bestes_beet, beste_punktzahl)
	return bestes_beet, beste_punktzahl

print(mache_beet())