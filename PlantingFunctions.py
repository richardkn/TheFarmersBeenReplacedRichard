def plant_grass():
	untill_if_needed()
	water_if_needed()

def plant_wood():
	if get_pos_x() % 2 == 0:
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)
	water_if_needed()
		
def plant_carots():
	till_if_needed()
	if get_entity_type() == None:
		trade(Items.Carrot_Seed)
		plant(Entities.Carrots)
	water_if_needed()
		
def plant_pumpkin():
	till_if_needed()
	if get_entity_type() == None:
		trade(Items.Pumpkin_Seed)
		plant(Entities.Pumpkin)
	water_if_needed()
	

def plant_sunflower():
	if get_entity_type() != Entities.Sunflower:
		harvest()
	
	till_if_needed()
	trade(Items.Sunflower_Seed)
	plant(Entities.Sunflower)
	water_if_needed()