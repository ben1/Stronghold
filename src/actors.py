'''
Actor is the base class for central characters in the game. It contains some basic information 
as well as relationships to other characters (from their perspective).
This module also contains a number of core characters.
'''

class Actor():
    nextId = 1
    def __init__(self, name, firstName):
        self.id = Actor.nextId
        Actor.nextId += 1
        self.name = name
        self.firstName = firstName
        self.isPlayer = False
        self.feelingsFor = {}
        self.respectFor = {}
        self.introduced = False
        self.description = 'A non-descript person.'

    def modFeelingsFor(self, actor, value):
        self.feelingsFor[actor] = self.feelingsFor.get(actor, 0) + value
    
    def getFeelingsFor(self, actor):
        return self.feelingsFor.get(actor, 0)

    def modRespectFor(self, actor, value):
        self.respectFor[actor] = self.respectFor.get(actor, 0) + value
    
    def getRespectFor(self, actor):
        return self.respectFor.get(actor, 0)

class Player(Actor):
    def __init__(self):
        super().__init__('Some player', 'Player')
        self.isPlayer = True

class Emperor(Actor):
    def __init__(self):
        super().__init__('Emperor Kanate', 'Emperor')

class Advisor(Actor):
    def __init__(self):
        super().__init__('Johan Kratz', 'Johan')


