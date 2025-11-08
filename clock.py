# Digital clock in PyQt5
import sys 
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout 
from PyQt5.QtCore import QTimer, QTime, Qt 

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__() 
        
        self.time_label = QLabel(self)  
        self.timer = QTimer(self) 
        self.initUI()

    def initUI(self):
        # setting an icon
        icon_path = os.path.join(os.path.dirname(__file__), "clock.jpg") 
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print("Icon not found:", icon_path)
        
        self.setWindowTitle("Timer")
        self.setGeometry(300, 350, 700, 200) 
        vbox = QVBoxLayout(self) 
        vbox.addWidget(self.time_label) 
        self.time_label.setStyleSheet("font-size: 250px;"
                                      "color: #0a8024;"
                                      "background-color: #000000") 
        
        self.timer.timeout.connect(self.update_time) 
        self.timer.start(1000)  

        self.time_label.setAlignment(Qt.AlignCenter)  
        self.update_time() 
        
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_()) 