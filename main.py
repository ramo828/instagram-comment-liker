from pyui.main import Ui_CommentLikerPanel
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QTextCharFormat, QColor, QTextCursor, QPixmap
from PyQt6 import QtCore, QtGui, QtWidgets
import urllib.request
from controller.extension import Extension
import sys
import threading as td


class Pencere(QMainWindow, Ui_CommentLikerPanel):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = object
        self.getComments.clicked.connect(self.download_comments)
        self.manual.clicked.connect(self.comment_choise)
        self.set_limit.clicked.connect(self.limit_control)
        self.manual_text.clicked.connect(self.comment_choise)
        self.manual.setChecked(True)
        self.ext = Extension()
        self.ext.terminal.connect(self.add_colored_text)
        self.ext.image.connect(self.setPixmap)
        self.ext.commentList.connect(self.commentAddItem)
        self.ext.clear.connect(self.commentListClear)
        self.ext.status.connect(self.statusLabel)
        self.ext.data.connect(self.sepCommand)
        self.ext.pk.connect(self.setCommandPk)
        self.postLink.returnPressed.connect(self.link_controller)
        self.startLike.clicked.connect(self.runLiker)
        self.commentsList.currentIndexChanged.connect(self.commentListController)

    def commentListController(self):
        index = self.commentsList.currentIndex()
        print(self.ext.get_pk_from_index(index))
        self.setCommandPk(self.ext.get_pk_from_index(index))

    def setCommandPk(self, pk):
        self.pk = pk        

    def runLiker(self):
        print(self.pk)
        args=(self.pk,
        int(self.like_count.text()))
        self.thread2 = td.Thread(target=self.ext.run_command_liker, daemon=True, args=args)
        self.thread2.start()

    def link_controller(self):
        link = self.postLink.text()
        if(link.find("/c/") != -1):
            print("pk link")
            self.statusLabel(True)
            self.add_colored_text(f"\nYorum seçildi: {self.ext.get_comment_pk_from_url(link)}\n","lightgreen")
            self.setCommandPk(self.ext.get_comment_pk_from_url(link))
            self.objectsStatus(True)
        else:
            self.statusLabel(False)
            self.objectsStatus(False)

    def objectsStatus(self, status:bool):
        if(status):
            self.commentsList.setDisabled(True)
            self.getComments.setDisabled(True)
            self.manual.setDisabled(True)
            self.set_limit.setDisabled(True)
            self.manual_text.setDisabled(True)
            self.set_accept.setDisabled(True)
        else:
            self.commentsList.setEnabled(True)
            self.getComments.setEnabled(True)
            self.manual.setEnabled(True)
            self.set_limit.setEnabled(True)
            self.manual_text.setEnabled(True)
            self.set_accept.setEnabled(True)


    def download_comments(self):
        link = self.postLink.text()
        limitCheck = self.set_limit.isChecked()
        limit = int(self.limit.text())
        user = self.user.text()
        acceptCheck = self.set_accept.isChecked()
        manualCheck = self.manual.isChecked()
        # kullanici ve sifre
        userName = ''
        userPass = ''

        args=(
            link,
            limit,
            user,
            limitCheck,
            acceptCheck,
            manualCheck,
            userName,
            userPass)
        self.thread1 = td.Thread(target=self.ext.get_comments, daemon=True, args=args)
        self.thread1.start()
       
    def sepCommand(self, data):
        self.data = data
    
    def setPixmap(self, url):
        self.profile_image.setPixmap(self.set_profile_pic(url))

    def statusLabel(self, status:bool):
        if(status):
            self.status_label.setStyleSheet("""
            background-color: lightgreen;
            border-radius: 15px;
            """)
            self.startLike.setEnabled(True)
            self.like_count.setEnabled(True)
        else:
            self.status_label.setStyleSheet("""
            background-color: magenta;
            border-radius: 15px;
            """)
            self.startLike.setDisabled(True)
            self.like_count.setDisabled(True)




    def set_profile_pic(self, url):
        # Resmi indirin ve QPixmap nesnesine yükleyin
        data = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        # Resmi ölçeklendirin
        scaled_pixmap = pixmap.scaled(31, 17)
        return scaled_pixmap

    def limit_control(self):
        if(self.set_limit.isChecked()):
            self.limit.setEnabled(True)
        else:
            self.limit.setEnabled(False)

    def comment_choise(self):
        if(self.manual.isChecked()):
            self.commentsList.setEnabled(True)
            self.user.setEnabled(False)
        else:
            self.commentsList.setEnabled(True)
            self.user.setEnabled(True)

    def add_colored_text(self, text, color):
        # Yazı rengini ayarlamak için QTextCharFormat sınıfını kullanıyoruz
        char_format = QTextCharFormat()
        char_format.setForeground(QColor(color))
        # QTextCursor sınıfını kullanarak yazıyı seçiyoruz
        cursor = self.terminal.textCursor()
        cursor1 = QTextCursor(self.terminal.textCursor())
        cursor1.movePosition(cursor1.MoveOperation.Down)
        self.terminal.setTextCursor(cursor1)
        cursor.movePosition(QTextCursor.MoveOperation.End)
        cursor.insertText(text)
        # Seçili yazının rengini ayarlıyoruz
        cursor.setPosition(cursor.position() - len(text))
        cursor.movePosition(QTextCursor.MoveOperation.Right, QTextCursor.MoveMode.KeepAnchor, len(text))
        cursor.setCharFormat(char_format)
   

    def commentAddItem(self, item):
        self.commentsList.addItem(item)
    def commentListClear(self):
        self.commentsList.clear()
    

app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
sys.exit(app.exec())
