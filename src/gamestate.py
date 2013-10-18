
from PySide import QtCore
import actors
import scenes
import events
import views

''' 
'''
class GameState(QtCore.QObject):
    sigEnterScene = QtCore.Signal(scenes.Scene)
    sigLeaveScene = QtCore.Signal(scenes.Scene)
    
    def __init__(self):
        super().__init__()
        
    def init(self):
        self.pendingScenes = []
        self.player = actors.Player()
        self.emperor = actors.Emperor()
        self.advisor = actors.Advisor()
        
        ns = scenes.Scene(self)
        ns.name = 'Imperial Court'
        ns.addActor(self.player)
        ns.addActor(self.emperor)
        ns.addEvent(events.Narration("The Emperor regards you down his long nose as you kneel before him. As the pause extends, you begin to feel uncomfortable."))
        ns.addEvent(events.Say(self.emperor, "What was your name again?"))
        ns.addEvent(events.GetUserText("Type your name and press Enter", lambda text : setattr(self.player, 'name', text)))
        ns.addEvent(events.Say(self.player, "", lambda : "I am " + self.player.name + ", Emperor."))
        ns.addEvent(events.Say(self.emperor, "Ah yes, I'm told you saved my life by killing an assassin at the parade last week."))
        ns.addEvent(events.Say(self.emperor, "And if I'm not mistaken, the same Imperial agent who ended the siege of Ilsar, and more recently found the Tantoma Scrolls. The Arcanum tells me they are learning much from them."))
        ns.addEvent(events.Say(self.emperor, "The Empire is repaying your loyalty and resourcefulness by elevating you to nobility. Perhaps others will be inspired by your success."))
        ns.addEvent(events.Say(self.emperor, "", lambda : "Arise Dominus " + self.player.name + "."))
        ns.addEvent(events.Say(self.emperor, "Now there is the matter of a domain to live on. The Caldar region requires a new Dominus urgently, as it has been several months since Dominus Tenjin disappeared."))
        ns.addEvent(events.Say(self.emperor, "It is on the Eastern border of the Empire, not entirely civilised, but I believe it will suit your adventurous spirit! I shall send an advisor with you to help you learn the ways of a Dominus."))
        ns.addEvent(events.Say(self.emperor, "You will leave on tomorrow's Eastern railvan."))
        ns.addEvent(events.Narration("Nobility! All of your descendants will bear this status. If you have any, that is. The thought of governing a domain makes you a little nervous, but how hard can the life of a noble be? You've definitely survived worse."))
        self.enterScene(ns)

        s2 = scenes.Scene(self)
        s2.name = "Arinna Central Railvan Station"
        s2.addActor(self.player)
        s2.addActor(self.advisor)
        s2.addEvent(events.Narration("And so early in the morning, you push your way through the bustle of the capital to the central rail station, looking for your advisor. He is not hard to spot, surrounded by twenty Imperial guards."))
        s2.addEvent(events.Say(self.advisor, "", lambda : "Good morning " + self.player.name + "! I can see you haven't brought much apart from your weapons, but never fear, I have many books on a variety of subjects. We can also buy some clothes on the way."))
        s2.addEvent(events.Narration("Johan steps up into the first class railvan carriage being pushed in front of the engine, and you follow him. The troops pack into a van pulled behind, and the caravan jolts forward slowly gaining speed."))

        self.pendingScenes.append(s2)

    def cleanup(self):
        self.leaveScene()
        
    def enterScene(self, scene):
        self.scene = scene
        #scene.view = views.SceneView(scene)
        #self.widget.add(scene.view, 0, 50)
        self.sigEnterScene.emit(scene)
        scene.enter()

    def leaveScene(self):
        if self.scene:
            self.sigLeaveScene.emit(self.scene)
            #self.widget.remove(self.scene.view)
            self.scene.leave()
            self.scene = None
    
    def next(self):
        if(self.scene):
            if self.scene.next():
                self.leaveScene()
                self.prepareNextScene()
        else:
            self.prepareNextScene()
    
    def prepareNextScene(self):
        if len(self.pendingScenes) > 0:
            self.enterScene(self.pendingScenes.pop(0))
        else:
            self.enterScene(scenes.GameOver(self))


