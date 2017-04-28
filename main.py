import time
import random
def callforinput():
	usr = input('>>>').lower()
	return usr
def start():
	usr = callforinput()
    name = "Dasini's Masion"
    print("Welcome to %s, where you have to defeat all the monsters and survive the 7 hours until daybreak. Be sure to spell correctly, you will be deducted   HP if you dont do it right. Type play to start." % name)
    callforinput()

    if usr == "play" or usr == 'start':
        global usrname
        usrname = input("Enter your user name: \n>>>").capitalize()
        startGame()

    else:
        start()


def startGame():
    print("Welcome to the Mansion, %s. All of your friends have already been killed, can you stay alive for these 7 "
          "hours until day break?" % usrname)
    time.sleep(1)
    goal = eval(input("How many hours can you last?\n>>>"))

    global difficulty
    global hp
    global timeleft
    global monsters
    global loot
    loot = 4
    monsters = ["Goul", "Zombie", "Werewolf", "Boogieman", "Vampire", "Ghost"]
    timeleft = 7

    if type(goal) == int or type(goal) == float:
        if goal > 7:
            print("Thats more than 7, set to 7. Since you decided to test me, difficulty set to 'Extreme'. Goodluck you'll need it \n")
            goal = 7
            difficulty = 2
        elif goal > 5:
            print("Goodluck, you'll need it. Difficulty set to Hard \n")
            difficulty = 1.5
        else:
            print("Youre honest. I like you. Difficulty set to Casual \n")
            difficulty = 1

    else:
        print("Umm, try again.")
        startGame()

    time.sleep(1)
    hp = random.randint(25, 30) - (difficulty * 2)
    print("You have %d HP left after the attack." % hp)
    time.sleep(3)
    print("\n" * 20)
    time.sleep(4)

    rmselect()


def rmselect():
    global rm
    global rms
    global currentrm
    rms = ["Living", "Dining", "Kitchen", "Loft", "Bathroom", "Library", "Bedroom", "Theater", "Foyer", "Laundry",
           "Garage"]
    print("The mansion is huge! Ever since Mr Peters died, all his loot has just been sitting here. Waiting for someone to take it, so why not us?:")
    time.sleep(3)
    print("We were in here to collect all the loot.")
    time.sleep(1)
    print("You still have 4 in you pocket")
    time.sleep(2)
    print("The rooms we havent searched yet are these:")
    time.sleep(1.5)
    print(', '.join(rms))
    time.sleep(3)
    rm = input("What room do you last remember being in?\n>>>").capitalize()
    currentrm = rm
    eval(rm + '.room()')


def leave():
    global rms
    global currentrm
    global monsters
    global monster
    global hp
    monster = random.choice(monsters)
    rms.remove(currentrm)
    time.sleep(1)
    print("\nYou leave  the %s, which room do you want to search next?" % currentrm)
    time.sleep(1)
    print(', '.join(rms))
    currentrm = input(">>>").capitalize()

    if random.randint(1, 7) == 7 or timeleft == 1:
        print("A %s striked you from behind while waliking down the hallway. -%s hp" % (monster, 4 * difficulty))
        hp = hp - (4 * difficulty)
        time.sleep(1)
        print("You pass out from the pain")
        time.sleep(3)
        print("...................................")
        time.sleep(4)
        print("You wake up, but are now droggy")
        time.sleep(1)
        print("You continue to the %s" % currentrm)
        time.sleep(1)

    if currentrm in rms:
        print("You walk to that room, and hear something inside.")
        look()

    else:
        print("Check spelling")
        currentrm = input("\n>>>").capitalize()
        print("You walk to that room, and hear something inside.")
        look()


def GameOver():
    print("Game over, Play again?")
    playagain = input(">>>")

    if playagain == "yes":
        startGame()

    else:
        start()


def Won():
    print("You Won! Play again?")
    playagain = input(">>>")

    if playagain == "yes":
        startGame()

    else:
        start()


start()