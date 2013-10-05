'''
Created on 05/10/2013

@author: Ben
'''

#from gamestate import GameState


class Engine():
    def __init__(self, gameState):
        self.gameState = gameState
        
    def render(self):
        if(self.gameState.scene):
            # render the scene first because it is an immediate occurrence
            if not (self.gameState.scene.render()):
                # go to the next scene
                self.gameState.prepareNextScene()