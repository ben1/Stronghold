'''
Created on 09/10/2013

@author: Ben
'''

class Fragment():
    def __init__(self):
        self.preconditions = []
    
    def test(self, gameState):
        for fn in self.preconditions:
            if(not fn(self, gameState)):
                return False
        return True
            

def makeFragment():
    f = Fragment()
    f.preconditions.append(lambda s, g: g.currentLocation == "Caldar")
    
''' 
Algorithm
For all templates, find all potential instances that match existing variables, then score all potential instances

Scoring
The best score is 0. Potential instances lose points for all rules that don't macth perfectly, and lose points for not being relevant / timely / helping the arc, etc.
'''
