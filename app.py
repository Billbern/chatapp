import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QPushButton, QLineEdit, QStackedLayout, QVBoxLayout, QWidget
from ui.chat import ChatUI


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        self.mainwidget = QWidget()
        self.stacklayout = QStackedLayout()
        
        login = LoginUI()
        login.label3.clicked.connect(lambda : self.stacklayout.setCurrentIndex(1))
        login.button.clicked.connect(self.loggedIn)
       
        signup = SignupUI()
        signup.labelbutton.clicked.connect(lambda : self.stacklayout.setCurrentIndex(0))
        
        chats = ChatUI()
        
        self.stacklayout.addWidget(login)
        self.stacklayout.addWidget(signup)
        self.stacklayout.addWidget(chats)

        self.mainwidget.setLayout(self.stacklayout)
        self.setCentralWidget(self.mainwidget)
    
    
    def loggedIn(self):
        self.stacklayout.setCurrentIndex(2)


class LoginUI(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("AuthPage")
        layout = QVBoxLayout()

        label = QLabel("Login")
        label.setObjectName("PageTitle")
        layout.addWidget(label, 0, Qt.AlignCenter)


        vbox = QVBoxLayout()
        

        self.username = QLineEdit()
        self.username.setPlaceholderText("username")
        vbox.addWidget(self.username, 0, Qt.AlignCenter)
        

        self.password = QLineEdit()
        self.password.setPlaceholderText("password")
        vbox.addWidget(self.password, 0, Qt.AlignCenter)
        
        layout.addLayout(vbox, 0)

        vbox1 = QVBoxLayout()

        self.button = QPushButton("submit")
        self.button.setObjectName("LoginBtn")
        vbox1.addWidget(self.button, 0, Qt.AlignCenter)

        hbox = QHBoxLayout()

        label2 = QLabel("Not having an account? ")
        label2.setObjectName("bottomLabel")
        hbox.addWidget(label2, 0, Qt.AlignRight)

        self.label3 = QPushButton("register")
        self.label3.setObjectName("bottomButton")
        hbox.addWidget(self.label3, 0, Qt.AlignLeft)


        hbox.setStretch(0, 450)
        hbox.setStretch(1, 350)

        vbox1.addLayout(hbox, 0)
    

        layout.addLayout(vbox1)

        self.setLayout(layout)


class SignupUI(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("AuthPage")

        layout = QVBoxLayout()

        title = QLabel("Sign Up")
        title.setObjectName("PageTitle")
        layout.addWidget(title, 0, Qt.AlignCenter)

        vbox = QVBoxLayout()

        self.fullname = QLineEdit()
        self.fullname.setPlaceholderText("full name")
        vbox.addWidget(self.fullname, 0, Qt.AlignCenter)

        self.username = QLineEdit()
        self.username.setPlaceholderText("username")
        vbox.addWidget(self.username, 0, Qt.AlignCenter)

        self.password = QLineEdit()
        self.password.setPlaceholderText("password")
        vbox.addWidget(self.password, 0, Qt.AlignCenter)


        button = QPushButton("submit")
        button.setObjectName("SignupBtn")
        vbox.addWidget(button, 0, Qt.AlignCenter)
        
        layout.addLayout(vbox)

        hbox = QHBoxLayout()

        label = QLabel("Already have an account? ")
        label.setObjectName("bottomLabel")
        hbox.addWidget(label, 0, Qt.AlignRight) 

        self.labelbutton = QPushButton("Sign in")
        self.labelbutton.setObjectName("bottomButton")
        hbox.addWidget(self.labelbutton, 0, Qt.AlignLeft)

        hbox.setStretch(0, 450)
        hbox.setStretch(1, 350)

        layout.addLayout(hbox)

        self.setLayout(layout)





if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(open("./ui/assets/css/style.css").read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())