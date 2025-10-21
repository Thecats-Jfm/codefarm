import utils
clear()

change_hat(Hats.Green_Hat)

n = get_world_size()
print("World size:", n)

plant_dict = {}
plant_list = []

print(len(plant_dict))
while True:
	if len(plant_list) == 0:
		x, y = utils.get_pos()
		plant_dict[(x, y)] = Entities.Tree
		plant_list.append((x, y))
		print("Added plant at:", (x, y))

	x, y = plant_list[0]
	plant_list.pop(0)
	utils.move_to((x, y), n)

	plant_type, (tx, ty) = get_companion()

	print("At position:", (x, y), "Companion plant:", plant_type, "at", (tx, ty))

	utils.move_to((tx, ty), n)
	utils.plant_entity(plant_type)
	utils.move_to((x, y), n)
	while not can_harvest():
		pet_the_piggy()
	harvest()
