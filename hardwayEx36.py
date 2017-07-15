import random

#############
## Classes ##
#############

##  This class defines an instance of the Game.
##  Defines a list of rooms for every game.
##  For the current game, sets score and rooms
##  visited to 0.
##  Allows modification of instance variables
##  with its built in functions.

class Game(object):
    rooms = ["Enter", "Pentagram", "Triangle", "Square", "Circle", "Star", "Dungeon", "Cell", "Royal"]
    def __init__ (self, score, visited):
        self.score = score
        self.visited = visited

    def visitedPlus(room):
        if room == "Enter":
            self.visited[0] += 1
        elif room == "Pentagram":
            self.visited[1] += 1
        elif room == "Triangle":
            self.visited[2] += 1
        elif room == "Square":
            self.visited[3] += 1
        elif room == "Circle":
            self.visited[4] += 1
        elif room == "Star":
            self.visited[5] += 1
        elif room == "Dungeon":
            self.visited[6] += 1
        elif room == "Cell":
            self.visited[7] += 1
        elif room == "Royal":
            self.visited[8] += 1
        else:
            print "We have a programming errror, because we should never end up here."
    def scoreAdded(newScore):
        self.score = self.score + newScore


class QAndA(object):
    def __init__(self, roomName, qType, Q, answerList,numCorrectNeeded, pts, weight):
        self.roomName = roomName        #String
        self.qType = qType              #string
        self.Q = Q                      #string
        self.answerList = answerList    #list of strings
        self.numCorrectNeeded = numCorrectNeeded        # int
        self.pts = pts                  #int
        self.weight = weight            #int

class RoomQuestionList(object):
    # Defines a list of questions for a specific room.
    # We must call a loop on the addAQuestion method to add
    # all of the questions for this room.
    def __init__(self, roomName):
        self.roomName = roomName
        self.questions = []

    def buildAQuestionList(self):
        rawFileData = open("hardwayEx36questions.txt")
        for eachLine in rawFileData:
            parsedLine = eachLine.strip().split("%")
            if parsedLine[0] == self.roomName:
                print parsedLine
                thisQuestionObject = [self.roomName, parsedLine[1], parsedLine[2], parsedLine[3].split(" "), int(parsedLine[4]), int(parsedLine[5]), int(parsedLine[6])]
                self.questions.append(thisQuestionObject)
        rawFileData.close()


class Room(object):
	#Define what a room is, initializes variables for the instance of the object.
	#	Parameters needed (RoomName, Intro,  Doorlist)
	#	Defined functions of this class:
	#		PrintIntro(RoomName)
	#		printQuestions(RoomName, DoorList,)
 	#		PrintConclusion()
	#		PrintHelp(Topic)
	#		Improper(ImproperType)
    def __init__(self, roomName):
		self.roomName = roomName  #string

    def getAtts(self):
        rawFileData = open("hardwayEx36rooms.txt")
        for eachLine in rawFileData:
            parsedLine = eachLine.strip().split("%")
            if parsedLine[0] == self.roomName:
                self.intro = parsedLine[1]
                self.doorList = parsedLine[2].strip().split(" ")
        rawFileData.close()

######################
###   End Classes  ###
######################

#################
### Functions ###
#################

## chooseADoor ##
## funnction   ##
## params:  curRoom
##          correctQs
## returns nextRoom

def chooseADoor(curRoom, correctQs):
    print "You got %d questions right, so %d doors open." % (correctQs, correctQs)
    print "You can choose from:"
    for x in range(0, correctQs):
        print curRoom.doorList[x]
    strvar = raw_input("Which door would you like?")
    return strvar

## parseAndPrintASearchDiagram ##
## Function                    ##
## Params: qdata string
##          grid int
## return null
## Prints the wordsearch grid

def parseAndPrintASearchDiagram(qdata, grid):
    for y in range (0, grid):
        for x in range (0+y*grid, grid+y*grid):
            print qdata[x],
        print " "


