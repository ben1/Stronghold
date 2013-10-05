'''
Created on 05/10/2013

@author: Ben
'''

class Event():
    def __init__(self):
        self.name = 'Something happened'
        
class Say(Event):
    def __init__(self, sa, t):
        self.sourceActor = sa
        self.text = t
        
    def render(self):
        # output self.text as said by the source actor
        return True
    
class Narration(Event):
    def __init__(self, t):
        self.text = t
        
    def render(self):
        # output self.text as said by the narrator
        return True