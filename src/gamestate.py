
from player import Player
import actors
import scenes
import events


class GameState():
    def __init__(self,**params):
        self.player = Player()
        self.emperor = actors.Emperor()
        ns = scenes.Scene()
        ns.name = 'Imperial Court'
        ns.addActor(self.player)
        ns.addActor(self.emperor)
        ns.addEvent(events.Narration("The Emperor regards you down his long nose as you kneel before him. As the pause extends, you begin to feel uncomfortable."))
        ns.addEvent(events.Say(self.emperor, "What was your name again?"))
        # get input and set playername. why make an event class to do this? can we run python like 'self.player.name = GetUserText("Type your name and press Enter")'
        self.scene = ns


    def prepareNextScene(self):
        self.scene = scenes.GameOver()

