class CardTemplate:
	def __init__(self):
		self.name = "Card_Name"
		self.power = 0
		self.tech = 0
		self.will = 0
		self.speed = 0
		self.level = 1
		self.experience = 0
		self.rarity = 1
		# Below should be auto-generated or given a default before being grown
		self.roll = 0 #dribble
		self.loss = 0 #steal
		self.react_spd = 0 #action speed
		self.observation = 0 #reflexes
		self.max_HP = 0 #duh
		self.support = 0 #pass
		self.defense = 0 #duh
		self.recovery = 0 #duh
		self.critical = 0 #duh
		self.crit_dam = 1.5 #duh
		self.loss_resist = 0 #counter_resist
		self.crit_resist = 0 #crit_resist

		self.HP = 0 # HP actual
		self.action = 0 #action bar actual (max 100)

		#Skills go here
		self.points = 0
		self.active = 1 #skills out of five
		self.active_text = ""
		self.active_desc = ""
		self.passive1 = 0
		self.passive1_text = ""
		self.passive1_desc = ""
		self.passive2 = 0
		self.passive2_text = ""
		self.passive2_desc = ""
		self.passive3_text = ""
		self.passive3 = 0
		self.passive3_desc = ""

class Field_Effect:
	def __init__(self):
		self.effect = "" #description
		self.modifier = 1
		self.type = "" #matching stat

class Field:
	def __init__(self):
		self.fl = CardTemplate()
		self.fc = CardTemplate()
		self.fr = CardTemplate()
		self.ml = CardTemplate()
		self.mc = CardTemplate()
		self.mr = CardTemplate()
		self.dl = CardTemplate()
		self.dc = CardTemplate()
		self.dr = CardTemplate()
		self.core = CardTemplate()
		self.map = Field_Effect()
	def print_front(self):
		print("F |  ",self.fl.name," | ", self.fc.name, " | ", self.fr.name, " | ")
	def print_middle(self):
		print("M |  ",self.ml.name," | ", self.mc.name, " | ", self.mr.name, " | ")
	def print_defense(self):
		print("D |  ",self.dl.name," | ", self.dc.name, " | ", self.dr.name, " | ")
	def print_core(self):
		print("C                      | ", self.core.name, " |")
	def print_state(self):
		print("-----------------------------------------")
		self.print_front()
		print("-----------------------------------------")
		self.print_middle()
		print("-----------------------------------------")
		self.print_defense()
		print("-----------------------------------------")
		self.print_core()
		print("-----------------------------------------")

def init_card(x, value):
	x.name = value
	x.power = 12
	x.tech = 12
	x.will = 12
	x.speed = 12
	x.level = 1
	x.experience = 0
	x.rarity = 5
	# Below should be auto-generated or given a default before being grown
	x.roll = 15 #dribble
	x.loss = 15 #steal
	x.react_spd = 15 #action speed
	x.observation = 15 #reflexes
	x.max_HP = 21 #duh
	x.support = 15 #pass
	x.defense =  15 #duh
	x.recovery = 15 #duh
	x.critical = 15 #duh
	x.crit_dam = 1.5 #duh
	x.loss_resist = 15 #counter_resist
	x.crit_resist = 15 #crit_resist

	x.HP = x.max_HP # HP actual
	x.action = 0 #action bar actual (max 100)

	#Skills go here
	x.active = 1 #skills out of five
	x.active_text = "Huh. So that's a thing that can happen."
	x.active_desc = "Increase Reflexes and steal by 20% (x" + str(x.active) + ")"
	x.passive1 = 0
	x.passive1_text = "Blue Hoodie"
	x.passive1_desc = "Increase Defense, Recovery, and max HP by 3% (x" + str(x.passive1) +")"
	x.passive2 = 0
	x.passive2_text = "Oversight"
	x.passive2_desc = "Increase team will and power by 1 and decrease HP by 1 (x" + str(x.passive2) + ")"
	x.passive3_text = "Preparations"
	x.passive3 = 0
	x.passive3_desc = "Reduce damage taken when attacked by 15% (x" + str(x.passive3) + ")"


demo_field = Field()
test1 = CardTemplate()
init_card(test1,"Forward Left")
test2 = CardTemplate()
init_card(test2,"Forward Center")
test3 = CardTemplate()
init_card(test3, "Forward Right")
test4 = CardTemplate()
init_card(test4, "Middle Left")
test5 = CardTemplate()
init_card(test5, "Middle Center")
test6 = CardTemplate()
init_card(test6, "Middle Right")
test7 = CardTemplate()
init_card(test7, "Defense Left")
test8 = CardTemplate()
init_card(test8, "Defense Center")
test9 = CardTemplate()
init_card(test9, "Defense Right")
core = CardTemplate()
init_card(core, "Core")
demo_field.fl = test1
demo_field.fc = test2
demo_field.fr = test3
demo_field.ml = test4
demo_field.mc = test5
demo_field.mr = test6
demo_field.dl = test7
demo_field.dc = test8
demo_field.dr = test9
demo_field.core = core

print("Now Displaying Field")
demo_field.print_state()
