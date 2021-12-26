from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget


class SideBar(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setObjectName('sidebar')
        self.setStyleSheet("background-color: #383838;")
        self.setAutoFillBackground

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0,0,0,0)
        mainLayout.setSpacing(20)

        topbar = QHBoxLayout()
        topbar.setContentsMargins(10, 10, 10, 0)
        topbar.setSpacing(10)

        mainBar = QVBoxLayout()
        mainBar.setContentsMargins(0,0,0,0)
        mainBar.setSpacing(20)

        menuButton = QPushButton(QIcon('./ui/assets/img/menu.svg'), "")
        menuButton.setObjectName("menuButton")
        
        self.searchBox = QLineEdit()
        self.searchBox.setObjectName("searchBox")
        self.searchBox.setPlaceholderText("Search")

        self.userList = QListWidget()
        self.userList.setObjectName("userList")
        
        topbar.addWidget(menuButton)
        topbar.addWidget(self.searchBox)
        mainBar.addWidget(self.userList)

        mainLayout.addLayout(topbar)
        mainLayout.addLayout(mainBar)

        self.setLayout(mainLayout)


class ViewWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("viewWindow")
        self.setStyleSheet('background-color: #434343;')
        self.initUI()
    

    def initUI(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        self.listBox = QListWidget()
        self.listBox.setObjectName("listBox")
        layout.addWidget(self.listBox)
        self.setLayout(layout)


class ChatUI(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("chatUI")
        self.setStyleSheet("background-color: #383838;")

        mainLayout = QHBoxLayout()
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0,0,0,0)

        self.sidebar = SideBar()
        self.messagebox = ViewWindow()

        mainLayout.addWidget(self.sidebar)
        mainLayout.addWidget(self.messagebox)

        mainLayout.setStretch(0, 80)
        mainLayout.setStretch(1, 200)
        
        self.setLayout(mainLayout)