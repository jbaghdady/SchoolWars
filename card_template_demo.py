import math
import tkinter
import pickle

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

	def print_basic_stats(self):
		print("Card", "Name", "=", self.name, sep=" ")
		print("Power", "=", self.power, sep=" ")
		print("Tech", "=", self.tech, sep=" ")
		print("Will", "=", self.will, sep=" ")
		print("Speed", "=", self.speed, sep=" ")
		print("Level = ", self.level)
		print("Experience = ", self.experience)
		rar_string = ""
		for i in range(self.rarity):
			rar_string = rar_string + "*"
		print("Rarity = ", rar_string)

	def print_adv_stats(self):
		print("Roll = ",self.roll)
		print("Loss = ",self.loss)
		print("Reaction Speed = ", self.react_spd)
		print("Observation = ", self.observation)
		print("HP = ", self.max_HP)
		print("Support = ", self.support)
		print("Defense = ", self.defense)
		print("Recovery = ", self.recovery)
		print("Critical = ", self.critical)
		print("Critical Damage = ", self.crit_dam)
		print("Loss Resistance = ", self.loss_resist)
		print("Critical Resistance = ", self.crit_resist)

	def print_skills(self):
		print("Available Skill Points: ", self.points)
		print(self.active_text)
		print(self.active_desc)
		print(self.active,"/5")
		print(self.passive1_text)
		print(self.passive1_desc)
		print(self.passive1,"/5")
		print(self.passive2_text)
		print(self.passive2_desc)
		print(self.passive2,"/5")
		print(self.passive3_text)
		print(self.passive3_desc)
		print(self.passive3,"/5")

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
	x.active1 = 1 #skills out of five
	x.active1_text = "Huh. So that's a thing that can happen."
	x.active1_desc = "Increase Reflexes and Steal by 20% (x" + str(x.active1) + ")"
	x.passive1_1 = 0
	x.passive1_1_text = "Blue Hoodie"
	x.passive1_1_desc = "Increase Defense, Recovery, and max HP by 3% (x" + str(x.passive1_1) + ")"
	x.passive1_2 = 0
	x.passive1_2_text = "Oversight"
	x.passive1_2_desc = "Increase team will and power by 1 and decrease HP by 1 (x" + str(x.passive1_2) + ")"
	x.passive1_3_text = "Preparations"
	x.passive1_3 = 0
	x.passive1_3_desc = "Reduce damage taken when attacked by 15% (x" + str(x.passive1_3) + ")"
	
	x.active2 = 2 # Baghs code
	x.active2_text = "Here we go again!"
	x.active2_desc = "Boost Stamina by 10% (x" + str(x.active2) + ")"
	x.passive2_1 = 0
	x.passive2_1_text = "Green Hoodie...Wait. What?"
	x.passive2_1_desc = "Boost max HP by 12% (x" + str(x.passive2_1) + ")"
	x.passive2_2 = 0
	x.passive2_2_text = "What is wrong with this picture?"
	x.passive2_2_desc = "Boost Stamina by 3% and decrease max HP by 10% (x" + str(x.passive2_2) + ")"
	x.passive2_3 = 0
	x.passive2_3_text = "Hands"
	x.passive2_3_desc = "Boost team will by 4% and decrease max HP by 5% (x" + str(x.passive2_3) + ")"
	
	x.active3 = 3
	x.active3_text = "Mine Mine Mine!!!"
	x.active3_desc = "Boost Reflexes and Steal by 25% (x" + str(x.active3) + ")"
	x.passive3_1 = 0
	x.passive3_1_text = "Purple Hoodie."
	x.passive3_1_desc = "Boost Recovery by 5% (x" + str(x.passive3_1) + ")"
	x.passive3_2 = 0
	x.passive3_2_text = "What is right with this picture?"
	x.passive3_2_desc = "Boost HP by 2% and decrease Power by 4% (x" + str(x.passive3_2) + ")"
	x.passive3_3 = 0
	x.passive3_3_text = "CALEBBBBBB!!!!!!! MAKE IT STOPPPPP!!!"
	x.passive3_3_desc = "Boost team will by 2% and increase attack damage 20% (x" + str(x.passive3_3) + ")"
	
	x.active4 = 4
	x.active4_text = "Are we having fun yet?"
	x.active4_desc = "Boost Recovery, Power and max HP by 10% (x" + str(x.active4) + ")"
	x.passive4_1 = 0
	x.passive4_1_text = "Polka-dot Hoodie (You knew it was coming)"
	x.passive4_1_desc = "Boost Recovery by 25% (What else did you expect from polka-dot?) (x" + str(x.passive4_1) + ")"
	x.passive4_2 = 0
	x.passive4_2_text = "I'm beginning to think this isn't really soccer."
	x.passive4_2_desc = "Decrease attack damage by 14% (x" + str(x.passive4_2) + ")"
	x.passive4_3 = 0
	x.passive4_3_text = "And suddenly: Kapadia"
	x.passive4_3_desc = "Decrease Recovery, Power, Stamina, max HP, Reflexes, Defense, Steal by 30% (x" + str(x.passive4_3) + ")"

	x.active5 = 5
	x.active5_text = "A Wild Pikachu Appears!"
	x.active5_desc = "Boost Stamina, max HP and Reflexes by 20% (x" + str(x.active5) + ")"
	x.passive5_1 = 0
	x.passive5_1_text = "RAINBOW HOODIE"
	x.passive5_1_desc = "Decrease attack damage by 50% (x" + str(x.passive5_1) + ")"
	x.passive5_2 = 0
	x.passive5_2_text = "The Neymar"
	x.passive5_2_desc = "Increase max HP, Recovery, Stamina and Reflexes by 40% (x" + str(x.passive5_2) + ")"
	x.passive5_3 = 0
	x.passive5_3_text = "The Bill Reid (aka the Reverse Kapadia)"
	x.passive5_3_desc = "Increase Recovery, Power, Stamina, max HP, Reflexes, Defense Steal by 30% (x" + str(x.passive5_3) + ")"

	
def print_card(x):
	print()
	x.print_basic_stats()
	print()
	x.print_adv_stats()
	print()
	x.print_skills() 
	print()

def level_set(x):
	x.level = math.floor(math.log2(x.experience))
	x.points = math.floor(x.level/5) - x.active - x.passive1 - x.passive2 - x.passive3
	if (x.points < 0):
		print("ERROR: Skills Exceed Level")
		exit()

def set_skills(x):
	x.print_adv_stats()
	if (x.points > 0):
		resp = input("Would you like to allocate skill points? (Y/N)")
		if resp == "Y" or resp == "y" or resp == "yes" or resp == "Yes":
			print("Enter points now") # Fill this in later (graphical makes more sense)
		else:
			print("For future reference, you have ",x.points," points available")


test = CardTemplate()
init_card(test)
print_card(test)

print("Now setting exp to 1253245352.")
test.experience = 1253245352
print("Now calculating level")
level_set(test)
print("Now printing New Card Stats")
print_card(test)
set_skills(test)
