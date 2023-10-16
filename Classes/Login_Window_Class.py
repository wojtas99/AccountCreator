from FunctionsQt import *

x, y, width, height = 175, 195, 150, 30


class Login_Window(QWidget):
    def __init__(self):
        super().__init__()
        #  Window Properties
        self.setWindowTitle("ScrapMaster")
        self.resize(500, 500)
        #  Text
        self.title = create_label(self, 125, 10, 250, 30, "Welcome to ScrapMaster V1.0")
        self.title.setFont(QFont("arial", 12))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #  Login
        self.login_title = create_label(self, x, y, width, height, "Login:")
        self.login_title.setFont(QFont("arial", 10))
        self.login_button = create_button(self, x, y + 155, width, height, "Login")  # Creates login push button.
        self.login_textfield = create_textfield(self, x, y + 30, width, height)  # Create text field for login.
        #  Password
        self.password_title = create_label(self, x, 270, width, height, "Password:")
        self.password_title.setFont(QFont("arial", 10))
        self.password_textfield = create_textfield(self, x, y + 105, width, height)  # Create text field for password.
        self.password_textfield.setEchoMode(QLineEdit.EchoMode.Password)  # Create EchoMode Password