import math
import tkinter
import cPickle
class CardTemplate:
	name = "Card_Name"
	power = 0
	tech = 0
	will = 0
	speed = 0
	level = 1
	experience = 0
	rarity = 1
	# Below should be auto-generated or given a default before being grown
	roll = 0 #dribble
	loss = 0 #steal
	react_spd = 0 #action speed
	observation = 0 #reflexes
	max_HP = 0 #duh
	support = 0 #pass
	defense = 0 #duh
	recovery = 0 #duh
	critical = 0 #duh
	crit_dam = 1.5 #duh
	loss_resist = 0 #counter_resist
	crit_resist = 0 #crit_resist

	HP = 0 # HP actual
	action = 0 #action bar actual (max 100)

	#Skills go here
	points = 0
	active = 1 #skills out of five
	active_text = ""
	active_desc = ""
	passive1 = 0
	passive1_text = ""
	passive1_desc = ""
	passive2 = 0
	passive2_text = ""
	passive2_desc = ""
	passive3_text = ""
	passive3 = 0
	passive3_desc = ""

def init_card(x):
	x.name = "test"
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
	x.passive2_desc = "Incease team will and power by 1 and decrease HP by 1 (x" + str(x.passive2) + ")"
	x.passive3_text = "Preparations"
	x.passive3 = 0
	x.passive3_desc = "Reduce damage taken when attacked by 15% (x" + str(x.passive3) + ")"

def print_basic_stats(x):
	print("Card", "Name", "=", x.name, sep=" ")
	print("Power", "=", x.power, sep=" ")
	print("Tech", "=", x.tech, sep=" ")
	print("Will", "=", x.will, sep=" ")
	print("Speed", "=", x.speed, sep=" ")
	print("Level = ", x.level)
	print("Experience = ", x.experience)
	rar_string = ""
	for i in range(x.rarity):
		rar_string = rar_string + "*"
	print("Rarity = ", rar_string)

def print_adv_stats(x):
	print("Roll = ",x.roll)
	print("Loss = ",x.loss)
	print("Reaction Speed = ", x.react_spd)
	print("Observation = ", x.observation)
	print("HP = ", x.max_HP)
	print("Support = ", x.support)
	print("Defense = ", x.defense)
	print("Recovery = ", x.recovery)
	print("Critical = ", x.critical)
	print("Critical Damage = ", x.crit_dam)
	print("Loss Resistance = ", x.loss_resist)
	print("Critical Resistance = ", x.crit_resist)

def print_skills(x):
	print("Available Skill Points: ", x.points)
	print(x.active_text)
	print(x.active_desc)
	print(x.active,"/5")
	print(x.passive1_text)
	print(x.passive1_desc)
	print(x.passive1,"/5")
	print(x.passive2_text)
	print(x.passive2_desc)
	print(x.passive2,"/5")
	print(x.passive3_text)
	print(x.passive3_desc)
	print(x.passive3,"/5")

def print_card(x):
	print()
	print_basic_stats(x)
	print()
	print_adv_stats(x)
	print()
	print_skills(x) 
	print()

def level_set(x):
	x.level = math.floor(math.log2(x.experience))
	x.points = math.floor(x.level/5) - x.active - x.passive1 - x.passive2 - x.passive3
	if (x.points < 0):
		print("ERROR: Skills Exceed Level")
		exit()

def set_skills(x):
	print_adv_stats(x)
	if (x.points > 0):
		resp = input("Would you like to allocate skill points? (Y/N)")
		if resp == "Y" or resp == "y" or resp == "yes" or resp == "Yes":
			print("Enter points now") # Fill this in later (graphical makes more sense)
		else:
			print("For future reference, you have ",x.points," points available")


test = CardTemplate
init_card(test)
print_card(test)

print("Now setting exp to 1253245352.")
test.experience = 1253245352
print("Now calculating level")
level_set(test)
print("Now printing New Card Stats")
print_card(test)
set_skills(test)
