'''
Created on 06/10/2013

@author: Ben
'''
import pygame
from pgu import gui
import events


class SceneView(gui.ScrollArea):
    def __init__(self, scene):
        self.scene = scene
        doc = gui.Document(width=700, height = 400)
        super().__init__(doc, hscrollbar = False)
        self.space = doc.style.font.size(" ")
        self.widget.block(align=-1)
        self.textInput = None

    def addText(self, text):
        for word in text.split(' '):
            self.widget.add(gui.Label(word))
            self.widget.space(self.space)

    def onEnterScene(self, scene):
        self.addText(scene.name)
        self.widget.br(self.space[1])

    def onNarration(self, narration):
        self.widget.br(self.space[1])
        self.addText(narration.text)
        self.widget.br(self.space[1])
        self.connect(gui.MOUSEBUTTONDOWN, self.onClickToProgress)
        
    def onSay(self, say):
        self.widget.br(self.space[1])
        if(say.sourceActor.isPlayer):
            self.addText('You say "' + say.text + '"')
        else:
            self.addText(say.sourceActor.name + ' says "' + say.text + '"')
        self.widget.br(self.space[1])
        self.connect(gui.MOUSEBUTTONDOWN, self.onClickToProgress)

    def onClickToProgress(self):
        if(self.scene.currentEvent):
            self.disconnect(gui.MOUSEBUTTONDOWN, self.onClickToProgress)
            self.scene.currentEvent.done = True
            
    def onGetUserText(self, getUserText):
        self.widget.br(self.space[1])
        self.addText(getUserText.caption)
        self.widget.br(self.space[1])
        i = gui.Input(size = 20)
        self.textInput = i
        self.widget.add(i)
        i.focus()
        i.connect(gui.ACTIVATE, self.onGetUserTextComplete, i)
        self.widget.br(self.space[1])

    def onGetUserTextComplete(self, i):
        if (len(i.value) > 0) and self.scene.currentEvent:
            self.scene.currentEvent.setText(i.value)
            i.blur() # remove focus so that it doesn't hang around even though we remove from the container
            self.textInput = None
            self.widget.remove(i)
            self.widget.removeLine()
            self.widget.removeLine()
            self.widget.removeLine()
        
    def event(self,e):
        super().event(e)
#         if(self.scene.currentEvent):
#             eventType = type(self.scene.currentEvent)
#             if e.type == pygame.MOUSEBUTTONDOWN:
#                 if(eventType is events.Say or eventType is events.Narration):
#                     self.scene.currentEvent.done = True
                
            
