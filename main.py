from  PyQt5.QtWidgets import (QMainWindow, QApplication, 
QDesktopWidget)
from Vista.vista import Ui_MainWindow
import  sys
from Desing.Style import  style
from lexer import Lexer
class App(QMainWindow):
    def __init__(self):
        super(App,self).__init__()
        self.app = Ui_MainWindow()
        self.app.setupUi(self) 
        self.setStyleSheet(style)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2), 
        int((screen.height() - size.height())/2)) 
        
        # Preparamos el Lexer
        self.lexer = Lexer()
        self.lexer.build()
        # Eventos de teclado
        self.app.btn_push.clicked.connect(lambda: self.btnClicked())
        self.app.textEdit.setEnabled(False)
    def btnClicked(self):
        
        self.app.textEdit.setText("")
        texto = self.app.line_text.text()
        tokens = self.lexer.run(texto)

        cadena = ""
        for tok in tokens:
            cadena+= str(tok.type)+ ":"+ str(tok.value)+"\n\n"
            self.app.textEdit.setText(cadena)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = App()
    my_app.show()
    sys.exit(app.exec_())
