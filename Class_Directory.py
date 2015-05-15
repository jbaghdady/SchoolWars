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
		
class ItemTemplate:
	def __init__(self):
		self.item_name = ""
		self.item_alignment = ""
		self.item_rarity = 1
		self.item_desc = ""

class Player:
	def __init__(self):
		self.userID = ""
		self.rank = 0
		self.grade = ""
		self.avatar = CardTemplate()
		self.funds = ""
		self.alignment = ""

		self.roster = [CardTemplate() for i in range(100)]
		self.inventory = [ItemTemplate() for i in range(100)]

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
