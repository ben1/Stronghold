'''
Created on 06/10/2013

@author: Ben
'''
from PySide import QtGui, QtCore
from gamestate import GameState


class Paragraph(QtGui.QLabel):

    def __init__(self, text):
        super().__init__()
        self.setText(text)  
        self.setWordWrap(True)
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred);


class SceneView(QtGui.QScrollArea):

    def __init__(self, scene):
        super().__init__()
        self.scene = scene
        scene.sigEvent.connect(self.onSceneEvent)

        # why doesn't this work?
        #s = QtGui.QWidget()
        #self.setWidget(s)
        #s.setLayout(hbox)
        hbox = QtGui.QHBoxLayout()
        self.setLayout(hbox)
        hbox.addStretch(1)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addStretch()
        hbox.addLayout(self.vbox, 3)
        hbox.addStretch(1)

        t = Paragraph(scene.name)
        self.vbox.insertWidget(self.vbox.count() - 1, t)
        
    def onSceneEvent(self, event):
        self.currentEvent = event
        if event.__class__.__name__ == 'Say':
            text = event.text
            if(event.sourceActor.isPlayer):
                text = 'You say "' + text + '"'
            else:
                text = event.sourceActor.name + ' says "' + text + '"'
            self.vbox.insertWidget(self.vbox.count() - 1, Paragraph(text))
        elif event.__class__.__name__ == 'Narration':
            p = Paragraph(event.text)
            self.vbox.insertWidget(self.vbox.count() - 1, p)
            print(p.sizeHint())
        elif event.__class__.__name__ == 'GetUserText':
            self.vbox.insertWidget(self.vbox.count() - 1, Paragraph(event.caption))
            e = QtGui.QLineEdit()
            self.getUserText = e
            e.returnPressed.connect(self.onGetUserText)
            self.vbox.insertWidget(self.vbox.count() - 1, e)

    def onGetUserText(self):
        #remove caption and QLineEdit
        oldText = self.vbox.takeAt(self.vbox.count() - 2)
        oldText.widget().deleteLater()
        oldText = self.vbox.takeAt(self.vbox.count() - 2)
        oldText.widget().deleteLater()
        self.currentEvent.setText(self.getUserText.text())


class GameView(QtGui.QWidget):
    
    def __init__(self, gameState):
        super().__init__()
        self.gameState = gameState        
        self.gameState.sigEnterScene.connect(self.onEnterScene)
        self.hbox = QtGui.QVBoxLayout()
        self.setLayout(self.hbox)

    def mousePressEvent(self, e):
        self.gameState.next()

    def onEnterScene(self, scene):
        # Qt requires removing the layout item then explicitly deleting the widget on the layout item
        # Also note that we need the SceneView widget to act as a parent of all the widgets in the layout, otherwise we'd have to iterate them all and delete them explicitly
        if self.hbox.count() > 0:
            oldScene = self.hbox.takeAt(0)
            oldScene.widget().deleteLater()
        self.hbox.addWidget(SceneView(scene))

        
