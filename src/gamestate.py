'''
The root object containing information about the state of the game world.
It acts as a dictionary of miscellaneous information as well as a state-
machine for the current scene.
'''

from PySide import QtCore
import actors
import events
import scene
import scenetemplate


class GameState(QtCore.QObject):
    sigEnterScene = QtCore.Signal(scene.Scene)
    sigLeaveScene = QtCore.Signal(scene.Scene)
    
    def __init__(self):
        super().__init__()
        self.sceneTemplates = []
        self.pendingScenes = []
        self.state = {}
        self.actors = {}

        self.player = actors.Player()
        self.emperor = actors.Emperor()
        self.advisor = actors.Advisor()
                
    def init(self):
        self.prepareNextScene()

    def getState(self, key):
        return self.state.get(key, None)

    def setState(self, key, value = True):
        self.state[key] = value

    def cleanup(self):
        self.leaveScene()
        
    def addSceneTemplate(self, sceneTemplate):
        self.sceneTemplates.append(sceneTemplate)
        
    def enterScene(self, sc):
        self.scene = sc
        self.sigEnterScene.emit(sc)
        sc.enter(self) #has to be after sigEnterScene otherwise events aren't hooked up before scene.enter() triggers them.

    def leaveScene(self):
        if self.scene:
            self.sigLeaveScene.emit(self.scene)
            #self.widget.remove(self.scene.view)
            self.scene.leave()
            self.scene = None
    
    def next(self):
        if(self.scene):
            self.scene.next()
        else:
            self.prepareNextScene()
    
    def doNextScene(self):
        self.leaveScene()
        self.prepareNextScene()
        
    def prepareNextScene(self):
        if len(self.pendingScenes) > 0:
            self.enterScene(self.pendingScenes.pop(0))
        else:
            validSceneTemplates = []
            for st in self.sceneTemplates:
                if st.isValid():
                    validSceneTemplates.append((st.score(), st))
            if len(validSceneTemplates) > 0:
                validSceneTemplates.sort(key = lambda t : -t[0]) # put highest values first
                self.enterScene(validSceneTemplates[0][1].createScene())
                return
            self.enterScene(SceneTemplateGameOver(self).createScene())


class SceneTemplateGameOver(scenetemplate.SceneTemplate):
    def __init__(self, gameState):
        super().__init__(gameState)
        self.name = 'Game Over'
        
    class Scene(scene.Scene):
        def __init__(self, template):
            super().__init__(template)        
            self.addEvent(events.Narration('Sorry but you must try again.'))
            self.addEvent(events.GameOver())

