from display.login import Ui_LoginForm
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit

from frontend.main import Main
from backend.login import check_duplicate, create_new_user, login_check, check_exceed_max_users, check_new_password, check_new_username, get_user_info


class Login(QMainWindow, Ui_LoginForm):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def show_register_popup(self, input):
        msg = QMessageBox()
        msg.setWindowTitle("PaceMaker")
        if (input == 1):
            msg.setText("Duplicate username detected")
        elif (input == 2):
            msg.setText("Duplicate username detected")
        elif(input == 3):
            msg.setText("Inappropriate Password: You must have a minimum 8 character password with an uppercase and lowercase letter, no spaces, and at least 1 digit.")
        elif(input == 4):
            msg.setText("Inappropriate Username: You must have a username with no spaces!")
        else:
            msg.setText("Test")
        x = msg.exec_()

    def show_login_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("PaceMaker Login")
        msg.setText("Your Username and/or Password is invalid")
        x = msg.exec_()

    def register(self):
        if (check_duplicate(self.UsernameInput.text())):
            #To do: make this an error text on the UI
            print("Duplicate detected")
            self.show_register_popup(1)
        elif(check_exceed_max_users()):
            print("Exceed max users")
            self.show_register_popup(2)
        elif(check_new_password(self.PasswordInput.text())):
            print("Inappropriate Password")
            self.show_register_popup(3)
        elif(check_new_username(self.UsernameInput.text())):
            print("Inappropriate Username")
            self.show_register_popup(4)
        else:
            create_new_user(self.UsernameInput.text(), self.PasswordInput.text())   

    def login(self):
        user_id = login_check(self.UsernameInput.text(), self.PasswordInput.text())
        if (user_id):
            if (get_user_info(user_id, self.UsernameInput.text())):
                self.main = Main()
                self.main.show()
            else:
                print("Error: get_user_info(user_id, username) failed")
            
        else:
            self.show_login_popup()