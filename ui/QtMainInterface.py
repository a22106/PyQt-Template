import sys
from abc import ABC, abstractmethod
from PySide6 import QtWidgets

class QtMainInterface(ABC):
    def __init__(self, ui_class) -> None:
        super().__init__()
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.ui = ui_class()
        self.ui.setupUi(self.main_window)
        self.Dialog = QtWidgets.QDialog()