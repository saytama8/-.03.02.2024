import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt
import math  # Імпорт модулю для обчислення кореня


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Калькулятор')
        self.setGeometry(100, 100, 300, 400)

        self.init_ui()

    def init_ui(self):
        self.display = QLineEdit(self)
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        buttons = [
            ('7', self.add_to_display),
            ('8', self.add_to_display),
            ('9', self.add_to_display),
            ('/', self.add_to_display),
            ('4', self.add_to_display),
            ('5', self.add_to_display),
            ('6', self.add_to_display),
            ('*', self.add_to_display),
            ('1', self.add_to_display),
            ('2', self.add_to_display),
            ('3', self.add_to_display),
            ('-', self.add_to_display),
            ('0', self.add_to_display),
            ('.', self.add_to_display),
            ('%', self.add_percent),
            ('+', self.add_to_display),
            ('C', self.clear_display),
            ('=', self.calculate_result),
            ('√', self.calculate_square_root),  # Додано кнопку для кореня
        ]

        grid_layout = QGridLayout()
        row, col = 1, 0

        for button_text, callback in buttons:
            button = QPushButton(button_text, self)
            button.clicked.connect(callback)
            grid_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)
        main_layout.addLayout(grid_layout)

        self.setLayout(main_layout)

    def add_to_display(self):
        sender = self.sender()
        current_text = self.display.text()
        new_text = current_text + sender.text()
        self.display.setText(new_text)

    def add_percent(self):
        current_text = self.display.text()
        try:
            result = eval(current_text) / 100
            self.display.setText(str(result))
        except Exception as e:
            self.display.setText('Error')

    def clear_display(self):
        self.display.clear()

    def calculate_result(self):
        current_text = self.display.text()
        try:
            result = eval(current_text)
            self.display.setText(str(result))
        except Exception as e:
            self.display.setText('Error')

    def calculate_square_root(self):
        current_text = self.display.text()
        try:
            result = math.sqrt(eval(current_text))  # Обчислення кореня
            self.display.setText(str(result))
        except Exception as e:
            self.display.setText('Error')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())