## askNScore ##
## function  ##
## params:  a question object
## returns: score

def askNScore(Q):
    score = 0
    if Q[1] == "RIDDLE" or Q[1] == "TRICKRIDDLE" or Q[1] == "TRIVIA" or Q[1] == "MATH" or Q[1] == "GENERAL":
        print "Here is your %s question: " % Q[1]
        print Q[2]
    elif Q[1] == "SEARCH3":
        print "Find all the 3-letter words, list each with a space between in one answer:"
        print ""
        parseAndPrintASearchDiagram(Q[2], 3)
    elif Q[1] == "SEARCH4":
        print "Find all the 3 and 4-letter words, list each with a space between in one answer:"
        print ""
        parseAndPrintASearchDiagram(Q[2], 4)
    elif Q[1] == "SEARCH5":
        print "Find all the 3, 4 and 5-letter words, list each with a space between in one answer:"
        print ""
        parseAndPrintASearchDiagram(Q[2], 5)
    else:
        print "This is a test of your ability to get something exactly right."
        print "There is no time limit, so be careful and take your time!"
        print "Copy the line EXACTLY for your answer."
        print Q[2]
    strvar = raw_input("Your answer:")
    answers = strvar.strip().split(" ")
    number_of_correct_answers = 0
    for each in answers:
        if each in Q[3]:
            number_of_correct_answers += 1
    if number_of_correct_answers >= Q[4]:
        print "Correct!"
        score = Q[5] * Q[6]
    else:
        print "Nope, Incorrect, or not enough correct Answers!"
    return score

## enter_a_room ##
## Parameters needed: roomName string

def enter_a_room(room):
    curRoom = Room(room)
    curRoom.getAtts()                           #reads variables from file.
    roomscore = 0                                   #reset roomscore
    print curRoom.intro
    print "The doors here are marked with these words:"
    print curRoom.doorList                      #print the doorList
    questions = RoomQuestionList(room)  #start RoomQuestionList object,this room.
    questions.buildAQuestionList()                  #get the question list
    numberOfQs = len(questions.questions)           #number of questions
    numCorrect = 0
    for door in curRoom.doorList:                    #one question per door
        currentQNum = random.randint(0, numberOfQs-1)    #choose a question
        currentQ = questions.questions[currentQNum]     #this holds the list of
                                                        #question data line.
        thisQScore = askNScore(currentQ)
        roomscore += thisQScore                         # assign the result of
                                                        #the questioning to the
                                                        #roomscore
        if thisQScore > 0:
            numCorrect +=1
    print "Your total Room Score is: %r" % roomscore
    nextRoom = chooseADoor(curRoom, numCorrect)
    global thisGame
    thisGame.score += roomscore
    print "Current Game Score: %r" % thisGame.score

    return nextRoom

def _main():
    """ This is the main program. It initializes
    uses only functions and classes previously
    defined."""
    play_a_game = True
    global thisGame
    while play_a_game:
        score = 0                               #initial score
        visited = [0,0,0,0,0,0,0,0,0]           #times each room visited
        thisGame = Game(score, visited)         #initialize thisGame
        print "Game initialized and started."

        thisRoom = ""
        nextRoom = thisGame.rooms[0]
        while nextRoom != "Royal" and nextRoom != "Dungeon" and nextRoom != "Cell":
            nextRoom = enter_a_room(nextRoom)

        # need code here to handle end of game for 3 EOG rooms.
        if nextRoom == "Royal":
            print "Congrats. You Win."
        elif nextRoom == "Dungeon":
            print "You are dead from torment."
        elif nextRoom == "Cell":
            print "You are dead from going crazy."
        else:
            print "Program error, we should never be here."
        again = raw_input("Would you like to play again? Y or N >>")
        if again == "N":
            play_a_game = False
        elif again != "Y":
            print "LOL because you can't follow simple instructions, now you must play again!"
        else:
            pass
    print "Thanks for playing!"

_main()
