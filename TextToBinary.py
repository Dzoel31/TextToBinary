#Import library
from PyQt5.QtWidgets import *
import sys

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.setWindowTitle("Converter")
        self.resize(300,200)

        #QLabel untuk membuat label
        #QLineEdit untuk membuat box input
        self.labelinput = QLabel("Masukkan text")
        self.Input = QLineEdit("")
        self.labelOutput = QLabel("Hasil Konversi")
        self.Output = QLineEdit("")
        
        #QPushButton untuk membuat tombol
        #Clicked untuk signal bila tombol diklik, bila diklik akan memanggil fungsi
        self.ResultButton = QPushButton("Konversi", clicked = self.Result) 
        self.ResetButton = QPushButton("Reset", clicked = self.Reset)
        self.ChangeButton = QPushButton("Tukar", clicked = self.Change)
        self.ChangeButton.setCheckable(True) #Agar program mengenali tombol bila diklik atau tidak

        #QHBoxLayout untuk membuat box/widget secara horizontal
        hbox = QHBoxLayout()
        hbox.addWidget(self.ResultButton)
        hbox.addWidget(self.ResetButton)
        hbox.addWidget(self.ChangeButton)

        #QVBoxLayout untuk membuat box/widget secara vertikal
        vbox = QVBoxLayout()
        vbox.addWidget(self.labelinput)
        vbox.addWidget(self.Input)
        vbox.addLayout(hbox)
        vbox.addWidget(self.labelOutput)
        vbox.addWidget(self.Output)

        #Set layout
        self.setLayout(vbox)
    
    def Result(self):
        InputText = self.Input.text()
        list_desimal = []
        list_result = []

        if self.ChangeButton.isChecked():
            list_biner = InputText.split(" ")

            for biner in list_biner:
                in_decimal = 0
                for i in range(len(biner)):
                    in_decimal += int(biner[::-1][i]) * 2 ** i
                list_desimal.append(in_decimal)
            
            for item in list_desimal:
                list_result.append(chr(item))
            
            self.Output.setText("".join(list_result))

        else:
            for char in InputText:
                list_desimal.append(ord(char))

            for desimal in list_desimal:
                result_convert = ""
                while desimal != 0:
                    mod = desimal % 2
                    result_convert += f"{mod}"
                    desimal //= 2
            
                list_result.append(f"{int(result_convert[::-1]):08d}")

            result = ""
            for binary in list_result:
                if len(result) == 0 :
                    result = result + binary
                else:
                    result = result + " " + binary            
            self.Output.setText(result)
        
    def Reset(self):
        self.Input.setText("")
        self.Output.setText("")
    
    def Change(self):
        if self.ChangeButton.isChecked():
            self.labelinput.setText("Masukkan biner")
        else :
            self.labelinput.setText("Masukkan text")
    
App = QApplication(sys.argv)
Window = MainApp()
Window.show()
App.exec_()