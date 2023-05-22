from pyui.main import Ui_CommentLikerPanel
from PyQt6.QtGui import QTextCharFormat, QColor, QTextCursor, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QDialog, QWidget, QLabel, QVBoxLayout,QFileDialog
from PyQt6 import QtCore, QtGui, QtWidgets
from random import randint
import urllib.request
from controller.extension import Extension
from controller.database import Database
from pyui.settings import Ui_Dialog as Settings
from pyui.loginUI import Ui_MainWindow as loginInterface
from pyui.main import Ui_CommentLikerPanel as Pencere
from controller.app_controls import Setting_controls
import sys
import threading as td


class loginUI(QMainWindow, loginInterface):
    def __init__(self):
        super().__init__()
        self.default_login = ''
        self.default_pass = ''
        self.style1 = [
            "themes/default.qss",
            "themes/besiktas.qss",
            "themes/galatasaray.qss",
            "themes/fenerbahce.qss",
            "themes/trabzonspor.qss",
            "themes/black.qss",
            "themes/light_blue.qss",
            "themes/yellow.qss",
            "themes/red.qss",
            "themes/purple.qss"]
        self.setupUi(self)
        self.db = Database()
        self.settingUI = Settings()
        self.set = Setting_controls()
        self.logIn.clicked.connect(self.control)
        self.password.returnPressed.connect(self.control)
        self.passShow.clicked.connect(self.passEcho)
        theme = self.loadTheme()
        self.setStyleSheet(theme)
        

    def settUI(self):
        dialog = QDialog(self)
        theme = self.loadTheme()
        self.settingUI = Settings()
        self.settingUI.setupUi(dialog, theme)
        self.settingUI.pshow.clicked.connect(self.showPassword)
        self.settingUI.fileChoiser.pressed.connect(self.setFile)
        self.settingUI.pass_try.textChanged.connect(self.controlPassword)
        self.settingUI.save_quit.clicked.connect(self.save_and_quit)
        self.settingUI.theme.currentIndexChanged.connect(self.getTheme)
        self.settingUI.user.setText(self.db.load_data(0))
        self.settingUI.fileName.setText(self.db.load_data(2))
        self.settingUI.sep.setText(self.db.load_data(3))
        dialog.exec()

    def loadTheme(self):
        theme = ''
        index = self.db.load_data(5)
        with open(self.style1[index]) as qss:
            theme = qss.read()
        return theme
    
    def setFile(self):
        dosya_yolu, _ = QFileDialog.getOpenFileName(None, "Dosya Seç", "", "Tüm Dosyalar (*);;Metin Dosyaları (*.txt)")

        if dosya_yolu:
            print("Seçilen dosya yolu:", dosya_yolu)
            self.settingUI.fileName.setText(dosya_yolu)
        else:
            print("Dosya seçilmedi.")

    def controlPassword(self):
        ps1 = self.settingUI.pass2.text()
        ps2 = self.settingUI.pass_try.text()
        if(ps1 == ps2):
            self.settingUI.pass2.setStyleSheet('color: black;')
            self.settingUI.pass_try.setStyleSheet('color: black;')
        else:
            self.settingUI.pass_try.setStyleSheet('color: red;')
            self.settingUI.pass2.setStyleSheet('color: red;')


    def about(self):
        h = 300
        w = 120
        theme = self.loadTheme()
        dialog = QDialog(self)
        dialog.setWindowTitle("Hakkında")
        dialog.setModal(True)
        dialog.resize(h, w)
        dialog.setStyleSheet(theme)
        # Label oluşturun
        label = QLabel("""
        Bu program özel olarak RamoSoft'a yapılmışdır ve tüm hakları saklıdır.
            iletisim Bilgileri
        email: illegalism666@gmail.com
        whatsapp: +994558302766
        """, dialog)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: red;")
        label.move(int(h/2), int(w/2))
        # Düzen oluşturun ve label'i ekleyin
        layout = QVBoxLayout(dialog)
        layout.addWidget(label)
        dialog.setLayout(layout)
        dialog.exec()

    def save_and_quit(self):
        password = ""
        old_password = self.db.load_data(1)
        # kohne sifreni vb'dan al
        ps = self.settingUI.pass1.text()
        ps1 = self.settingUI.pass2.text()
        ps2 = self.settingUI.pass_try.text()
        fileName = self.settingUI.fileName.text()
        sep = self.settingUI.sep.text()
        if(not ps1):
            ps = old_password
        
        if(old_password == ps):
        # eger kohne sifre uygundursa sertleri yerine yetir
            self.settingUI.pass1.setStyleSheet('color: black;')
        # sifre dogrudursa input rengini qoru
            if(ps1 == ps2):
        # sifre tekrari eynidirse serti yerine yetir
                password = ps1
                index = self.settingUI.theme.currentIndex()
                self.db.save_data_index(5,index)
                user = self.settingUI.user.text()
                self.set.checkSettingData(
                                        user, 
                                        password,
                                        fileName,
                                        sep
                                        )
                exit()

            else:
                password = ''
        else:
            self.settingUI.pass1.setStyleSheet('color: red;')
            # sifre kohne sifre ile uygun deyilse input'u qirmizi renge boya
            print(ps, old_password)


        # eger hec bir sey daxil edilmeyibse sifreleri eynilesdir ve seti yerine yetir

    def showPassword(self):
        ps = self.settingUI.pshow.isChecked()
        if(ps):
            self.settingUI.pass1.setEchoMode(QLineEdit.EchoMode.Normal)
            self.settingUI.pass2.setEchoMode(QLineEdit.EchoMode.Normal)
            self.settingUI.pass_try.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.settingUI.pass1.setEchoMode(QLineEdit.EchoMode.Password)
            self.settingUI.pass2.setEchoMode(QLineEdit.EchoMode.Password)
            self.settingUI.pass_try.setEchoMode(QLineEdit.EchoMode.Password)
       

    def getTheme(self):
        index = self.settingUI.theme.currentIndex()
        with open(self.style1[index]) as qss:
            self.setStyleSheet(qss.read())
            print(qss.read())
            print(self.style1[index])

    def passEcho(self):
        ctrl = self.passShow.isChecked()
        if(ctrl):
            self.password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:    
            self.password.setEchoMode(QLineEdit.EchoMode.Password)
        

    def control(self):
        _login = self.login.text()
        _password = self.password.text()
       
        if(_login == self.db.load_data(0) and _password == self.db.load_data(1)):
            self.home()
        else:
            self.status.setText("Kullanıcı adı ve ya şifre yanlış")

    def home(self):
        self.homeUI = Pencere()
        self.ext = Extension()
        theme = self.loadTheme()
        self.homeUI.setupUi(self, theme)
        self.data = object
        udata = self.db.load_data(2)
        if(udata):
            data = open(udata,"r").read()
            self.homeUI.like_count.setValue(len(data.splitlines())+1)
        self.homeUI.getComments.clicked.connect(self.download_comments)
        self.homeUI.manual.clicked.connect(self.comment_choise)
        self.homeUI.set_limit.clicked.connect(self.limit_control)
        self.homeUI.manual_text.clicked.connect(self.comment_choise)
        self.homeUI.manual.setChecked(True)
        self.ext.terminal.connect(self.add_colored_text)
        self.ext.image.connect(self.setPixmap)
        self.ext.commentList.connect(self.commentAddItem)
        self.ext.clear.connect(self.commentListClear)
        self.ext.status.connect(self.statusLabel)
        self.ext.statusLike.connect(self.statusLabel2)
        self.ext.data.connect(self.sepCommand)
        self.ext.pk.connect(self.setCommandPk)
        self.ext.counter_signal.connect(self.setCounter)
        self.homeUI.postLink.returnPressed.connect(self.link_controller)
        self.homeUI.startLike.clicked.connect(self.runLiker)
        self.homeUI.commentsList.currentIndexChanged.connect(self.commentListController)
        self.homeUI.action_k.triggered.connect(self.quit)
        self.homeUI.actionAyarlar.triggered.connect(self.settUI)
        self.homeUI.actionHakk_nda.triggered.connect(self.about)



    def setCounter(self, ch, count):
        if(ch == 0):
            self.homeUI.label_6.setText(str(count))
        elif(ch == 1):
            self.homeUI.label_5.setText(str(count))


    def commentListController(self):
        index = self.homeUI.commentsList.currentIndex()
        print(self.ext.get_pk_from_index(index))
        self.setCommandPk(self.ext.get_pk_from_index(index))

    def setCommandPk(self, pk):
        self.pk = pk        

    def quit(self):
        exit(1)

    def runLiker(self):
        fileName = self.db.load_data(2)
        sep = self.db.load_data(3)
        print(fileName, sep)
        args=(
        self.pk,
        int(self.homeUI.like_count.text()),
        fileName,
        sep
        )
        self.thread2 = td.Thread(target=self.ext.run_command_liker, daemon=True, args=args)
        self.thread2.start()

    def link_controller(self):
        link = self.homeUI.postLink.text()
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
            self.homeUI.commentsList.setDisabled(True)
            self.homeUI.getComments.setDisabled(True)
            self.homeUI.manual.setDisabled(True)
            self.homeUI.set_limit.setDisabled(True)
            self.homeUI.manual_text.setDisabled(True)
            self.homeUI.set_accept.setDisabled(True)
        else:
            self.homeUI.commentsList.setEnabled(True)
            self.homeUI.getComments.setEnabled(True)
            self.homeUI.manual.setEnabled(True)
            self.homeUI.set_limit.setEnabled(True)
            self.homeUI.manual_text.setEnabled(True)
            self.homeUI.set_accept.setEnabled(True)


    def download_comments(self):
        link = self.homeUI.postLink.text()
        limitCheck = self.homeUI.set_limit.isChecked()
        limit = int(self.homeUI.limit.text())
        user = self.homeUI.user.text()
        acceptCheck = self.homeUI.set_accept.isChecked()
        manualCheck = self.homeUI.manual.isChecked()
        # kullanici ve sifre
        duser = ''
        dpass = ''
        fileName = self.db.load_data(2)
        if(fileName):
            data = open(fileName,"r").read().splitlines()
            length = len(data)
            randomUser = randint(0, length)
            duser = str(data[randomUser].split(":")[0])
            dpass = str(data[randomUser].split(":")[1])

        args=(
            link,
            limit,
            user,
            limitCheck,
            acceptCheck,
            manualCheck,
            duser,
            dpass)
        self.thread1 = td.Thread(target=self.ext.get_comments, daemon=True, args=args)
        self.thread1.start()
       
    def sepCommand(self, data):
        self.data = data
    
    def setPixmap(self, url):
        self.homeUI.profile_image.setPixmap(self.set_profile_pic(url))

    def statusLabel(self, status:bool):
        if(status):
            self.homeUI.status_label.setStyleSheet("""
            background-color: green;
            border-radius: 15px;
            """)
            self.homeUI.startLike.setEnabled(True)
            self.homeUI.like_count.setEnabled(True)
        else:
            self.homeUI.status_label.setStyleSheet("""
            background-color: red;
            border-radius: 15px;
            """)
            self.homeUI.startLike.setDisabled(True)
            self.homeUI.like_count.setDisabled(True)

    def statusLabel2(self, status:bool):
        if(status):
                self.homeUI.status_label2.setStyleSheet("""
                background-color: red;
                border-radius: 5px;
                """)
        else:
                self.homeUI.status_label2.setStyleSheet("""
                background-color: green;
                border-radius: 5px;
                """)
                



    def set_profile_pic(self, url):
        # Resmi indirin ve QPixmap nesnesine yükleyin
        data = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        # Resmi ölçeklendirin
        scaled_pixmap = pixmap.scaled(31, 17)
        return scaled_pixmap

    def limit_control(self):
        if(self.homeUI.set_limit.isChecked()):
            self.homeUI.limit.setEnabled(True)
        else:
            self.homeUI.limit.setEnabled(False)

    def comment_choise(self):
        if(self.homeUI.manual.isChecked()):
            self.homeUI.commentsList.setEnabled(True)
            self.homeUI.user.setEnabled(False)
        else:
            self.homeUI.commentsList.setEnabled(True)
            self.homeUI.user.setEnabled(True)

    def add_colored_text(self, text, color):
        # Yazı rengini ayarlamak için QTextCharFormat sınıfını kullanıyoruz
        char_format = QTextCharFormat()
        char_format.setForeground(QColor(color))
        # QTextCursor sınıfını kullanarak yazıyı seçiyoruz
        cursor = self.homeUI.terminal.textCursor()
        cursor1 = QTextCursor(self.homeUI.terminal.textCursor())
        cursor1.movePosition(cursor1.MoveOperation.Down)
        self.homeUI.terminal.setTextCursor(cursor1)
        cursor.movePosition(QTextCursor.MoveOperation.End)
        cursor.insertText(text)
        # Seçili yazının rengini ayarlıyoruz
        cursor.setPosition(cursor.position() - len(text))
        cursor.movePosition(QTextCursor.MoveOperation.Right, QTextCursor.MoveMode.KeepAnchor, len(text))
        cursor.setCharFormat(char_format)
   

    def commentAddItem(self, item):
        self.homeUI.commentsList.addItem(item)
    def commentListClear(self):
        self.homeUI.commentsList.clear()
    

app = QApplication(sys.argv)
login_face = loginUI()
login_face.show()
sys.exit(app.exec())
