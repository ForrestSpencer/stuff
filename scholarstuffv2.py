names = ['Gabe', 'Clara','Ben','Caleb','Danielle']
rounds = ['Round 1','Round 2','Round 3','the Quarterfinals','the Semifinals','the Finals']
round1scores = ['0','130','10','0','0']
round2scores = ['20','100','10','0','0']
round3scores = ['30','90','0','0','0']
roundquarterscores = ['40','80','0','10','0']
roundsemiscores = ['40','110','10','0','0']
roundfinalscores = ['60','70','0','0','0']
totalroundscores = ['430','370','360','300','480','370']
def scores(name):
	for namez in names:
		if name == 'Gabe':
			x = names[0] 
			y = round1scores[0]
			z = round2scores[0]
			q = round3scores[0]
			w = roundquarterscores[0]
			e = roundsemiscores[0]
			r = roundfinalscores[0]
			t = 0
		if name == 'Clara':
			x = names[1] 
			y = round1scores[1]
			z = round2scores[1]
			q = round3scores[1]
			w = roundquarterscores[1]
			e = roundsemiscores[1]
			r = roundfinalscores[1]
			t = 0
		if name == 'Ben':
			x = names[2] 
			y = round1scores[2]
			z = round2scores[2]
			q = round3scores[2]
			w = roundquarterscores[2]
			e = roundsemiscores[2]
			r = roundfinalscores[2]
			t = 0
		if name == 'Caleb':
			x = names[3] 
			y = round1scores[3]
			z = round2scores[3]
			q = round3scores[3]
			w = roundquarterscores[3]
			e = roundsemiscores[3]
			r = roundfinalscores[3]
			t = 0
		if name == 'Danielle':
			x = names[4] 
			y = round1scores[4]
			z = round2scores[4]
			q = round3scores[4]
			w = roundquarterscores[4]
			e = roundsemiscores[4]
			r = roundfinalscores[4]
			t = 0
	
	for roundz in rounds:
		if name == 'Round 1':
			x = rounds[0] 
			y = totalroundscores[0]
			t = 1
		if name == 'Round 2':
			x = rounds[1] 
			y = totalroundscores[1]
			t = 1
		if name == 'Round 3':
			x = rounds[2] 
			y = totalroundscores[2]
			t = 1
		if name == 'Quarterfinals':
			x = rounds[3] 
			y = totalroundscores[3]
			t = 1
		if name == 'Semifinals':
			x = rounds[4] 
			y = totalroundscores[4]
			t = 1
		if name == 'Finals':
			x = rounds[5] 
			y = totalroundscores[5]
			t = 1
	if t: 
		print("\nThe team got %s points in %s."%( y, x))
	else:
		print("\n%s got %s points in round 1, %s points in round 2, %s points in round 3, %s points in the Quarterfinals, %s points in the Semifinals, and %s points in the Finals."%( x, y, z, q, w, e, r))
	
scores('')
