import PyQt5
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication,QWidget
import sys

class Foo(QWidget):
    
    trigger = pyqtSignal()
    
    def __init__(self) -> None:
        super().__init__()

    # Define a new signal called 'trigger' that has no arguments.
    # self.trigger = pyqtSignal()

    def connect_and_emit_trigger(self):
        # Connect the trigger signal to a slot.
        self.trigger.connect(self.handle_trigger)

        # Emit the signal.
        self.trigger.emit()

    def handle_trigger(self):
        # Show that the slot has been called.
        print("trigger signal received")
        
class Windows(PyQt5.QWidget):
        # Creates a widget containing:
    # - a QLineEdit (status_widget)
    # - a button, connected to on_run_clicked

    def on_run_clicked(self):
        def update(text):
            self.widget.setText(text)

        threading.Thread(target=run, args=(update, )).start()
        
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Foo()
    ex.connect_and_emit_trigger()
    sys.exit(app.exec_())
    
   
    