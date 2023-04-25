from controller.instagram import Instagram
from pyui.main import Ui_CommentLikerPanel
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QTextCharFormat, QColor, QTextCursor
import sys

class Pencere(QMainWindow, Ui_CommentLikerPanel):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.getComments.clicked.connect(self.get_comments)
        self.startLike.clicked.connect(self.start)
        self.instagram = Instagram()
        self.kullanicilar = {
            "elda.r2372": "ramiz123",
            "illegalism666": "Ramizz...1994hack"
        }


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

    def get_comments(self):
        if(not self.postLink.text()):
            self.add_colored_text("Post linki bos buraxildi\n",'red')
        elif(not self.postLink.text().startswith('https://')):
            self.add_colored_text("Post linki dogru yazilmadi\n",'red')
        else:
            self.commentsList.setEnabled(True)
            self.add_colored_text("Ger sey qaydasindadir\n",'blue')
            self.get_comment_list()

    def get_comment_list(self):
        self.commentsList.clear()
        self.instagram.set_account('illegalism666', self.kullanicilar['illegalism666'])
        media = self.instagram.get_media(self.postLink.text())
        comments = self.instagram.get_comments(media)
        for comment in range(len(comments)):
            self.commentsList.addItem(comments[comment].text)
        
        # print(comments[0].text)
        self.comment_pk = self.instagram.get_comment_pk(comments[self.commentsList.currentIndex()])
        # print(comment_pk)
        # ins.like_comment(comment_pk)
        
        
    def start(self):
        print(self.comment_pk)
       

app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
sys.exit(app.exec())