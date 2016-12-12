import time
import random

def start():
	name = "Dasini's Masion"
	print "Welcome to %s, where you have to defeat all the monsters and survive the 7 hours until daybreak. Be sure to spell correctly, you will be deducted HP if you dont do it right. Type play to start." % name
	usr = raw_input('>>>').lower()
	
	if usr == "play":
		global usrname
		usrname = raw_input("Enter your user name: \n>>>").capitalize()
		startGame()
	
	else:
		start()
	
def startGame():
	print "Welcome to the Mansion, %s. All of your friends have already been killed, can you stay alive for these 7 hours until day break?" % usrname
	time.sleep(1)
	goal = input("How many hours can you last?\n>>>")
	
	global difficulty
	global hp
	global timeleft
	global monsters
	global loot
	loot = 4
	monsters = ["Goul","Zombie","Werewolf","Boogieman","Vampire"]
	timeleft = 7
	
	if type(goal) == int or type(goal) == float:
		if goal > 7:
			print "Thats more than 7, smartass, set to 7. Since you decided to test me, difficulty set to 'Extreme'. Goodluck you'll need it \n"
			goal = 7
			difficulty = 2
		elif goal > 5:
			print "Goodluck, you'll need it. Difficulty set to Hard \n"
			difficulty = 1.5
		else:
			print "Youre honest. I like you. Difficulty set to Casual \n"
			difficulty = 1
	
	else:
		print "Umm, try again."
		startGame()
	
	time.sleep(1)
	hp = random.randint(25, 30) - (difficulty * 2) + random.randint(0, 5)
	print "You have %d HP left after the attack." % hp
	time.sleep(3)
	print "\n" * 20
	time.sleep(4)
	
	rmselect()
	
def rmselect():
	global startrm
	global rms
	global currentrm
	rms = ["Living","Dining", "Kitchen","Loft","Bathroom","Library","Bedroom","Theater"]
	print "The mansion is huge! Ever since Mr Peters died, all his loot has just been sitting here. Waiting for someone to take it, so why not us?:"
	time.sleep(3)
	print "We were in here to collect all the loot."
	time.sleep(1)
	print "You still have 4 in you pocket"
	time.sleep(2)
	print "The rooms we havent searched yet are these:"
	time.sleep(1.5)
	print ', '.join(rms)
	time.sleep(3)
	startrm = raw_input("What room are you in?\n>>>").capitalize()
	currentrm = startrm
	if startrm in rms:
		print "\n\nWell I dont see any monsters in here. \n\n"
		time.sleep(1)
		print "Wait, whats that noise? \n\n"
		time.sleep(1)
		print"I... I think it came from the closet.\n\n"
		time.sleep(1)
		print "Should we go check out the noise in the closet, or leave?\nType C for closet or L for leave"
		move = raw_input(">>>").upper()
		if move == "L":
			leave()
		elif move == "C":
			look()
		else:
			print "That wasnt an option. Try again"
	else:
		print "Umm, thats not a room. Try again.\n\n"
		rmselect()
def look():
	global timeleft
	global hp
	global randomnum
	global hploss
	global startrm
	global currentrm
	global monster
	global lootfound
	global loot
	chances = [1,2,3,4,5,6,4,5,6,7,8]
	randomnum = random.choice(chances)
	hploss = randomnum * difficulty
	monster = random.choice(monsters)
	lootfound = (random.choice(chances) * difficulty) / random.randint(2,3)
	time.sleep(1)
	print "Oh my, its a %s." % monster
	time.sleep(1)
	
	if randomnum < 4:
		print "It jumped out, hit you. -%d hp" % hploss
		hp = hp - hploss
	
	elif randomnum < 8:
		print "You hit it, but it didnt die. It lahsed out against you. %d hp to %s, %d hp to you" % (randomnum, monster, hploss)
		hp = hp - hploss
		time.sleep(1)
		action = raw_input("Do you run, or strike again? R for run, or S for strike\n>>>").upper()
	
		if action == "S":
			print ("You hit it, and killed it, but now your wrist hurts. -%s hp") % difficulty
	
		elif action == "R":
			leave()
	
		else:
			print "Watch your spelling. -%d hp" % randomnum
			hp = hp - randomnum
	
		hp = hp - difficulty
	
	else:
		global hp
		print ("You hit it, and killed it, but now your wrist hurts. -%s hp") % difficulty
		hp = hp - difficulty * random.randint(1,2)
	
	print "You found %d loot" % lootfound
	
	loot = loot + lootfound
	time.sleep(1)
	timeleft = timeleft - 1
	
	if hp > 0:
		print "You have %d hp left" % hp
	
	elif hp < 0:
		GameOver()
	
	time.sleep(1)
	
	if timeleft == 0:
		Won()
	
	else:
		print "You have %s hours until daybreak." % timeleft
	time.sleep(1)
	print "You have found a total of %d loot." % loot
	leave()

def leave():
	global rms
	global currentrm
	global monsters
	global monster
	global hp
	monster = random.choice(monsters)
	rms.remove(currentrm)
	time.sleep(1)
	print "\nYou leave  the %s, which room do you want to search next?" % currentrm
	time.sleep(1)
	print ', '.join(rms)
	currentrm = raw_input(">>>").capitalize()
	
	if random.randint(1,7) == 7 or timeleft == 1:
		print "A %s striked you from behind while waliking down the hallway. -%s hp" % (monster, 4 * difficulty)
		hp = hp - (4 * difficulty)
		time.sleep(1)
		print "You pass out from the pain"
		time.sleep(3)
		print "..................................."
		time.sleep(4)
		print "You wake up, but are now droggy"
		time.sleep(1)
		print "You continue to the %s" % currentrm
		time.sleep(1)
	
	if currentrm in rms:
		print "You walk to that room, and hear something inside."
		look()
	
	else:
		print "Check spelling"
		currentrm = raw_input("\n>>>").capitalize()
		print "You walk to that room, and hear something inside."
		look()

def GameOver():

	print "Game over, Play again?"
	playagain = raw_input(">>>")
	
	if playagain == "yes":
		startGame()

	else:
		start()
	
def Won():
	
	print "You Won! Play again?"
	playagain = raw_input(">>>")
	
	if playagain == "yes":
		startGame()
	
	else:
		start()
	
	 
start()
