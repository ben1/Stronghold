'''
Created on 05/10/2013

@author: Ben
'''
from PySide import QtCore
import events


class SceneTemplate(QtCore.QObject):
    sigEvent = QtCore.Signal(events.Event)
    
    def __init__(self, gameState):
        super().__init__()
        self.gameState = gameState
        self.name = 'A Scene Template'
    
    def createScene(self):
        return self.Scene(self)
    
    def leave(self):
        pass


class SceneTemplateRegistry():
    def __init__(self):
        self.sceneTemplates = []

    def __call__(self, sceneTemplateClass):
        self.sceneTemplates.append(sceneTemplateClass)

    def register(self, gameState):
        for s in self.sceneTemplates:
            gameState.addSceneTemplate(s(gameState))


sceneTemplate = SceneTemplateRegistry()


