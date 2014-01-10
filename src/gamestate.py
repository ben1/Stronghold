
from PySide import QtCore
import actors
import scenes
import events

''' 
'''
class GameState(QtCore.QObject):
    sigEnterScene = QtCore.Signal(scenes.Scene)
    sigLeaveScene = QtCore.Signal(scenes.Scene)
    
    def __init__(self):
        super().__init__()
        self.sceneTemplates = []
        self.pendingScenes = []

        self.player = actors.Player()
        self.emperor = actors.Emperor()
        self.advisor = actors.Advisor()
                
    def init(self):
        self.location = 'Imperial Court'
        self.prepareNextScene()
        

    def cleanup(self):
        self.leaveScene()
        
    def addSceneTemplate(self, sceneTemplate):
        self.sceneTemplates.append(sceneTemplate)
        
    def enterScene(self, scene):
        self.scene = scene
        self.sigEnterScene.emit(scene)
        scene.enter(self) #has to be after sigEnterScene otherwise events aren't hooked up before scene.enter() triggers them.

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
                if st.isValid(self):
                    validSceneTemplates.append((st.score(self), st))
            if len(validSceneTemplates) > 0:
                validSceneTemplates.sort(key = lambda t : t[0])
                self.enterScene(validSceneTemplates[0][1])
                return
            self.enterScene(scenes.GameOver())


