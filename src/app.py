import pygame
from pgu import gui
import pyconsole
from gamestate import GameState

class QuitDialog(gui.Dialog):
    def __init__(self,**params):
        title = gui.Label("Quit")
        
        t = gui.Table()
        
        t.tr()
        t.add(gui.Label("Are you sure you want to quit?"),colspan=2)
        
        t.tr()
        e = gui.Button("Okay")
        e.connect(gui.CLICK,self.send,gui.QUIT)
        t.td(e)
        
        e = gui.Button("Cancel")
        e.connect(gui.CLICK,self.close,None)
        t.td(e)
        
        gui.Dialog.__init__(self,title,t)


        
class App(gui.Desktop):
    def __init__(self,**params):
        gui.Desktop.__init__(self,**params)
        
        self.gameState = None
        self.connect(gui.QUIT,self.quit,None)
        
        c = gui.Container(width=800,height=800)
                
        self.new_d = QuitDialog()
        self.new_d.connect(gui.CHANGE,self.action_new,None)
        self.quit_d = QuitDialog()
        self.quit_d.connect(pygame.QUIT,self.quit,None)
                
        #Initializing the Menus, we connect to a number of Dialog.open methods for each of the dialogs.
        menus = gui.Menus([
            ('File/New',self.action_new,None),
            ('File/Exit',self.quit_d.open,None),
            ])
        c.add(menus,0,0)
        menus.rect.w,menus.rect.h = menus.resize()
        
        self.widget = c
        
    def action_new(self,value):
        if(self.gameState):
            self.gameState.cleanup()
        self.gameState = GameState(self.widget)
        
                
    def process_event(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and pygame.key.get_mods() & pygame.KMOD_CTRL:
                self.console.set_active()
                if not self.console.active:
                    self.repaint()
                return True
            elif event.key == pygame.K_q and pygame.key.get_mods() & pygame.KMOD_CTRL: 
                self.console.setvar("python_mode", not self.console.getvar("python_mode"))
                self.console.set_interpreter()                        
                return True

    def run(self):
        self.init()
        self.console = pyconsole.Console(
                                    self.screen, #The surface you want the console to draw on
                                    (self.rect.x,self.rect.y,self.rect.w,200), #A rectangle defining the size and position of the console
                                    globals=globals(),
                                    functions={}, # Functions for the console
                                    key_calls={}, # Defines what function Control+char will call.
                                    syntax={}
                                    )

        while not self._quit:
            # Get input events all in one place and cascade them to each component until processed.
            # (so that it's not a random component that gets an event)
            for event in pygame.event.get():
                if not self.process_event(event):
                    if not self.console.process_input(event):
                        if not (event.type == pygame.QUIT and self.mywindow):
                            self.event(event)
            #update
            if(self.gameState):
                self.gameState.update()
            # draw
            pygame.display.update(self.update())
            self.console.draw()
            
            pygame.time.wait(10)

