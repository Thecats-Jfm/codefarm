def try_harvest(do_action=True):
	if can_harvest():
		if do_action:
			harvest()
		return True
	return False

clear()

def pumpkin_area(i, j, harvest_pumpkins_this_round):
	if get_ground_type() != Grounds.Soil:
		till()
	# print("Pumpkin area at", i, j, "harvest this round:", harvest_pumpkins_this_round)
	ret = try_harvest( harvest_pumpkins_this_round)
	plant(Entities.Pumpkin)
	return ret

def carrot_area(i, j):
	if get_ground_type() != Grounds.Soil:
		till()
	try_harvest()
	plant(Entities.Carrot)

def sunflower_area(i, j):
	if get_ground_type() != Grounds.Soil:
		till()
	try_harvest()
	plant(Entities.Sunflower)


n = get_world_size()
print("World size:", n)

sunflower_size = 1
pumpkin_size = 8
carrot_size = 7
# bush_size = n*2 // 3
bush_size = n

harvest_pumpkins_this_round = False

while True:
	all_pumpkins_alive = True
	print("New pass, harvest pumpkins this round:", harvest_pumpkins_this_round)
	for j in range(get_world_size()):
		for i in range(get_world_size()):
			# while can_harvest():
			#     pass

			if i < carrot_size:
				if j < sunflower_size:
					sunflower_area(i, j)
				elif j < pumpkin_size:
					all_pumpkins_alive = pumpkin_area(i, j, harvest_pumpkins_this_round) and all_pumpkins_alive
				else:
					carrot_area(i, j)

			elif i < bush_size and (i+j) % 2 == 0:
				# tree!!
				if can_harvest():
					harvest()
				plant(Entities.Tree)
			else:
				# grass area
				if can_harvest():
					harvest()


			move(North)
		move(East)

	harvest_pumpkins_this_round = all_pumpkins_alive and not harvest_pumpkins_this_round