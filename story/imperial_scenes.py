import events
import scene
import scenetemplate
from scenetemplate import sceneTemplate


def addSceneTemplates(gameState):
    sceneTemplate.register(gameState)


@sceneTemplate
class ImperialCourt(scenetemplate.SceneTemplate):
    def __init__(self, gameState):
        super().__init__(gameState)
        self.name = 'Imperial Court'
    
    def isValid(self):
        return self.gameState.state['location'] == 'Imperial Court'
    
    def score(self):
        return 0

    def leave(self):
        self.gameState.setState('location', 'Arinna Central Railvan Station')

    class Scene(scene.Scene):
        def __init__(self, template):
            super().__init__(template)
            self.addEvent(events.Narration("The Emperor regards you down his long nose as you kneel before him. As the pause extends, you begin to feel uncomfortable."))
            self.addEvent(events.Say(self.gameState.emperor, "What was your name again?"))
            self.addEvent(events.GetUserText("Type your name and press Enter", lambda text : setattr(self.gameState.player, 'name', text)))
            self.addEvent(events.Say(self.gameState.player, "", lambda : "I am " + self.gameState.player.name + ", Emperor."))
            self.addEvent(events.Say(self.gameState.emperor, "Ah yes, I'm told you saved my life by killing an assassin at the parade last week."))
            self.addEvent(events.Say(self.gameState.emperor, "And if I'm not mistaken, the same Imperial agent who ended the siege of Ilsar, and more recently found the Tantoma Scrolls. The Arcanum tells me they are learning much from them."))
            choiceContinue = events.GetUserChoice.Choice('Modest', self.choiceContinue)
            choiceProud = events.GetUserChoice.Choice('Proud', self.choiceProud)
            self.addEvent(events.GetUserChoice("Are you ...", [choiceContinue, choiceProud]))
        
        def choiceProud(self):
            self.addEvent(events.Say(self.gameState.player, "Those are the least of my accomplishments my Emperor!"))
            self.addEvent(events.Narration("The Emperor regards you sharply."))
            self.addEvent(events.Say(self.gameState.emperor, "Quiet, citizen. I shall be the judge of your worth."))
            self.choiceContinue()
        
        def choiceContinue(self):
            self.addEvent(events.Say(self.gameState.emperor, "The Empire is repaying your loyalty and resourcefulness by elevating you to nobility. Perhaps others will be inspired by your success."))
            self.addEvent(events.Say(self.gameState.emperor, "", lambda : "Arise Dominus " + self.gameState.player.name + "."))
            self.addEvent(events.Say(self.gameState.emperor, "Now there is the matter of a domain to live on. The Caldar region requires a new Dominus urgently, as it has been several months since Dominus Tenjin disappeared."))
            self.addEvent(events.Say(self.gameState.emperor, "It is on the Eastern border of the Empire, not entirely civilised, but I believe it will suit your adventurous spirit! I shall send an advisor with you to help you learn the ways of a Dominus."))
            self.addEvent(events.Say(self.gameState.emperor, "You will leave on tomorrow's Eastern railvan."))
            self.addEvent(events.Narration("Nobility! All of your descendants will bear this status. If you have any, that is. The thought of governing a domain makes you a little nervous, but how hard can the life of a noble be? You've definitely survived worse."))

            

@sceneTemplate
class RailvanStation(scenetemplate.SceneTemplate):
    def __init__(self, gameState):
        super().__init__(gameState)
        self.name = 'Arinna Central Railvan Station'
     
    def isValid(self):
        return self.gameState.getState('location') == self.name
     
    def score(self):
        return 0
     
    def leave(self):
        self.gameState.setState('location', 'Railvan to Hyree')

    class Scene(scene.Scene):
        def __init__(self, template):
            super().__init__(template)
            self.addEvent(events.Narration("And so early in the morning, you push your way through the bustle of the capital to the central rail station, looking for your advisor. He is not hard to spot, surrounded by twenty Imperial guards."))
            self.addEvent(events.Say(self.gameState.advisor, "", lambda : "Good morning " + self.gameState.player.name + "! I can see you haven't brought much apart from your weapons, but never fear, I have many books on a variety of subjects. We can also buy some clothes on the way."))
            self.addEvent(events.Narration(self.gameState.advisor.firstName + " steps up into the first class railvan carriage being pushed in front of the engine, and you follow him. The troops pack into a van pulled behind, and the caravan jolts forward slowly gaining speed."))

     
