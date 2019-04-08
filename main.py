import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from login import *
from PyQt5.QtCore import Qt


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        self.name = ''
        self.password = ''

    def saveName(self, QString):
        # global name
        self.name = QString

    def savePassword(self, QString):
        # global password
        self.password = QString

    def register(self):
        with open('information.txt', 'a+') as f:
            # justify wether or not register
            # if not register ,register_flag=0
            # else register_flag>0
            register_flag = 0
            # make file Pointer in the first
            f.seek(0)
            # return a list include information
            s = f.readlines()
            for i in s:
                if self.name == i.strip('\n').split(' ')[0]:
                    self.success.setText(self.name + '已经注册，请重新注册')
                    # 自适应文本
                    self.success.adjustSize()
                    self.success.setWordWrap(True)
                    self.success.setAlignment(Qt.AlignCenter)
                    register_flag += 1
                    pass

            if register_flag == 0:
                f.writelines(self.name + ' ' + self.password + '\n')
                self.success.setText('恭喜' + self.name + '注册成功')
                # adjust the label size
                self.success.adjustSize()
                # make the word filling
                self.success.setWordWrap(True)
                # make the word in the center
                self.success.setAlignment(Qt.AlignCenter)
                f.flush()
                f.close()
                print('lichaofi' + self.name + self.password)

    def land(self):
        with open('information.txt', 'r') as f:
            land_flag = 0
            lines = f.readlines()
            for line in lines:
                if (self.name == line.strip('\n').split(' ')[0]) and (self.password == line.strip('\n').split(' ')[1]):
                    self.success.setText(self.name + '登陆成功')
                    # 自适应文本
                    self.success.adjustSize()
                    self.success.setWordWrap(True)
                    self.success.setAlignment(Qt.AlignCenter)
                    land_flag += 1

                elif (self.name == line.strip('\n').split(' ')[0]) and (self.password != line.strip('\n').split(' ')[1]):
                    self.success.setText('密码错误，请重新输入')
                    # 自适应文本
                    self.success.adjustSize()
                    self.success.setWordWrap(True)
                    self.success.setAlignment(Qt.AlignCenter)
                    land_flag += 1
                    break

            if land_flag == 0:
                self.success.setText(self.name + '没有注册，请注册之后再登陆')
                # 自适应文本
                self.success.adjustSize()
                self.success.setWordWrap(True)
                self.success.setAlignment(Qt.AlignCenter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
