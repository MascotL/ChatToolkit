import sys
import set_mode
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

import chat


class MyWindow(QWidget):

    def send_message(self, message):
        if message[0] == ".":
            display_text = "#" + message + "\n\n"
            self.top_left_output.insertPlainText(display_text)

            ret = set_mode.set_i(message)
            if ret == "":
                display_text = ret
            else:
                display_text = ret + "\n\n"
            self.top_left_output.insertPlainText(display_text)
            return "done"
        display_text = "You: " + message + "\n\n"
        self.top_left_output.insertPlainText(display_text)

    def chat_display(self, message):
        display_text = chat.chat(message) + "\n\n"
        self.top_left_output.insertPlainText(display_text)

    def click_run(self):
        message = self.bottom_left_input.text()
        self.bottom_left_input.clear()

        if not self.send_message(message) == "done":
            self.chat_display(message)

    def __init__(self):
        super().__init__()

        # 设置窗口大小和不可变大小
        self.setFixedSize(700, 400)

        # 窗口标题
        self.setWindowTitle('ChatToolkit')

        # 设置窗口图标
        self.setWindowIcon(QIcon('icon.ico'))

        # 创建上面的输出框
        self.top_left_output = QTextEdit(self)
        self.top_left_output.setReadOnly(True)
        self.top_left_output.setFixedSize(677, 340)
        self.top_left_output.setFont(QFont("Courier New", 10))

        # 下面左边输入框
        self.bottom_left_input = QLineEdit(self)
        self.bottom_left_input.move(10, 300)
        self.bottom_left_input.setFixedSize(600, 21)
        self.bottom_left_input.setAlignment(Qt.AlignVCenter)
        self.bottom_left_input.setFont(QFont("Courier New", 10))
        self.bottom_left_input.returnPressed.connect(self.click_run)

        # 下面右边按钮
        send_button = QPushButton('Send', self)
        send_button.setGeometry(590, 360, 100, 30)
        send_button.clicked.connect(self.click_run)

        # 将下面的输入框和按钮放在一个水平布局中
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.bottom_left_input)
        bottom_layout.addWidget(send_button)

        # 将上面的输出框、下面的输入框和按钮布局放在一个垂直布局中
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.top_left_output)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
