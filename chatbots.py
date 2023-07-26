import openai
from PyQt5.QtWidgets import QApplication, QLabel, QWidget,QLineEdit,QScrollArea,QVBoxLayout,QHBoxLayout,QListWidget,QListWidgetItem,QStackedWidget,QFormLayout,QPushButton
from PyQt5.QtCore import Qt, QSize
import sys

key=""
def test():
    response=openai.ChatCompletion.create(model="gpt-3.5-turbo",
    messages=[
            {"role":"system","content":"Your are to be behaving like a normal person in its teen years. Respond in a way that coresponds to that"},
            {"role": "user", "content": "how are you?"},
        ])

class SignInPage(QWidget):
    def __init__(self,callback,*args):
        QWidget.__init__(self,*args)
        self.callback=callback
        self.layout=QFormLayout()
        self.keyInput=QLineEdit()
        self.buttonLayout=QHBoxLayout()
        self.submit=QPushButton("Submit")
        self.usePrev=QPushButton("Use Previous")
        self.buttonLayout.addWidget(self.usePrev)
        self.buttonLayout.addWidget(self.submit)
        self.layout.addRow("API-Key",self.keyInput)
        self.layout.addRow(self.buttonLayout)
        self.submit.clicked.connect(self.submitKey)
        self.setLayout(self.layout)

    def submitKey(self):
        openai.api_key=self.keyInput.text()
        print(self.keyInput.text())
        self.callback("menu")

class MainPage(QWidget):
    def __init__(self,*args):
        QWidget.__init__(self,*args)
        self.leftMenuScroll=QScrollArea()
        self.leftMenuWidget=QListWidget()
        self.leftMenuLayout=QVBoxLayout()
        self.mainLayout=QHBoxLayout()
        self.items=[]
        for i in range(1,50):
            self.items.append(QListWidgetItem(str(i)))
            self.leftMenuWidget.addItem(self.items[-1])

        
        self.leftMenuScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.leftMenuScroll.setWidget(self.leftMenuWidget)

        self.mainLayout.addWidget(self.leftMenuWidget)
        self.setLayout(self.mainLayout)
class MainWindow(QWidget):
    def __init__(self,*args):
        QWidget.__init__(self,*args)
        self.setWindowTitle("Chat Bot's")
        self.setGeometry(100, 100, 280, 80)
        self.stack=QStackedWidget(self)
        self.stack.addWidget(SignInPage(self.display))
        self.stack.addWidget(MainPage())
        #self.stack.addWidget(MainPage())
    def display(self,number):
        indexes={"signin":0,"menu":1,}
        print(indexes[number])
        self.stack.setCurrentIndex(indexes[number])

class App(QApplication):
    def __init__(self,*args):
        QApplication.__init__(self,*args)
        self.main=MainWindow()
        self.main.show()

    def endWindow(self):
        sys.exit(0)

def main():
    app = App(sys.argv)
    sys.exit(app.exec())

main()
