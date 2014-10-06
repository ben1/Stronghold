'''
A scene is an organizational unit for action in the game. It ties together a 
few Actors and a series of events. The exact actors that may be involved in a
scene depends on how the scene was initialized, and how the events play out
depends on the starting conditions as well as how the actors act.
'''
from PySide import QtCore
import events


class Scene(QtCore.QObject):
    sigEvent = QtCore.Signal(events.Event)
    
    def __init__(self, template):
        super().__init__()
        self.gameState = template.gameState
        self.template = template
        self.name = template.name
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
        self.template.leave()
        
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



