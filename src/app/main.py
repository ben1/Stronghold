'''
Created on 13/04/2013

@author: Ben
'''

import pyglet
import pyglet.app


class StrongholdWindow(pyglet.window.Window):
    def __init__(self):
        super(StrongholdWindow, self).__init__(1024, 768)

        self.label = pyglet.text.Label('Hello, world!')

    def on_draw(self):
        self.clear()
        self.label.draw()

if __name__ == '__main__':
    window = StrongholdWindow()
    pyglet.app.run()
    
