N = North
E = East
S = South
W = West





def Must_Harvest():
	while not can_harvest():
		if get_entity_type() == Entities.Dead_Pumpkin:
			return False
	harvest()
	return True

def WE_NEED_POWER():
	start_tick = get_tick_count()
	n = get_world_size()
	start_power = num_items(Items.Power)
	start_carrots = num_items(Items.Carrot)
	SUB = 7
	leave_cnt = [ [], [], [], [], [], [], [], [], [] ]

	for i in range(n):
		for j in range(n):
			plant_entity(Entities.Sunflower)
			leaf_cnt = measure()
			leave_cnt[leaf_cnt-SUB].append( (i, j) )
			move(N)
		move(E)

	for i in range(9):
		for pos in leave_cnt[8-i]:
			move_to(pos, n)
			harvest()



	end_carrots = num_items(Items.Carrot)
	end_power = num_items(Items.Power)
	end_tick = get_tick_count()
	print("[UseTick]:", end_tick - start_tick, " [Carrots]:", end_carrots - start_carrots, " [Earn Power]:", end_power - start_power)
	do_a_flip()
	pet_the_piggy()


	return True

def repeat_move(direction, times):
	ret = []
	for _ in range(times):
		ret.append(direction)
	return ret

def find_shortest_path(start, goal, world_size):
	# return list
	ret = []
	x1, y1 = start
	x2, y2 = goal

	dis1 = abs(x1 - x2)

	if dis1 < world_size - dis1:
		if x1 < x2:
			ret += repeat_move(E, x2 - x1)
		else:
			ret += repeat_move(W, x1 - x2)
	else:
		if x1 < x2:
			ret += repeat_move(W, world_size - (x2 - x1))
		else:
			ret += repeat_move(E, world_size - (x1 - x2))
	dis2 = abs(y1 - y2)

	if dis2 < world_size - dis2:
		if y1 < y2:
			ret += repeat_move(N, y2 - y1)
		else:
			ret += repeat_move(S, y1 - y2)
	else:
		if y1 < y2:
			ret += repeat_move(S, world_size - (y2 - y1))
		else:
			ret += repeat_move(N, world_size - (y1 - y2))

	return ret

require_check_ground = {Entities.Carrot:Grounds.Soil, Entities.Sunflower:Grounds.Soil, Entities.Pumpkin:Grounds.Soil}
def plant_entity(entity):
	if entity in require_check_ground:
		required_ground = require_check_ground[entity]
		if get_ground_type() != required_ground:
			till()
	plant(entity)




def move_to(target, world_size):
	path = find_shortest_path(get_pos(), target, world_size)
	for dir in path:
		move(dir)

def copy_list(lst):
	ret = []
	for item in lst:
		ret.append(item)
	return ret

def get_pos():
	return (get_pos_x(), get_pos_y())