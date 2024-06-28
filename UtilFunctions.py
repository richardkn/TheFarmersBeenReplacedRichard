def harvest_if_ready():
	if can_harvest():
		harvest()

def till_if_needed():
	if get_ground_type() == Grounds.Turf:
		till()

def untill_if_needed():
	if get_ground_type() == Grounds.Soil:
		till()

def water_if_needed():
	if get_water() <= 0.75:
		waterAvailable = use_item(Items.Water_Tank)
		## If we don't have a water we probably need more tanks
		if waterAvailable == False:
			trade(Items.Empty_Tank)
	
def continue_on():
	if get_pos_y() == 7:
		move(East)
	move(North)

def go_to_start():
	go_to_position(0, 0)

def go_to_position(x, y):
	while get_pos_x() != x:
		move(West)
	while get_pos_y() != y:
		move(North)

def is_not_at_start():
	total = get_pos_x() + get_pos_y()
	return total > 0
	