#!/usr/bin/env python3
import sys, os, json, time, random
# Check to make sure we are running the correct version of Python
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# The game and item description files (in the same folder as this script)
game_file = 'zork.json'
item_file = 'items.json'
class Sahir(object):
    def __init__(self):
        self.inventory = []
        self.gold = 0
# Load the contents of the files into the game and items dictionaries. You can largely ignore this
# Sorry it's messy, I'm trying to account for any potential craziness with the file location
def load_files():
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, game_file)) as json_file: game = json.load(json_file)
        with open(os.path.join(__location__, item_file)) as json_file: items = json.load(json_file)
        return (game,items)
    except:
        print("There was a problem reading either the game or item file.")
        os._exit(1)

def render(game, current):
    c = game[current]
    print(c["desc"])

def get_input(game, current, sahir):
    if(current == "DEMON" or current == "TOWN1" or current == "TUTOR" or current == "STEAL"):
        print()
        time.sleep(5)
        response = 'ON'
    elif(current == "BREAD"):
        if("gold" in sahir.inventory):
            if(gold >= 5):
                gold = gold - 5
                sahir.inventory.append("Bread")
                print("Sahir buys some bread")
            if(gold <= 0):
                sahir.inventory.remove("gold")
        else:
            print("Vendor: You don't got da money kid, GET LOST")
        response = "ON"
    elif(current == "CROOK"):
        print("The man hands Sahir a gold coin. Cloaked Man: Here, this round's on me")
        if("gold" not in sahir.inventory):
            sahir.inventory.append("gold")
        sahir.gold = sahir.gold + 1
        follow = True
        while(follow == True):
            if("gold" not in sahir.inventory):
                follow = False
            while(sahir.gold > 0):
                print("You have " + str(sahir.gold) + " gold peices")
                bet = input("Cloaked Man: How much gold would like to bet? ")
                pOP = random.randint(1, 100)
                if(pOP < 15 or pOP > 15):
                    print("You pull out a black peice of paper")
                    print("Cloaked Man: awww... too bad")
                    sahir.gold = sahir.gold - int(bet)
                    if(sahir.gold <= 0):
                        sahir.inventory.remove("gold")
                    if(sahir.gold > 0):
                        tryA = input("Cloaked Man: wanna play again? (Y/N)")
                        if(tryA.lower == "y"):
                            follow = True
                        elif(tryA.lower == "n"):
                            follow = False
                        else:
                            print("Cloaked Man: Do you take me for a fool, come back when your ready to play right!!")
                elif(pOP == 15):
                    print("You pull out a white peice of paper")
                    print("Cloaked Man: good grab^^^")
                    if("gold" not in sahir.inventory):
                        sahir.inventory.append("gold")
                    sahir.gold = sahir.gold + (int(bet) * 2)
                    tryA = input("Cloaked Man: wanna play again? (Y/N)")
                    if(tryA.lower == "y"):
                        follow = True
                    elif(tryA.lower == "n"):
                        follow = False
                    else:
                        print("Cloaked Man: Do you take me for a fool, come back when your ready to play right!!")
        response = "ON"
        print()
    elif(current == "CHASE"):
        print("The guard looks at the commotion and yells...")
        print("Guard: HEY KID!!")
        time.sleep(2)
        print("")
        time.sleep(2)
        print("As Sahir is running, he trips over a corpet for sale and ", end = "")
        if("bread" in sahir.inventory):
            print("drops the bread.")
            sahir.inventory.remove("bread")
        elif("gold" in sahir.inventory):
            print("drops all his gold")
            sahir.gold = 0
            sahir.inventory.remove("gold")
        else:
            print("curls up on the ground")
        time.sleep(2)
        print("")
        print("The guard catches up to Sahir and starts kicking him while he's curled up on the ground")
        time.sleep(2)
        print("Guard: THIS OUTTA TEACH YOU SCOUNDREL, YOU STREETRAT!!!")
        time.sleep(2)
        print("")
        print("When the guard stops, he walks away, and Sahir crawls into a dark alley")
        time.sleep(2)
        print("He starts crying and only stops when he hears...")
        time.sleep(2)
        print("Alley Guy: What's wrong kid? You just now figured out the the rich guards are a bit classist?")
        time.sleep(2)
        print("Sahir looks up from where he was sitting and sees an old man looking at him, huddled over against the wall")
        time.sleep(2)
        print("Sahir nodded")
        time.sleep(2)
        print("Alley Guy: Haha, I thought so. Everyone who wakes up hungry in the morning finds out sooner or later")
        time.sleep(2)
        print("The man lifts his head up so Sahir can see two glowing eyes, one green and one yellow")
        time.sleep(2)
        print("Alley Guy: You know, if I had the strength, I'd grab this treasure that's deep in Vangadar Cave")
        print("But I hear it's guarded by traps and stuff, It would take a real strong and smart person to do it")
        print("All I can do is keep the key safe")
        time.sleep(2)
        print("The man holds out a stone sphere with a small emerald in the side")
        time.sleep(2)
        print("Sahir gets a twinkle in his eyes at the sound of the idea of a treasure, for the taking")
        time.sleep(2)
        print("He held out his hand and put a serious look on his face")
        time.sleep(2)
        print("Alley Guy: What? You wanna do it? Really? You could die")
        time.sleep(2)
        print("Sahir nods and looks at the sphere")
        time.sleep(2)
        print("Alley Guy: Fine I guess, If it'll make you happy, hopefully you can get it")
        time.sleep(2)
        print("The man places the sphere in Sahir's outstreched hand")
        sahir.inventory.append("Key")
        time.sleep(2)
        print("Alley Guy: Just remember, when the stones all show themselves, the answer isn't in the glitter")
        time.sleep(2)
        print("Sahir gets up and heads off to Vangadar Cave, a mile outside of town")
        time.sleep(2)
        print("After 2 hours, Sahir finally gets to the cave's mouth")
        print()
        response = "ON"
    elif(current == "LEFT"):
        Puzz = False
        while(Puzz == False):
            responsee = input("What word comes next? ")
            if(responsee.upper() != "SIN"):
                print("That is incorrect, please try again")
                print()
            else:
                print("Correct")
                print("The wall opens and Sahir sees 7 orbs of different colors, equal in size to a baseball")
                print("The colors are: RED, PINK, GREEN, WHITE, BLACK, VIOLET, and YELLOW")
                print()
                Puzz = True
        response = "SIN"
    elif(current == "ORBS"):
        orbTake = input("Would you like to take one of the orbs? (Y/N)")
        if(orbTake.upper() == "Y"):
            take = True
        elif(orbTake.upper() == "N"):
            take = False
        while(take == True):
                orb = input("Which orb would you like to take?")
                sahir.inventory.append(orb.upper() + "orb")
                print("Sahir picked up the orb")
                orbTake = input("Would you like to take another orb? (Y/N)")
                if(orbTake.upper() == "Y"):
                    take = True
                elif(orbTake.upper() == "N"):
                    take = False
                print()
        response = "DONE"
    elif(current == "RIGHT"):
        Puzz = False
        while(Puzz == False):
            responsee = input("What word comes next? ")
            if(responsee.upper() != "SALOR"):
                print("That is incorrect, please try again")
                print()
            else:
                print("Correct")
                print("The wall opens and Sahir sees a sword stuck in the stone")
                print()
                Puzz = True
        response = "SALOR"
    elif(current == "SWORD"):
        sword = input("Would you like to take the sword? (Y/N)")
        if(sword == "Y"):
            print("Sahir took the sword")
            sahir.inventory.append("Sword")
        elif(sword =="N"):
            print("Oh... Ok")
        response = "DONE"
    elif(current == "CENT"):
        takenOrbs = []
        if("GREEN orb" in sahir.inventory):
            print("The GREEN ORB shines, curiously Sahir puts the orb into a hole on the wall")
            sahir.inventory.remove("GREEN orb")
            takenOrbs.append("GREEN orb")
        if("WHITE orb" in sahir.inventory):
            print("The WHITE ORB shines, curiously Sahir puts the orb into a hole on the wall")
            sahir.inventory.remove("WHITE orb")
            takenOrbs.append("WHITE orb")
        if("RED orb" in sahir.inventory):
            print("The RED ORB shines, curiously Sahir puts the orb into a hole on the wall")
            sahir.inventory.remove("RED orb")
            takenOrbs.append("RED orb")
        if("YELLOW orb" in sahir.inventory):
            print("The YELLOW ORB shines, curiously Sahir puts the orb into a hole on the wall")
            sahir.inventory.remove("YELLOW orb")
            takenOrbs.append("YELLOW orb")
        if("VIOLET orb" in sahir.inventory):
            print("The VIOLET ORB shines, curiously Sahir puts the orb into a hole on the wall")
            sahir.inventory.remove("VIOLET orb")
            takenOrbs.append("VIOLET orb")
        if("BLACK orb" in sahir.inventory):
            print("The BLACK ORB shines, curiously Sahir puts the orb into a hole on the wall")
            sahir.inventory.remove("BLACK orb")
            takenOrbs.append("BLACK orb")
        if("PINK orb" in sahir.inventory):
            print("The PINK ORB shines, curiously Sahir puts the orb into a hole on the wall")
            sahir.inventory.remove("PINK orb")
            takenOrbs.append("PINK orb")
        takenOrbs.sort()
        if(takenOrbs == ["BLACK orb", "GREEN orb", "PINK orb", "RED orb", "VIOLET orb ", "WHITE orb", "YELLOW orb"]):
            print("The door's outline starts to glow. The strange stone begins to pulse a high pitched noise")
            print("Sahir takes out the stone and the final hole begins to glow. Sahir places the stone into the hole")
            response = "ON"
    else:
        response = input("What would you like Sahir to do?: ")
        print()
    return response

def update(game, current, response):
    c = game[current]
    try:
        for e in c["exits"]:
            if(e["exit"] == response):
                return e["target"]
    except:
        print("That is not a given option")

# The main function for the game
def main():
    sahir = Sahir()
    current = 'DEMON'  # The starting location
    end_game = ['FINAL']  # Any of the end-game locations

    (game,items) = load_files()

    quit = False
    while not quit:
        render(game, current)
        response = get_input(game, current, sahir)
        current = update(game, current, response)
        for local in end_game:
            if local == current:
                render(game, current)
                quit = True

    # Add your code here

# run the main function
if __name__ == '__main__':
	main()