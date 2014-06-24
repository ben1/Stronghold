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
        
    def enter(self, gameState):
        self.doNextEvent()

    def leave(self):
        self.onExit()
        
    def next(self):
        if self.currentEvent:
            self.currentEvent.next()
        else:
            self.gameState.doNextScene()

    def doNextEvent(self):
        if self.currentEvent:
            self.events = self.events[1:]
        if(len(self.events) > 0):
            self.currentEvent = self.events[0]
            self.currentEvent.trigger(self)
            self.sigEvent.emit(self.currentEvent)
        else:
            self.gameState.doNextScene()

        
class GameOver(Scene):
    def __init__(self, gameState):
        super().__init__(gameState)
        self.name = 'Game Over'
        self.addEvent(events.Narration('Sorry but you must try again.'))
        self.addEvent(events.GameOver())



