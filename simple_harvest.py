while True:
	plant(Entities.Bush)
	if can_harvest():
		harvest()
	else:
		move(North)