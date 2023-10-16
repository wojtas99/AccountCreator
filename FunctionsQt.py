from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


def create_button(window, x: int, y: int, width: int, height: int, text: str):
    button = QPushButton(text, window)
    button.setGeometry(x, y, width, height)
    return button


def create_textfield(window, x: int, y: int, width: int, height: int):
    textfield = QLineEdit(window)
    textfield.setGeometry(x, y, width, height)
    return textfield


def create_label(window, x: int, y: int, width: int, height: int, text: str):
    label = QLabel(text, window)
    label.setGeometry(x, y, width, height)
    return label


def create_checkbox(window, x: int, y: int, text: str):
    checkbox = QCheckBox(text, window)
    checkbox.move(x, y)
    return checkbox
