from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QPushButton,QRadioButton,QMessageBox,QLineEdit
from PyQt5.QtGui import QFont
import sys,random
ls=[0,"*","/","+",1,2,3,"-",4,5,6,".",7,8,9,"="]


class Tugma(QPushButton):
    def __init__(self,name,ob,x,y):
        super().__init__(name,ob)
        self.setFont(QFont("Times",40))
        self.setGeometry(x,y,100,100)
    def click(self,fun):
        self.clicked.connect(fun)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,550,600)
        self.begin()
    def font(self,ob):
        ob.setFont(QFont("Times",40))
    def begin(self):
        
        self.a1=Tugma("",self,50,160)
        self.a2=Tugma("",self,160,160)
        self.a3=Tugma("",self,270,160)
        self.a4=Tugma("",self,380,160)
        self.a5=Tugma("",self,50,270)
        self.a6=Tugma("",self,160,270)
        self.a7=Tugma("",self,270,270)
        self.a8=Tugma("",self,380,270)
        self.a9=Tugma("",self,50,380)
        self.a10=Tugma("",self,160,380)
        self.a11=Tugma("",self,270,380)
        self.a12=Tugma("",self,380,380)
        self.a13=Tugma("",self,50,490)
        self.a14=Tugma("",self,160,490)
        self.a15=Tugma("",self,270,490)
        self.a16=Tugma("",self,380,490)
        self.a17=QPushButton("C",self)
        self.a17.setFont(QFont("Times",35))
        self.a17.move(475,50)
        self.txt=QLineEdit(self)
        self.txt.setFont(QFont("Times",35))
        self.txt.move(49,50)
        self.numbers=[self.a1,self.a2,self.a3,self.a4,self.a5,self.a6,self.a7,self.a8,self.a9,self.a10,self.a11,self.a12,self.a13,self.a14,self.a15,self.a16]
        for i in range(16):
            self.numbers[i].setText(str(ls[i]))

        self.a1.click(self.A1)
        self.a2.click(self.A2)
        self.a3.click(self.A3)
        self.a4.click(self.A4)
        self.a5.click(self.A5)
        self.a6.click(self.A6)
        self.a7.click(self.A7)
        self.a8.click(self.A8)
        self.a9.click(self.A9)
        self.a10.click(self.A10)
        self.a11.click(self.A11)
        self.a12.click(self.A12)
        self.a13.click(self.A13)
        self.a14.click(self.A14)
        self.a15.click(self.A15)
        self.a16.click(self.A16)
        self.a17.clicked.connect(self.A17)

    def A1(self):
        self.txt.setText(self.txt.text()+"0")
    def A2(self):
        self.txt.setText(self.txt.text()+"*")
    def A3(self):
        self.txt.setText(self.txt.text()+"/")
    def A4(self):
        self.txt.setText(self.txt.text()+"*")
    def A5(self):
        self.txt.setText(self.txt.text()+"1")
    def A6(self):
        self.txt.setText(self.txt.text()+"2")
    def A7(self):
        self.txt.setText(self.txt.text()+"3")
    def A8(self):
        self.txt.setText(self.txt.text()+"-")
    def A9(self):
        self.txt.setText(self.txt.text()+"4")
    def A10(self):
        self.txt.setText(self.txt.text()+"5")
    def A11(self):
        self.txt.setText(self.txt.text()+"6")
    def A12(self):
        self.txt.setText(self.txt.text()+".")
    def A13(self):
        self.txt.setText(self.txt.text()+"7")
    def A14(self):
        self.txt.setText(self.txt.text()+"8")
    def A15(self):
        self.txt.setText(self.txt.text()+"9")
    def A16(self):
        try:
            self.sum=str(eval(self.txt.text()))
            self.txt.setText(self.sum)
        except:
            self.txt.setText("0ga bo'linmaydi")   
    def A17(self):
        self.txt.clear()

app=QApplication(sys.argv)
oyna=Window()
oyna.show()
sys.exit(app.exec_())
