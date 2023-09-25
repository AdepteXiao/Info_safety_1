import tricemus_cipher
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, \
    QHBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QTextEdit

class TextEncryptionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.result_text = None
        self.process_button = None
        self.operation_group = None
        self.decryption_radio = None
        self.encryption_radio = None
        self.keyword_input = None
        self.keyword_label = None
        self.text_input = None
        self.text_label = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Шифрование и дешифрование текста')
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.text_label = QLabel('Введите текст:', self)
        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_label)
        layout.addWidget(self.text_input)

        self.keyword_label = QLabel('Введите ключевое слово:', self)
        self.keyword_input = QLineEdit(self)
        layout.addWidget(self.keyword_label)
        layout.addWidget(self.keyword_input)

        self.encryption_radio = QRadioButton('Зашифровать', self)
        self.decryption_radio = QRadioButton('Расшифровать', self)
        self.operation_group = QHBoxLayout()
        self.operation_group.addWidget(self.encryption_radio)
        self.operation_group.addWidget(self.decryption_radio)
        layout.addLayout(self.operation_group)

        self.result_text = QTextEdit(self)
        layout.addWidget(self.result_text)

        self.process_button = QPushButton('Выполнить', self)
        self.process_button.clicked.connect(self.processText)
        layout.addWidget(self.process_button)

        central_widget.setLayout(layout)

    def processText(self):
        cipher = tricemus_cipher.Tricemus()
        text = self.text_input.text().upper()
        keyword = self.keyword_input.text().upper()
        cipher.creating_table(keyword)

        if self.encryption_radio.isChecked():
            self.result_text.setPlainText(cipher.cipher(text))
        elif self.decryption_radio.isChecked():
            self.result_text.setPlainText(cipher.decipher(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextEncryptionApp()
    window.show()
    sys.exit(app.exec_())

