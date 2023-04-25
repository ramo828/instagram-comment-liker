from controller.instagram import Instagram
from pyui.main import Ui_CommentLikerPanel
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QTextCharFormat, QColor, QTextCursor
import sys

class Pencere(QMainWindow, Ui_CommentLikerPanel):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.getComments.clicked.connect(self.radio_button_ekle)
        self.counter = 0

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

    def radio_button_ekle(self):
        if(not self.postLink.text()):
            self.add_colored_text("Post linki bos buraxildi\n",'red')
        elif(not self.postLink.text().startswith('https://')):
            self.add_colored_text("Post linki dogru yazilmadi\n",'red')
        else:
            self.commentsList.setEnabled(True)
            self.add_colored_text("Ger sey qaydasindadir\n",'blue')


        # ins = Instagram()
        # user = 'elda.r2372'
        # password = 'ramiz123'
        # url = 'https://www.instagram.com/p/CrIk5JTqLQ5/'
        # ins.set_account(user, password)
        # media = ins.get_media(url)
        # comments = ins.get_comments(media)
        # for comment in range(len(comments)):
        #     self.commentsList.addItem(comments[comment].text)
                # Model oluşturma
        
        # print(comments[0].text)
        # comment_pk = ins.get_comment_pk(comments[0])
        # print(comment_pk)
        # ins.like_comment(comment_pk)
        
        
    def start(self):
        print("OK")
       

app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
sys.exit(app.exec())