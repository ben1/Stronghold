'''
Created on 06/10/2013

@author: Ben
'''


        
class LogGameView(object):
    
    def __init__(self, gameState):
        super().__init__()
        self.gameState = gameState        
        self.gameState.sigEnterScene.connect(self.onEnterScene)
        self.logfile = open('game_log.txt', 'w', 1)
        
    def onEnterScene(self, scene):
        self.scene = scene
        scene.sigEvent.connect(self.onSceneEvent)
        self.logfile.write('\n\n' + scene.name + '\n\n')
    
    def onSceneEvent(self, event):
        self.currentEvent = event
        if event.__class__.__name__ == 'Say':
            text = event.text
            if(event.sourceActor.isPlayer):
                text = 'You say "' + text + '"'
            else:
                text = event.sourceActor.name + ' says "' + text + '"'
            self.logfile.write(text + '\n')
        elif event.__class__.__name__ == 'Narration':
            self.logfile.write(event.text + '\n')
        elif event.__class__.__name__ == 'GetUserText':
            self.logfile.write(event.caption + '\n')
        elif event.__class__.__name__ == 'GetUserChoice':
            self.logfile.write(event.caption + '\n')
            for choice in event.choices:
                self.logfile.write('  ' + choice.text + '\n')

