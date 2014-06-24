'''
Created on 05/10/2013

@author: Ben
'''

class Actor():
    nextId = 1
    def __init__(self):
        self.id = Actor.nextId
        Actor.nextId += 1
        self.name = 'Someone'
        self.isPlayer = False


class Player(Actor):
    def __init__(self):
        self.name = 'Some player'
        self.isPlayer = True
        
class Emperor(Actor):
    def __init__(self):
        super().__init__()
        self.name = 'Emperor Kanate'
        self.firstName = 'Emperor'
        
class Advisor(Actor):
    def __init__(self):
        super().__init__()
        self.name = 'Johan Kratz'
        self.firstName = 'Johan'
        

