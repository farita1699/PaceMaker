'''
2022/10/13
This file imports many modules from the PyQt.5 environment to generate a GUI. The last few lines define an 
Application, and a Window (with size, title, and ability to exit).

The benefit of the PyQt environment is to generate well-formatted code for Graphical Interfaces given a 
custom build in PyQt Designer, a graphical user interface designer. 
PyQt is able to generate Python code from Qt Designer. As we do not need to distribute the GUI commercially,
we determined this environment to suit our front-end needs.
'''

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication
)
from frontend.splash_screen import SplashScreen
from frontend.main import Main

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # splash_screen = SplashScreen()
    # splash_screen.show()
    main = Main()
    main.show()
    sys.exit(app.exec())

print(sys.version)
