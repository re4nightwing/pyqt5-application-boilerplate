import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5 import QtGui


class Window(QWidget):
    
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        
        self.setWindowTitle('Test Application')
        self.show()

    
app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())

