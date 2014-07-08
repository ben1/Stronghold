'''
Created on 05/10/2013

@author: Ben
'''

class Event():
    def __init__(self):
        self.name = 'Something happened'

    def trigger(self, scene):
        self.scene = scene

    def next(self):
        self.scene.doNextEvent()

        
class Say(Event):
    def __init__(self, sourceActor, text, func = None):
        super().__init__()
        self.sourceActor = sourceActor
        self.text = text
        self.func = func
        
    def trigger(self, *args, **kw):
        super().trigger(*args, **kw)
        if(self.func):
            self.text = self.func()

    
class Narration(Event):
    def __init__(self, t):
        super().__init__()
        self.text = t
        

class Func(Event):
    def __init__(self, func):
        super().__init__()
        self.func = func
    
    def trigger(self, scene):
        super().trigger(scene)
        self.func()
        self.next()
        
        
class GameOver(Event):
    def __init__(self):
        super().__init__()

    def next(self):
        pass #never end


class GetUserText(Event):
    def __init__(self, caption, func):
        super().__init__()
        self.caption = caption
        self.func = func
    
    def next(self):
        pass # don't end except when the user enters text
    
    def setText(self, text):
        self.text = text
        if(self.func):
            self.func(text)
        super().next()


class GetUserChoice(Event):
    class Choice:
        def __init__(self, text, func = None):
            self.text = text
            self.func = func

    def __init__(self, caption, choices):
        super().__init__()
        self.caption = caption
        self.choices = []
        for c in choices:
            self.choices.append(GetUserChoice.Choice(c[0], c[1]))
        
    def next(self):
        pass # don't end except when the user enters a choice
    
    def setChoice(self, choice):
        if(choice.func):
            choice.func()
        super().next()

