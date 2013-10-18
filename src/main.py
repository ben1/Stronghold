"""
"""
#from app import App
import sys
from PySide import QtGui, QtCore
from gamestate import GameState
#app = App()
#app.run()

class MainMenu(QtGui.QWidget):
    signalNew = QtCore.Signal()
    signalExit = QtCore.Signal()
    
    def __init__(self):
        super().__init__()
        hbox = QtGui.QHBoxLayout()
        self.setLayout(hbox)
        
        hbox.addStretch(3)
        vbox = QtGui.QVBoxLayout()
        hbox.addLayout(vbox, 2)
        hbox.addStretch(3)

        vbox.addStretch()
        btnNew = QtGui.QPushButton(' New Game ')
        btnNew.clicked.connect(lambda : self.signalNew.emit())
        btnNew.setStyleSheet('QPushButton{ font-size: 24px; padding: 8px; } QPushButton:hover{ color: darkgoldenrod;}')
        vbox.addWidget(btnNew)
        btnExit = QtGui.QPushButton('Exit')
        btnExit.clicked.connect(lambda : self.signalExit.emit())        
        btnExit.setStyleSheet('QPushButton{ font-size: 24px; padding: 8px; } QPushButton:hover{ color: darkgoldenrod;}')
        vbox.addWidget(btnExit)
        vbox.addStretch()


class Paragraph(QtGui.QLabel):

    def __init__(self, text):
        super().__init__()
        self.setText(text)  
        self.setWordWrap(True)


class GameView(QtGui.QWidget):
    
    def __init__(self, gameState):
        super().__init__()
        self.gameState = gameState
        
        hbox = QtGui.QHBoxLayout()
        self.setLayout(hbox)
        hbox.addStretch()
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addStretch()
        hbox.addLayout(self.vbox)
        hbox.addStretch()
        
        self.gameState.sigEnterScene.connect(self.onEnterScene)

    def mousePressEvent(self, e):
        self.gameState.next()

    def onEnterScene(self, scene):
        scene.sigEvent.connect(self.onSceneEvent)
        t = Paragraph(scene.name)
        self.vbox.insertWidget(self.vbox.count() - 1, t)

    def onSceneEvent(self, event):
        if event.__class__.__name__ == 'Say':
            text = event.text
            if(event.sourceActor.isPlayer):
                text = 'You say "' + text + '"'
            else:
                text = event.sourceActor.name + ' says "' + text + '"'
            self.vbox.insertWidget(self.vbox.count() - 1, Paragraph(text))
        elif event.__class__.__name__ == 'Narration':
            self.vbox.insertWidget(self.vbox.count() - 1, Paragraph(event.text))
        elif event.__class__.__name__ == 'GetUserText':
            self.vbox.insertWidget(self.vbox.count() - 1, Paragraph(event.caption))
            e = QtGui.QLineEdit()
            self.getUserText = e
            e.returnPressed.connect(self.onGetUserText)
            self.vbox.insertWidget(self.vbox.count() - 1, e)

    def onGetUserText(self):
        # do something with self.getUserText.text()
        

class AppWindow(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.gameState = None
        
    def initUI(self):
        font = QtGui.QFont('Calisto MT')
        QtGui.QApplication.setFont(font)
        self.setGeometry(100, 100, 1280, 768)
        self.setWindowTitle('Stronghold Demo')
        self.mainMenu = MainMenu()
        self.setCentralWidget(self.mainMenu)
        self.mainMenu.signalNew.connect(self.onNew)
        self.mainMenu.signalExit.connect(self.onExit)
        self.show()

        
    def onNew(self):
        if(self.gameState):
            msg = QtGui.QMessageBox()
            msg.setText('A game is already in progress.')
            msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            if msg.exec_() == QtGui.QMessageBox.Ok:
                self.gameState.cleanup()
            else:
                return
        self.gameState = GameState()
        self.gameView = GameView(self.gameState)
        self.gameState.init()
        self.setCentralWidget(self.gameView)
        
        
    def onExit(self):
        self.close()
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    appWnd = AppWindow()
    sys.exit(app.exec_())
    