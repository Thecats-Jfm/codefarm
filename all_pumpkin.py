import utils

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

n = get_world_size()
pumpkin_to_plant_ori = []
for i in range(n):
	for j in range(n):
		pumpkin_to_plant_ori.append( (i, j) )


pumpkin_to_plant = utils.copy_list(pumpkin_to_plant_ori)


while True:

	while len(pumpkin_to_plant) > 0:
		target = pumpkin_to_plant[0]
		pumpkin_to_plant.pop(0)
		path = utils.find_shortest_path(utils.get_pos(), target, n)
		for dir in path:
			move(dir)
		ret = pumpkin_area(target[0], target[1], False)
		if ret:
			pass
		else:
			pumpkin_to_plant.append( target )

	print("All pumpkins ripe, harvested once, replanting all pumpkins")
	harvest()
	pumpkin_to_plant = utils.copy_list(pumpkin_to_plant_ori)
