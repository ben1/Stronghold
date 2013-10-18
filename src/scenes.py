'''
Created on 05/10/2013

@author: Ben
'''
from PySide import QtCore
import events


class Scene(QtCore.QObject):
    sigEvent = QtCore.Signal(events.Event)
    
    def __init__(self, gameState):
        super().__init__()
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
        if(len(self.events) > 0):
            self.currentEvent = self.events[0]
            self.currentEvent.trigger()
            self.sigEvent.emit(self.currentEvent)

    def leave(self):
        pass
        
    def next(self):
        if self.currentEvent:
            if not self.currentEvent.next():
                return False
            else:
                self.events = self.events[1:]
                if(len(self.events) > 0):
                    self.currentEvent = self.events[0]
                    self.currentEvent.trigger()
                    self.sigEvent.emit(self.currentEvent)
                    return False
        return True # the scene is finished

              
class GameOver(Scene):
    def __init__(self, gameState):
        super().__init__(gameState)
        self.name = 'Game Over'
        self.addEvent(events.Narration('Sorry but you must try again.'))
        self.addEvent(events.GameOver())



