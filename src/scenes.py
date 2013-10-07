'''
Created on 05/10/2013

@author: Ben
'''
import events

class Scene():
    def __init__(self, gameState):
        self.gameState = gameState
        self.name = 'Somewhere'
        self.actors = {}
        self.events = []
        self.currentEvent = None
        
    def addActor(self, actor):
        self.actors[actor.name] = actor

    def addEvent(self, event):
        self.events.append(event)
        
    def enter(self):
        self.view.onEnterScene(self)
        if(len(self.events) > 0):
            self.currentEvent = self.events[0]
            self.currentEvent.render(self.view)

    def leave(self):
        pass
        
    def update(self):
        if(self.currentEvent):
            if(self.currentEvent.update()):
                return True
            else:
                self.events = self.events[1:]
                if(len(self.events) > 0):
                    self.currentEvent = self.events[0]
                    self.currentEvent.render(self.view)
                    return True
        # the scene is finished
        return False

              
class GameOver(Scene):
    def __init__(self, gameState):
        super().__init__(gameState)
        self.name = 'Game Over'
        self.addEvent(events.Narration('Sorry but you must try again.'))
        self.addEvent(events.GameOver())



