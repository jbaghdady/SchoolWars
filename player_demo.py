import pickle
import os.path

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

def init_card(x):
	x.name = "Bright Eyes"
	x.power = 10
	x.tech = 10
	x.will = 10
	x.speed = 10
	x.level = 1
	x.experience = 0
	x.rarity = 3
	# Below should be auto-generated or given a default before being grown
	x.roll = 12 #dribble
	x.loss = 12 #steal
	x.react_spd = 12 #action speed
	x.observation = 12 #reflexes
	x.max_HP = 18 #duh
	x.support = 12 #pass
	x.defense =  12 #duh
	x.recovery = 12 #duh
	x.critical = 12 #duh
	x.crit_dam = 1.2 #duh
	x.loss_resist = 12 #counter_resist
	x.crit_resist = 12 #crit_resist

	x.HP = x.max_HP # HP actual
	x.action = 0 #action bar actual (max 100)

	#Skills go here
	x.active = 1 #skills out of five
	x.active_text = "The future is ours!"
	x.active_desc = "Increase strike by 7.5% (x" + str(x.active) + ")"
	x.passive1 = 0
	x.passive1_text = "Unbound"
	x.passive1_desc = "Increase Critical Resistance and Loss Resistance by 10% (x" + str(x.passive1) +")"
	x.passive2 = 0
	x.passive2_text = "Complete Notes"
	x.passive2_desc = "Increase Attack and Defense by 5 (x" + str(x.passive2) + ")"
	x.passive3_text = "Prepared"
	x.passive3 = 0
	x.passive3_desc = "Reduce damage taken when attacked by 5% (x" + str(x.passive3) + ")"


def gen_player(x,usename):
	x.userID = usename
	x.rank = 1
	x.grade = "C"
	loadme = CardTemplate()
	init_card(loadme)
	x.avatar = loadme
	x.funds = 1000
	x.alignment = "General"
	x.roster[0] = loadme


def recovery_user(address,useid):
	print("Loading Account.")
	f = open(address,"rb")
	useid = pickle.load(f)
	f.close()

def create_user(address,useid,usename):
	print("Creating a new Account!")
	gen_player(useid, usename)
	fh = open(address,"wb")
	pickle.dump(useid,fh)
	fh.close()
	print("Account created and saved!")

print("Now Running Player Account Demo.")
usename = input("Please Enter UserID: ")
address = usename + ".p"
if os.path.isfile(address):
	print("Loading Account.")
	f = open(address,"rb")
	f.seek(0)
	useid = pickle.load(f)
	f.seek(0)
	f.close()
else:
	useid = Player()
	create_user(address,useid,usename)

print("")
print("Printing Stats")
print("")
print(useid.userID)
print(useid.rank)
print(useid.grade)
print(useid.avatar.name)
print(useid.funds)
print(useid.alignment)
print(useid.roster[0].name)
