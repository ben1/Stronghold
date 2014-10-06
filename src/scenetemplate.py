'''
A SceneTemplate can create a scenes. A particular template may only create 
one scene, or the template may be re-used under different circumstances to 
create several similar scenes during the course of a game.
Annotate your scene template classes with @sceneTemplate in order to add
them to the SceneTemplateRegistry automatically. 
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


