'''
Created on 05/10/2013

@author: Ben
'''

class Event():
    def __init__(self):
        self.name = 'Something happened'

    def trigger(self):
        pass

        
class Say(Event):
    def __init__(self, sourceActor, text, func = None):
        super().__init__()
        self.sourceActor = sourceActor
        self.text = text
        self.func = func
        
    def trigger(self):
        if(self.func):
            self.text = self.func()
        
    def next(self):
        return True

    
class Narration(Event):
    def __init__(self, t):
        super().__init__()
        self.text = t
                
    def next(self):
        return True


class GameOver(Event):
    def __init__(self):
        super().__init__()

    def next(self):
        return False # never end


class GetUserText(Event):
    def __init__(self, caption, func):
        super().__init__()
        self.done = False 
        self.caption = caption
        self.func = func

    def render(self, view):
        view.onGetUserText(self)
    
    def next(self):
        return self.done
    
    def setText(self, text):
        self.text = text
        if(self.func):
            self.func(text)
        self.done = True


# class ChangeScene(Event):
#     def __init__(self, scene):
#         super().__init__()
#         self.scene = scene
#     
#     def render(self, view):
#         pass
#     
#     def update(self):
#         return not self.done
#     
