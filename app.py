import sys
from PySide6 import QtWidgets, QtCore, QtGui
from ui.QtMainInterface import QtMainInterface
from ui.appui_ui import Ui_MainWindow

class ExampleProgram(QtMainInterface):
    def __init__(self, ui_class) -> None:
        super().__init__(ui_class)
        self.ui.pushButton.clicked.connect(self.on_button_clicked)
        self.main_window.show()
        sys.exit(self.app.exec_())

    @QtCore.Slot()
    def on_button_clicked(self):
        print("Button clicked")
        
def main():
    ui = ExampleProgram(Ui_MainWindow)
    program = ExampleProgram(ui_class=ui)
    program.run()
    
if __name__ == "__main__":
    main()