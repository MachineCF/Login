import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from loginWindows import *
from mainWindows import *
from PyQt5.QtCore import Qt


class login(QMainWindow, Ui_MainWindow_Login):
    def __init__(self, parent=None):
        super(login, self).__init__(parent)
        self.setupUi(self)

        self.name = ''
        self.password = ''

    def saveName(self, QString):
        # global name
        self.name = QString

    def savePassword(self, QString):
        # global password
        self.password = QString

    def echoWaringLand(self, value):
        if value==QMessageBox.Yes:
            self.password_edit.setText('')
        if value==QMessageBox.No:
            self.password_edit.setText('')
            self.name_edit.setText('')

    def waringLand(self,event):  # 消息：警告
        reply = QMessageBox.warning(self,
                                    "警告",
                                    event,
                                    QMessageBox.Yes | QMessageBox.No)
        self.echoWaringLand(reply)


    def waringRegisterToLand(self,event):  # 消息：警告
        reply = QMessageBox.warning(self,
                                    "警告",
                                    event,
                                    QMessageBox.Yes | QMessageBox.No)
        self.echoRegisterToLand(reply)

    def echoRegisterToLand(self, value):
        if value==QMessageBox.No:
            self.password_edit.setText('')
            self.name_edit.setText('')


    def waring(self,event):  # 消息：警告
        reply = QMessageBox.warning(self,
                                    "警告",
                                    event,
                                    QMessageBox.Yes | QMessageBox.No)
        pass



    def register(self):
        if len(self.name)==0 :
            self.waring('用户名不能为空')
        if len(self.name)>0 and len(self.password)<5:
            self.waring('密码不少于5位数')

        if len(self.name) >0 and len(self.password) >= 5:
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
                        self.waringRegisterToLand('该用户已经注册，请登录')
                        register_flag += 1
                        pass

                if register_flag == 0:
                    f.writelines(self.name + ' ' + self.password + '\n')
                    self.success.setText('恭喜用户：' + self.name + ' 注册成功')
                    # adjust the label size
                    self.success.adjustSize()
                    # make the word filling
                    self.success.setWordWrap(True)
                    # make the word in the center
                    self.success.setAlignment(Qt.AlignCenter)
                    f.flush()
                    f.close()
                    self.name_edit.setText('')
                    self.password_edit.setText('')
                    # print('lichaofi' + self.name + self.password)

    def land(self):
        if len(self.name)==0 :
            self.waring('用户名不能为空')
        if len(self.name)>0 and len(self.password)<5:
            self.waring('密码不少于5位数')
        if len(self.name) > 0 and len(self.password) >= 5:
            with open('information.txt', 'r') as f:
                land_flag = 0
                lines = f.readlines()
                for line in lines:
                    if (self.name == line.strip('\n').split(' ')[0]) and (self.password == line.strip('\n').split(' ')[1]):
                        land_flag += 1
                        mainWindows_show.show()
                        login_show.hide()

                    elif (self.name == line.strip('\n').split(' ')[0]) and (
                            self.password != line.strip('\n').split(' ')[1]):
                        self.waringLand('密码错误，请重新输入')
                        land_flag += 1
                        break

                if land_flag == 0:

                    self.success.setText(self.name + '没有注册，请注册之后再登陆')
                    # 自适应文本
                    self.success.adjustSize()
                    self.success.setWordWrap(True)
                    self.success.setAlignment(Qt.AlignCenter)
                f.close()


class mainWindows(QMainWindow, Ui_MainWindow_Main):
    def __init__(self, parent=None):
        super(mainWindows, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_show = login()
    login_show.show()
    mainWindows_show = mainWindows()
    sys.exit(app.exec_())
