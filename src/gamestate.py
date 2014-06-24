
from PySide import QtCore
import actors
import scene

''' 
'''
class GameState(QtCore.QObject):
    sigEnterScene = QtCore.Signal(scene.Scene)
    sigLeaveScene = QtCore.Signal(scene.Scene)
    
    def __init__(self):
        super().__init__()
        self.sceneTemplates = []
        self.pendingScenes = []

        self.player = actors.Player()
        self.emperor = actors.Emperor()
        self.advisor = actors.Advisor()
                
    def init(self):
        self.prepareNextScene()
        

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
                validSceneTemplates.sort(key = lambda t : t[0])
                self.enterScene(validSceneTemplates[0][1].Scene(self, validSceneTemplates[0][1]))
                return
            self.enterScene(scene.GameOver(self))


