import os
import shutil
import time
from playsound import playsound

def readData(rootDir, select):
    path = select
    os.chdir(path)
    rootDir = path
    return rootDir


def readDataFinal(rootDir, select):
    path = "final"
    os.chdir(path)
    return path


def incorrectInp(select):
    while True:
        if select == "ocean" or select == "dig" or select == "wild animals":
            return select
        else:
            print("Invalid input, please try again")
            select = input
            return select



class Tree:
        def __init__(self, cargo, letter, left=None, right=None):
            self.cargo = cargo
            self.letter = letter
            self.left = left
            self.right = right

        def __str__(self):
            return str(self.cargo)


class Tree_three:
    def __init__(self, cargo, left=None, middle=None, right=None):
        self.cargo = cargo
        self.left = left
        self.middle = middle
        self.right = right

    def __str__(self):
        return str(self.cargo)


#Driver program

caveNode = Tree("cave", "a")
shipNode = Tree("ship", "b")

swimNode = Tree("swim", "a", caveNode, shipNode)

exploreNode = Tree("explore ocean", "a")
animalNode = Tree("animal", "b")

vehicleNode = Tree("vehicle", "b", exploreNode, animalNode)

oceanNode = Tree("ocean", "a", swimNode, vehicleNode)

seaNode = Tree("sea", "a")
dinosaurNode = Tree("dinosaur", "b")

animalsNode = Tree("animals", "a", seaNode, dinosaurNode)

landNode = Tree("land", "a")
underwaterNode = Tree("underwater", "b")

citiesNode = Tree("cities", "b", landNode, underwaterNode)

digNode = Tree("dig", "b", animalsNode, citiesNode)

flyNode = Tree("fly", "a")
climbNode = Tree("climb", "b")

mountainsNode = ("mountains", "a", flyNode, climbNode)

elephantNode = Tree("elephant", "a")
birdsNode = Tree("birds", "b")

jungleNode = Tree("jungle", "b", elephantNode, birdsNode)

wildNode = Tree("wild animals", "c", mountainsNode, jungleNode)

rootNode = Tree("main", "a", oceanNode, wildNode)

currentNode = rootNode
leftNode = currentNode.left
rightNode = currentNode.right
rootDir = "example_story"
finalDir = "example_story/final"
os.chdir(rootDir)
count = 0
playsound('question.mp3')
finalSelect = ""

repeat = True

while repeat:
    for x in range(3):
        count += 1
        leftNode = currentNode.left
        rightNode = currentNode.right
        print("Options are ", leftNode.cargo, " and ", rightNode.cargo)
        select = input("Enter word selection: ")                                        # 1
        #if select != "ocean" or select != "dig" or select != "wild animals":
        #   select = incorrectInp(select)
        #print(leftNode)
       # print(rightNode)
        print("does ", leftNode.cargo, " equal ", select)
        #print("does " + rightNode.cargo + " equal " + select)
        if leftNode.cargo == select:
            currentNode = leftNode
            print("yes")
        elif rightNode.cargo == select:
            currentNode = rightNode
        else:
            currentNode = digNode
        print(currentNode)

        currDir = readData(rootDir, currentNode.letter)
        finalSelect = finalSelect+currentNode.letter
        print("finalSelect is ", finalSelect)

        if count == 3:
            print(os.getcwd())
            os.chdir('..')                                  #goes up to orig directory
            os.chdir('..')
            os.chdir('..')
            print(os.getcwd())
            playsound(finalSelect + '.wav')
        else:
            playsound(currentNode.letter + '.wav')

    repeatString = input("Would you like to repeat the game? Type yes/no")
    if repeatString == "yes":
        currentNode = rootNode
        leftNode = currentNode.left
        rightNode = currentNode.right
        rootDir = "example_story"
        finalDir = "example_story/final"
        os.chdir(rootDir)
        count = 0
        playsound('question.mp3')
        finalSelect = ""

        repeat = True
    else:
        repeat = False


'''select = input("Enter letter selection: ")                  #2
if select != "a" or select != "b" or select != "c":
    select = incorrectInp(select)
currDir = readData(currDir, select)
playsound(select + '.wav')                                  # in a.wav, "This is A"
finalSelect = finalSelect+select

select = input("Enter word selection: ")                  #3
currDir = readDataFinal(currDir, select)                     # in a.wav, "This is A", "This is B"
finalSelect = finalSelect + select
playsound(finalSelect + '.wav')'''

#should loop to the original after reading final one
#loop initial part


#You CHOOSE cave and that'll give you the complete, concatenated string.
#then go up a little in the directory, go into the final folder and play the wav there



'''
""" Write the body of the function that will be executed once the intent is recognized. 
In your scope, you have the following objects : 
- intentMessage : an object that represents the recognized intent
- hermes : an object with methods to communicate with the MQTT bus following the hermes protocol. 
- conf : a dictionary that holds the skills parameters you defined. 
  To access global parameters use conf['global']['parameterName']. For end-user parameters use conf['secret']['parameterName'] 
 
Refer to the documentation for further details. 
""" 


house_room = intentMessage.slots.wordsSlot.first().value # We extract the value from the slot "house_room"

result_sentence = ""

result_sentence = "Awesome! You want to be a  : {}".format(str(house_room))  # The response that will be said out loud by the TTS engine.


current_session_id = intentMessage.session_id
hermes.publish_end_session(current_session_id, result_sentence)
'''
