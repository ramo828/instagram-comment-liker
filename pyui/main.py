# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CommentLikerPanel(object):
    def setupUi(self, CommentLikerPanel):
        CommentLikerPanel.setObjectName("CommentLikerPanel")
        CommentLikerPanel.resize(731, 356)
        self.centralwidget = QtWidgets.QWidget(parent=CommentLikerPanel)
        self.centralwidget.setObjectName("centralwidget")
        self.commentBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.commentBox.setGeometry(QtCore.QRect(320, 10, 391, 261))
        self.commentBox.setObjectName("commentBox")
        self.commentsList = QtWidgets.QComboBox(parent=self.commentBox)
        self.commentsList.setEnabled(True)
        self.commentsList.setGeometry(QtCore.QRect(10, 80, 321, 41))
        self.commentsList.setEditable(False)
        self.commentsList.setIconSize(QtCore.QSize(32, 32))
        self.commentsList.setModelColumn(0)
        self.commentsList.setObjectName("commentsList")
        self.label = QtWidgets.QLabel(parent=self.commentBox)
        self.label.setGeometry(QtCore.QRect(10, 140, 171, 17))
        self.label.setObjectName("label")
        self.user = QtWidgets.QLineEdit(parent=self.commentBox)
        self.user.setEnabled(False)
        self.user.setGeometry(QtCore.QRect(208, 135, 121, 25))
        self.user.setObjectName("user")
        self.limit = QtWidgets.QSpinBox(parent=self.commentBox)
        self.limit.setEnabled(False)
        self.limit.setGeometry(QtCore.QRect(248, 171, 81, 26))
        self.limit.setMaximum(10000000)
        self.limit.setProperty("value", 1000)
        self.limit.setObjectName("limit")
        self.manual = QtWidgets.QRadioButton(parent=self.commentBox)
        self.manual.setGeometry(QtCore.QRect(10, 26, 251, 23))
        self.manual.setObjectName("manual")
        self.manual_text = QtWidgets.QRadioButton(parent=self.commentBox)
        self.manual_text.setGeometry(QtCore.QRect(10, 50, 251, 23))
        self.manual_text.setObjectName("manual_text")
        self.profile_image = QtWidgets.QLabel(parent=self.commentBox)
        self.profile_image.setGeometry(QtCore.QRect(340, 137, 41, 21))
        self.profile_image.setStyleSheet("border-radius: 8px;")
        self.profile_image.setText("")
        self.profile_image.setObjectName("profile_image")
        self.set_limit = QtWidgets.QCheckBox(parent=self.commentBox)
        self.set_limit.setGeometry(QtCore.QRect(10, 172, 171, 23))
        self.set_limit.setObjectName("set_limit")
        self.set_accept = QtWidgets.QCheckBox(parent=self.commentBox)
        self.set_accept.setGeometry(QtCore.QRect(10, 210, 161, 23))
        self.set_accept.setObjectName("set_accept")
        self.status_label = QtWidgets.QLabel(parent=self.commentBox)
        self.status_label.setGeometry(QtCore.QRect(340, 85, 31, 31))
        self.status_label.setStyleSheet("background-color: rgb(190, 190, 190);\n"
"border-radius: 15px;")
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.getComments = QtWidgets.QPushButton(parent=self.centralwidget)
        self.getComments.setGeometry(QtCore.QRect(560, 280, 151, 25))
        self.getComments.setObjectName("getComments")
        self.comment = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.comment.setGeometry(QtCore.QRect(9, 10, 301, 261))
        self.comment.setObjectName("comment")
        self.postLink = QtWidgets.QLineEdit(parent=self.comment)
        self.postLink.setGeometry(QtCore.QRect(10, 31, 288, 31))
        self.postLink.setObjectName("postLink")
        self.terminal = QtWidgets.QPlainTextEdit(parent=self.comment)
        self.terminal.setEnabled(True)
        self.terminal.setGeometry(QtCore.QRect(10, 80, 288, 171))
        self.terminal.setReadOnly(True)
        self.terminal.setObjectName("terminal")
        self.startLike = QtWidgets.QPushButton(parent=self.centralwidget)
        self.startLike.setGeometry(QtCore.QRect(10, 280, 151, 25))
        self.startLike.setObjectName("startLike")
        CommentLikerPanel.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=CommentLikerPanel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 22))
        self.menubar.setObjectName("menubar")
        CommentLikerPanel.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=CommentLikerPanel)
        self.statusbar.setObjectName("statusbar")
        CommentLikerPanel.setStatusBar(self.statusbar)

        self.retranslateUi(CommentLikerPanel)
        QtCore.QMetaObject.connectSlotsByName(CommentLikerPanel)

    def retranslateUi(self, CommentLikerPanel):
        _translate = QtCore.QCoreApplication.translate
        CommentLikerPanel.setWindowTitle(_translate("CommentLikerPanel", "Comment Liker Panel"))
        self.commentBox.setTitle(_translate("CommentLikerPanel", "Comments"))
        self.label.setText(_translate("CommentLikerPanel", "Kullanıcı adına göre ara: "))
        self.user.setPlaceholderText(_translate("CommentLikerPanel", "Kullanıcı adı"))
        self.manual.setText(_translate("CommentLikerPanel", "Manuel yorum arama"))
        self.manual_text.setText(_translate("CommentLikerPanel", "Kullanıcı adını yazarak arama"))
        self.set_limit.setText(_translate("CommentLikerPanel", "Yüklenecek yorum sayısı"))
        self.set_accept.setText(_translate("CommentLikerPanel", "Yanıtları gizle"))
        self.getComments.setText(_translate("CommentLikerPanel", "Commentleri Yükle"))
        self.comment.setTitle(_translate("CommentLikerPanel", "Comment link"))
        self.postLink.setPlaceholderText(_translate("CommentLikerPanel", "https://"))
        self.startLike.setText(_translate("CommentLikerPanel", "Başlat"))
