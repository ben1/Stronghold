'''
Created on 05/10/2013

@author: Ben
'''
import events

class Scene():
    def __init__(self):
        self.name = 'Somewhere'
        self.actors = {}
        self.events = []
        
    def addActor(self, actor):
        self.actors[actor.name] = actor

    def addEvent(self, event):
        self.events.append(event)
        
    def render(self):
        if(len(self.events) > 0):
            e = self.events[0]
            self.events = self.events[1:]
            e.render()
            return True
        else:
            # the scene is finshed
            return False
            
class GameOver(Scene):
    def __init__(self):
        self.addEvent(events.Narration("Game Over"))
        
    def render(self):
        Scene.render(self)
        # don't allow the scene to end
        return True

