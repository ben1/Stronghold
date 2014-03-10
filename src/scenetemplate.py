'''
Created on 05/10/2013

@author: Ben
'''
from PySide import QtCore
import events


class SceneTemplate(QtCore.QObject):
    sigEvent = QtCore.Signal(events.Event)
    
    def __init__(self):
        super().__init__()

        
    


