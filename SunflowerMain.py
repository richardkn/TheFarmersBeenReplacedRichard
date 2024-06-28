go_to_start()
plant_full_sunflower_filed()
while True:
	harvest_biggest_sunflower()
	go_to_start()
	
def harvest_biggest_sunflower():
	biggestValue = measure()
	biggestXPos = 0
	biggestYPos = 0
	continue_on()
	
	while is_not_at_start():
		if measure() > biggestValue:
			biggestValue = measure()
			biggestXPos = get_pos_x()
			biggestYPos = get_pos_y()
		continue_on()
		
	go_to_position(biggestXPos, biggestYPos)
	harvest()
	plant_sunflower()
	
def plant_full_sunflower_filed():
	plant_sunflower()
	continue_on()
	while is_not_at_start():
		plant_sunflower()
		continue_on()


