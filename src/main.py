"""
The main routine for the application that creates the window, initial game state 
and kicks off the game.
"""
import sys
from PySide import QtGui, QtCore
from gamestate import GameState
from views import GameView
from logviews import LogGameView
import core_scenes


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
        #imperial.addSceneTemplates(self.gameState)
        core_scenes.addSceneTemplates(self.gameState)
        self.logGameView = LogGameView(self.gameState)
        self.gameView = GameView(self.gameState)
        self.gameState.setState('location', 'Stronghold')
        self.gameState.init()
        self.setCentralWidget(self.gameView)
        
        
    def onExit(self):
        self.close()
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    appWnd = AppWindow()
    sys.exit(app.exec_())
    