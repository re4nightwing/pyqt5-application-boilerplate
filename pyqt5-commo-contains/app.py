import sys
from PyQt5.QtWidgets import (QCheckBox, QLineEdit, QPushButton, QLabel, QSlider, QApplication,
QWidget, QHBoxLayout, QVBoxLayout, QRadioButton)
from PyQt5 import QtGui
from PyQt5.QtCore import Qt


class Window(QWidget):
    
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        #Label
        self.l1 = QLabel('Test Application')
        self.l2 = QLabel()
        self.l2.setPixmap(QtGui.QPixmap('4k.jpg'))
        self.l3 = QLabel('Type of Vehicle : ')
        self.radioResL = QLabel()

        #lineEdit
        self.le1 = QLineEdit()

        #Button
        self.b1 = QPushButton('Push Me')
        self.b2 = QPushButton('Clear')
        self.b3 = QPushButton('Print')
        self.sub = QPushButton('Submit')

        #Slider
        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(1)
        self.s1.setMaximum(100)
        self.s1.setValue(25)
        self.s1.setTickInterval(10)
        self.s1.setTickPosition(QSlider.TicksBelow)

        #Check-Box
        self.ch1 = QCheckBox('Keep Me Signed In')

        #Radio-Button
        self.car = QRadioButton('Car')
        self.suv = QRadioButton('SUV')
        self.bike = QRadioButton('Bike')


        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l1)
        h_box.addStretch()

        h_box1 = QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.l2)
        h_box1.addStretch()

        h_box2 = QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.b1)
        h_box2.addStretch()

        h_box3 = QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.b3)
        h_box3.addStretch()
        h_box3.addWidget(self.b2)
        h_box3.addStretch()

        h_box4 = QHBoxLayout()
        h_box4.addStretch()
        h_box4.addWidget(self.ch1)
        h_box4.addStretch()

        h_box5 = QHBoxLayout()
        h_box5.addStretch()
        h_box5.addWidget(self.car)
        h_box5.addStretch()
        h_box5.addWidget(self.suv)
        h_box5.addStretch()
        h_box5.addWidget(self.bike)
        h_box5.addStretch()

        h_box6 = QHBoxLayout()
        h_box6.addStretch()
        h_box6.addWidget(self.sub)
        h_box6.addStretch()

        radioResLbl = QHBoxLayout()
        radioResLbl.addStretch()
        radioResLbl.addWidget(self.radioResL)
        radioResLbl.addStretch()

        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addLayout(h_box2)
        v_box.addWidget(self.le1)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)
        v_box.addWidget(self.l3)
        v_box.addLayout(h_box5)
        v_box.addLayout(h_box6)
        v_box.addLayout(radioResLbl)
        v_box.addLayout(h_box1)
        v_box.addWidget(self.s1)

        self.setLayout(v_box)
        self.setWindowTitle('Test Application')

        self.b1.clicked.connect(lambda: self.btn_click(self.b1, self.ch1.isChecked()))
        self.b2.clicked.connect(lambda: self.btn_click(self.b2, self.ch1.isChecked()))
        self.b3.clicked.connect(lambda: self.btn_click(self.b3, self.ch1.isChecked()))
        self.s1.valueChanged.connect(self.slider)
        self.sub.clicked.connect(self.radio_select)

        self.show()

    def btn_click(self, btn, checkBox):
        if (btn.text() == 'Push Me') & (checkBox):
            if self.l1.text() == 'Test Application[Checked]' :
                self.l1.setText('Tested Application[Checked]')
            else :
                self.l1.setText('Test Application[Checked]')
        elif (btn.text() == 'Push Me') & (checkBox != True):
            if self.l1.text() == 'Test Application' :
                self.l1.setText('Tested Application')
            else :
                self.l1.setText('Test Application')
        elif btn.text() == 'Clear':
            self.le1.clear()
        elif (btn.text() == 'Print') & (checkBox):
            print(self.le1.text()+' [Checked]')
        elif (btn.text() == 'Print') & (checkBox != True):
            print(self.le1.text())

    def slider(self):
        s_value = str(self.s1.value())
        self.le1.setText(s_value)

    def radio_select(self) :
        if self.car.isChecked():
            self.radioResL.setText('You Selected Car.')
        elif self.suv.isChecked():
            self.radioResL.setText('You Selected SUV.')
        elif self.bike.isChecked():
            self.radioResL.setText('You Selected Bike.')
        else :
            self.radioResL.setText('You Selected Nothing.')


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())

