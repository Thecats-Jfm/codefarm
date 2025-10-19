N = North
E = East
S = South
W = West

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

def copy_list(lst):
    ret = []
    for item in lst:
        ret.append(item)
    return ret

def get_pos():
    return (get_pos_x(), get_pos_y())