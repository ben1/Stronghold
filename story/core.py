import events
import scene
import scenetemplate
from scenetemplate import sceneTemplate


def addSceneTemplates(gameState):
    sceneTemplate.register(gameState)


@sceneTemplate
class Welcoming(scenetemplate.SceneTemplate):
    def __init__(self, gameState):
        super().__init__(gameState)
        self.name = 'Welcoming'

    def isValid(self):
        return self.gameState.getState('location') == 'Stronghold' and self.gameState.getState('welcomed') != True

    def score(self):
        return 1000

    class Scene(scene.Scene):
        def __init__(self, gameState, sceneT):
            super().__init__(gameState)
            self.name = sceneT.name
            self.addEvent(events.Narration("It is a grey and windy afternoon when your party sights the stronghold silhouetted on a ridge. This outpost, seated before the great snowy mountains of the North, and overlooking the rolling hills and forests of the wild-lands is to be your home. Remembering the attack on your party, you suddenly realise how vulnerable you are outside its walls.")) 
            self.addEvent(events.Narration("The path up from the valley floor winds back and forth, and the horses plod the last stretch up to the gates. The guard slouched by the open gate walks up to greet you."))
            self.addEvent(events.Narration('"Welcome to Hyree commander, we could do with some help."'))
            self.addEvent(events.GetUserChoice("Do you respond with...", [('Charisma', self.cCharisma), ('Seriousness', self.cSerious), ('Self-deprecation', self.cDeprecation)]))
        def onExit(self):
            self.gameState.setState('welcomed', True)

        def cCharisma(self):
            self.addEvent(events.Narration('You respond with a winning smile and say "I am sure we will be able to sort it all out!". The guard gives you an uneasy smile.'))
            self.cContinue()
        def cSerious(self):
            self.addEvent(events.Narration('You respond with a stern look and say "Things will certainly change now that I am here. Next time you are at the gates you will wear your helmet at all times. Understood?" The guard frowns alightly but just nods mutely.'))        
            self.cContinue()
        def cDeprecation(self):
            self.addEvent(events.Narration('You respond with a weak smile and say "Well, I might be able to help... we shall see." The guard loses his smile, but laughs politely.'))
            self.cContinue()
        def cContinue(self):
            self.addEvent(events.Narration("Your party is led through the gates and you dismount in the courtyard. Several other guards are on the walls, but there are far fewer people about than you expected. Another man greets you and leads you into the keep to meet the captain of the guard."))

@sceneTemplate
class CouncilMeeting(scenetemplate.SceneTemplate):
    def __init__(self, gameState):
        super().__init__(gameState)
        self.name = 'Council Meeting'
    
    def isValid(self):
        return self.gameState.getState('location') == 'Stronghold'
    
    def score(self):
        return 0

    class Scene(scene.Scene):
        def __init__(self, gameState, sceneT):
            super().__init__(gameState)
            self.name = sceneT.name
            self.addEvent(events.Narration("The Emperor regards you down his long nose as you kneel before him. As the pause extends, you begin to feel uncomfortable."))
            self.addEvent(events.Say(self.gameState.emperor, "What was your name again?"))
            self.addEvent(events.GetUserText("Type your name and press Enter", lambda text : setattr(self.gameState.player, 'name', text)))
            self.addEvent(events.Say(self.gameState.player, "", lambda : "I am " + self.gameState.player.name + ", Emperor."))
            self.addEvent(events.Say(self.gameState.emperor, "Ah yes, I'm told you saved my life by killing an assassin at the parade last week."))
            self.addEvent(events.Say(self.gameState.emperor, "And if I'm not mistaken, the same Imperial agent who ended the siege of Ilsar, and more recently found the Tantoma Scrolls. The Arcanum tells me they are learning much from them."))
            self.addEvent(events.GetUserChoice("Are you ...", [('Modest', self.choiceContinue), ('Proud', self.choiceProud)]))
        
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

        def onExit(self):
            self.gameState.setState('location', 'Arinna Central Railvan Station')
            

