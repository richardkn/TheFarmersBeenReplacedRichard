def grow_balanced():
	if get_pos_y()  == 0:
		plant_wood()
	elif get_pos_y() == 1:
		plant_carots()
	elif get_pos_y() == 2:
		plant_pumpkin()
	elif get_pos_y() == 3:
		plant_pumpkin()
	else:
		plantGrass()

def grow_grass():
	if get_pos_y() == 0:
		plant_wood()
	else:
		plant_grass()
			
def grow_carrots():
	if get_pos_y() == 0:
		plant_wood()
	elif get_pos_y() == 1:
		plant_grass()
	else:
		plant_carots()

def grow_pumpkins():
	if get_pos_y() == 0:
		plant_wood()
	elif get_pos_y() == 1:
		plant_grass()
	elif get_pos_y() == 2:
		plant_carots()
	else:
		plant_pumpkin()