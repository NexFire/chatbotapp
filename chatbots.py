import openai
from PyQt5.QtWidgets import QApplication, QLabel, QWidget,QLineEdit,QScrollArea,QVBoxLayout,QHBoxLayout,QListWidget,QListWidgetItem
from PyQt5.QtCore import Qt, QSize
import sys



response=openai.ChatCompletion.create(model="gpt-3.5-turbo",
  messages=[
        {"role":"system","content":"Your are to be behaving like a normal person in its teen years. Respond in a way that coresponds to that"},
        {"role": "user", "content": "how are you?"},
    ])

def main():
    app = QApplication([])
    window = QWidget()
    leftMenuScroll=QScrollArea()
    leftMenuWidget=QListWidget()
    leftMenuLayout=QVBoxLayout()
    mainLayout=QHBoxLayout()
    items=[]
    for i in range(1,50):
        items.append(QListWidgetItem(str(i)))
        leftMenuWidget.addItem(items[-1])

    window.setWindowTitle("Chat Bot's")
    window.setGeometry(100, 100, 280, 80)
    leftMenuScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    leftMenuScroll.setWidget(leftMenuWidget)

    mainLayout.addWidget(leftMenuWidget)
    window.setLayout(mainLayout)
    window.show()
    sys.exit(app.exec())

main()
