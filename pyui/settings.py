# Form implementation generated from reading ui file 'ui/settings.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog, theme):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 263)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/../resource/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(theme)
        self.p_box = QtWidgets.QGroupBox(parent=Dialog)
        self.p_box.setGeometry(QtCore.QRect(20, 80, 171, 165))
        self.p_box.setObjectName("p_box")
        self.pass1 = QtWidgets.QLineEdit(parent=self.p_box)
        self.pass1.setGeometry(QtCore.QRect(10, 30, 141, 25))
        self.pass1.setStyleSheet("background-color: rgb(239, 241, 255)")
        self.pass1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.pass1.setObjectName("pass1")
        self.pass2 = QtWidgets.QLineEdit(parent=self.p_box)
        self.pass2.setGeometry(QtCore.QRect(10, 65, 141, 25))
        self.pass2.setStyleSheet("background-color: rgb(239, 241, 255)")
        self.pass2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.pass2.setObjectName("pass2")
        self.pshow = QtWidgets.QCheckBox(parent=self.p_box)
        self.pshow.setGeometry(QtCore.QRect(10, 130, 121, 23))
        self.pshow.setObjectName("pshow")
        self.pass_try = QtWidgets.QLineEdit(parent=self.p_box)
        self.pass_try.setGeometry(QtCore.QRect(10, 100, 141, 25))
        self.pass_try.setStyleSheet("background-color: rgb(239, 241, 255)")
        self.pass_try.setText("")
        self.pass_try.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.pass_try.setObjectName("pass_try")
        self.k_box = QtWidgets.QGroupBox(parent=Dialog)
        self.k_box.setGeometry(QtCore.QRect(20, 0, 171, 71))
        self.k_box.setObjectName("k_box")
        self.user = QtWidgets.QLineEdit(parent=self.k_box)
        self.user.setGeometry(QtCore.QRect(10, 30, 141, 25))
        self.user.setStyleSheet("background-color: rgb(239, 241, 255)")
        self.user.setObjectName("user")
        self.ac_box = QtWidgets.QGroupBox(parent=Dialog)
        self.ac_box.setGeometry(QtCore.QRect(200, 80, 271, 131))
        self.ac_box.setObjectName("ac_box")
        self.fileName = QtWidgets.QLineEdit(parent=self.ac_box)
        self.fileName.setGeometry(QtCore.QRect(10, 30, 201, 25))
        self.fileName.setStyleSheet("background-color: rgb(239, 241, 255)")
        self.fileName.setText("")
        self.fileName.setObjectName("fileName")
        self.sep = QtWidgets.QLineEdit(parent=self.ac_box)
        self.sep.setGeometry(QtCore.QRect(10, 70, 201, 25))
        self.sep.setStyleSheet("background-color: rgb(239, 241, 255)")
        self.sep.setObjectName("sep")
        self.fileChoiser = QtWidgets.QPushButton(parent=self.ac_box)
        self.fileChoiser.setGeometry(QtCore.QRect(220, 30, 31, 23))
        self.fileChoiser.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/../resource/ch.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.fileChoiser.setIcon(icon1)
        self.fileChoiser.setIconSize(QtCore.QSize(32, 20))
        self.fileChoiser.setObjectName("fileChoiser")
        self.t_box = QtWidgets.QGroupBox(parent=Dialog)
        self.t_box.setGeometry(QtCore.QRect(200, 0, 271, 71))
        self.t_box.setObjectName("t_box")
        self.theme = QtWidgets.QComboBox(parent=self.t_box)
        self.theme.setGeometry(QtCore.QRect(10, 30, 201, 25))
        self.theme.setObjectName("theme")
        self.theme.addItem("")
        self.theme.addItem("")
        self.theme.addItem("")
        self.theme.addItem("")
        self.theme.addItem("")
        self.theme.addItem("")
        self.theme.addItem("")
        self.theme.addItem("")
        self.theme.addItem("")
        self.theme.addItem("")
        self.save_quit = QtWidgets.QPushButton(parent=Dialog)
        self.save_quit.setGeometry(QtCore.QRect(200, 220, 181, 25))
        self.save_quit.setObjectName("save_quit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.p_box.setTitle(_translate("Dialog", "Şifreni değistir"))
        self.pass1.setPlaceholderText(_translate("Dialog", "Eski şifre"))
        self.pass2.setPlaceholderText(_translate("Dialog", "Yeni şifre"))
        self.pshow.setText(_translate("Dialog", "Şifreyi göster"))
        self.pass_try.setPlaceholderText(_translate("Dialog", "Tekrar yeni şifre"))
        self.k_box.setTitle(_translate("Dialog", "Kullanıcı adını değiştir"))
        self.user.setPlaceholderText(_translate("Dialog", "Kullanıcı adı"))
        self.ac_box.setTitle(_translate("Dialog", "Instagram hesap dosya bilgileri"))
        self.fileName.setPlaceholderText(_translate("Dialog", "Dosya yolu"))
        self.sep.setPlaceholderText(_translate("Dialog", "Şifre ayırıcı"))
        self.t_box.setTitle(_translate("Dialog", "Temalar"))
        self.theme.setItemText(0, _translate("Dialog", "Default"))
        self.theme.setItemText(1, _translate("Dialog", "Beşiktaş"))
        self.theme.setItemText(2, _translate("Dialog", "Galatasaray"))
        self.theme.setItemText(3, _translate("Dialog", "Fenerbahçe"))
        self.theme.setItemText(4, _translate("Dialog", "Trabzonspor"))
        self.theme.setItemText(5, _translate("Dialog", "Siyah"))
        self.theme.setItemText(6, _translate("Dialog", "Acik mavi"))
        self.theme.setItemText(7, _translate("Dialog", "Sari"))
        self.theme.setItemText(8, _translate("Dialog", "Kirmizi"))
        self.theme.setItemText(9, _translate("Dialog", "Mor"))
        self.save_quit.setText(_translate("Dialog", "Kaydet ve çık"))