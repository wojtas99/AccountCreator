import random
from sendEmail import *
from Classes.Login_Window_Class import *
from PyQt5.QtWidgets import *
from dataBase import *
x, y, width, height = 175, 195, 150, 30


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget(self)
        #  Title and Size
        self.setWindowTitle("ScrapMaster")
        self.resize(500, 500)
        #  Text
        self.title = create_label(self, 125, 10, 250, 30, "Welcome to ScrapMaster V1.0")
        self.title.setFont(QFont("arial", 12))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #  Register
        self.register_button = create_button(self, x + 125, y + 150, width, height, "Register")  # Creates createAccount push button.
        self.register_button.clicked.connect(self.create_register_window)
        #  Create Account
        self.create_account = create_button(self, x, y + 245, width, height, "Create Account")  # Creates login push button.
        self.create_account.clicked.connect(self.code_window)
        self.create_account.hide()
        #  Login
        self.login_button = create_button(self, x - 125, y + 150, width, height, "Login")  # Creates login push button.
        self.login_button.clicked.connect(self.create_login_window)
        self.login_title = create_label(self, x, y, width, height, "Login:")
        self.login_title.setFont(QFont("arial", 10))
        self.login_textfield = create_textfield(self, x, y + 30, width, height)  # Create text field for login.
        self.login_textfield.hide()
        self.login_title.hide()
        #  Password
        self.password_title = create_label(self, x, y + 75, width, height, "Password:")
        self.password_title.setFont(QFont("arial", 10))
        self.password_textfield = create_textfield(self, x, y + 105, width, height)  # Create text field for password.
        self.password_textfield.setEchoMode(QLineEdit.EchoMode.Password)  # Create EchoMode Password
        self.password_checkbox = create_checkbox(self, x + width + 5, y + 110, "Show Password")
        self.password_checkbox.hide()
        self.password_checkbox.stateChanged.connect(self.show_password)
        self.password_textfield.hide()
        self.password_title.hide()
        #  Verification Code
        self.verification_title = create_label(self, x, y + 75, width, height, "Verification Code:")
        self.verification_title.hide()
        self.verification_textfield = create_textfield(self, x, y + 105, width, height)
        self.verification_textfield.hide()
        self.verification_button = create_button(self, x, y + 140, width, height, "Activate")  # Creates Activate Button
        self.verification_button.clicked.connect(self.activate)
        self.verification_button.hide()
        #  E-mail
        self.mail_title = create_label(self, x, y + 145, width, height, "E-mail:")
        self.mail_title.setFont(QFont("arial", 10))
        self.mail_textfield = create_textfield(self, x, y + 185, width, height)  # Create text field for login.
        self.mail_textfield.hide()
        self.mail_title.hide()

        # Used
        self.used = create_label(self, 125, 100, 250, 30, "")
        self.login_class = None

    def activate(self):
        code = sendQueryReturn(f"SELECT * FROM Client WHERE userEmail = '{self.mail_textfield.text()}'")
        if int(code) == int(self.verification_textfield.text()):
            self.used.setText("Account activated.")
            self.used.setFont(QFont("arial", 12))
            self.used.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.used.setStyleSheet("color: green")
            self.verification_textfield.hide()
            self.verification_title.hide()
            self.verification_button.hide()
            self.login_button.show()
            self.login_button.move(x, y + 40)
        else:
            self.used.setText("Wrong Code.")
            self.used.setFont(QFont("arial", 12))
            self.used.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.used.setStyleSheet("color: red")

    def code_window(self):
        code = random.randint(1000, 9999)
        data = sendQuery(f"INSERT INTO Client VALUES ({code},'{self.login_textfield.text()}'"
                               f",'{self.mail_textfield.text()}','{self.password_textfield.text()}',{0})")
        if data != '':
            #  Text
            self.used.setText("The account name is already used.")
            self.used.setFont(QFont("arial", 12))
            self.used.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.used.setStyleSheet("color: red")
        else:
            #  Hide Button
            self.create_account.hide()
            #  Hide Email
            self.mail_title.hide()
            self.mail_textfield.hide()
            #  Hide Password
            self.password_textfield.hide()
            self.password_title.hide()
            self.password_checkbox.hide()
            #  Hide Login
            self.login_title.hide()
            self.login_textfield.hide()
            #  Verification Code
            self.verification_textfield.show()
            self.verification_title.show()
            self.verification_button.show()
            #  Text
            self.used.setText("Successfully created account.")
            self.used.setFont(QFont("arial", 12))
            self.used.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.used.setStyleSheet("color: green")
            #  Send mail
            sendMail(self.mail_textfield.text(), code)

    def create_login_window(self):
        self.login_class = Login_Window()
        self.close()
        self.login_class.show()

    def create_register_window(self):
        #  Hide Login
        self.login_button.hide()
        self.register_button.hide()
        #  Show Password
        self.password_textfield.show()
        self.password_title.show()
        self.password_checkbox.show()
        #  Show Mail
        self.mail_textfield.show()
        self.mail_title.show()
        #  Show Login
        self.login_title.show()
        self.login_textfield.show()

        self.create_account.show()

    def show_password(self, state):
        if state == 0:
            self.password_textfield.setEchoMode(QLineEdit.EchoMode.Password)
        else:
            self.password_textfield.setEchoMode(QLineEdit.EchoMode.Normal)
