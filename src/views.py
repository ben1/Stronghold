'''
Created on 06/10/2013

@author: Ben
'''
from PySide import QtGui, QtCore


class Paragraph(QtGui.QLabel):

    def __init__(self, text):
        super().__init__()
        self.setText(text)  
        self.setWordWrap(True)
        self.setMargin(0)
        self.setStyleSheet("border: 1px solid grey")
        self.setSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)

#    def sizeHint(self):
#        return QtCore.QSize(self.parent().width(), self.heightForWidth(self.parent().width()))

class SceneView(QtGui.QScrollArea):

    def __init__(self, scene):
        super().__init__()
        self.completingTextInput = False
        
        # hook up to the game logic
        self.scene = scene
        scene.sigEvent.connect(self.onSceneEvent)

        # scrollbar always on to avoid jarring layout change, and make sure we're at the end when resizing the scroll area
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.verticalScrollBar().rangeChanged.connect(self.onScrollRangeChanged)
        
        # create a widget to live in the scroll area, so that we can set a layout on it. We want it to use all the space it can.
        hbox = QtGui.QHBoxLayout()
        s = QtGui.QWidget()
        s.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        s.setLayout(hbox)
        self.setWidgetResizable(True)
        self.setWidget(s)

        # the centre of the scene view is a vertical stack of events, aligned to the top
        hbox.addStretch(1)
        self.vbox = QtGui.QVBoxLayout()
        hbox.addLayout(self.vbox, 3)
        hbox.addStretch(1)
        self.vbox.setAlignment(QtCore.Qt.AlignTop)
        t = Paragraph(scene.name)
        self.vbox.insertWidget(self.vbox.count() , t)
        
    def keyPressEvent(self, e):
        # filter out \r from getting back to parent in the case where we know return was just used to complete some text entry
        if e.text() == '\r' and self.completingTextInput:
                self.completingTextInput = False
                return
        super().keyPressEvent(e)
        
    def onSceneEvent(self, event):
        self.currentEvent = event
        if event.__class__.__name__ == 'Say':
            text = event.text
            if(event.sourceActor.isPlayer):
                text = 'You say "' + text + '"'
            else:
                text = event.sourceActor.name + ' says "' + text + '"'
            p = Paragraph(text)
            self.vbox.addWidget(p)
        elif event.__class__.__name__ == 'Narration':
            p = Paragraph(event.text)
            self.vbox.addWidget(p)
        elif event.__class__.__name__ == 'GetUserText':
            self.vbox.addWidget(Paragraph(event.caption))
            e = QtGui.QLineEdit()
            self.getUserText = e
            e.returnPressed.connect(self.onGetUserText)
            self.vbox.addWidget(e)
            e.setFocus()
    
    def onScrollRangeChanged(self, maxX, maxY):
        self.verticalScrollBar().setValue(maxY)
        
    def onGetUserText(self):
        self.completingTextInput = True
        #remove caption and QLineEdit
        oldText = self.vbox.takeAt(self.vbox.count() - 1)
        oldText.widget().deleteLater()
        oldText = self.vbox.takeAt(self.vbox.count() - 1)
        oldText.widget().deleteLater()
        #tell the gamestate about the text
        self.currentEvent.setText(self.getUserText.text())
        self.setFocus() # now that the QLineEdit is gone, get focus back to the scene view


class GameView(QtGui.QWidget):
    
    def __init__(self, gameState):
        super().__init__()
        self.gameState = gameState        
        self.gameState.sigEnterScene.connect(self.onEnterScene)
        self.vbox = QtGui.QVBoxLayout()
        self.setLayout(self.vbox)

    def showEvent(self, e):
        super().showEvent(e)
        self.setFocus()
        
    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.gameState.next()
        else:
            super().mousePressEvent(e)
    
    def keyPressEvent(self, e):
        if e.text() == '\r':
            self.gameState.next()
        else:
            super().keyPressEvent(e)
            
    def onEnterScene(self, scene):
        # Qt requires removing the layout item then explicitly deleting the widget on the layout item
        # Also note that we need the SceneView widget to act as a parent of all the widgets in the layout, otherwise we'd have to iterate them all and delete them explicitly
        if self.vbox.count() > 0:
            oldScene = self.vbox.takeAt(0)
            oldScene.widget().deleteLater()
        self.vbox.addWidget(SceneView(scene))

        
