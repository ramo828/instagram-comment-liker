from PyQt6.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
from time import sleep
from instagrapi.exceptions import UnknownError, ClientError, ChallengeUnknownStep,ChallengeRequired, RateLimitError, LoginRequired
from controller.instagram import Instagram

class Extension(QObject):
    terminal = Signal(str,str)
    image = Signal(str)
    commentList = Signal(str)
    clear = Signal()
    status = Signal(bool)
    instagram = Instagram()

    def get_comments(self,
                     link:str, 
                     limit:int, 
                     user:str, 
                     set_limit:bool,
                     set_accept:bool, 
                     manual:bool,
                     userName:str,
                     userPass:str):
        print(link,limit,user,set_limit,set_accept,manual, userName, userPass)
        try:
            self.status.emit(False)
            if(not link):
                self.terminal.emit("Post linki bos buraxildi\n",'red')
                print(1)
            elif(not link.startswith('https://')):
                print(2)
                self.terminal.emit("Post linki dogru yazilmadi\n",'red')
            else:
                self.terminal.emit("Her sey qaydasindadir\n",'blue')
                self.clear.emit()
                self.instagram.set_account(userName, userPass)
                media = self.instagram.get_media(link)
                # Medialari al
                if(set_limit):
                    comments = self.instagram.get_comments(media, limit)
                else:
                    comments = self.instagram.get_comments(media, 1000000)
                length_comments = len(comments)
                # Comment uzunlugu
                self.terminal.emit(f'{length_comments} tane yorum bulundu\n',"blue")
                for comment in range(length_comments):
                    if(comments[comment].user.username == user):
                        if(set_accept):
                            if(not '@' in comments[comment].text):
                                self.image.emit(comments[comment].user.profile_pic_url)
                                self.commentList.emit(comments[comment].text)
                        else:
                                self.image.emit(comments[comment].user.profile_pic_url)
                                self.commentList.emit(comments[comment].text)
                    elif(manual):
                        if(set_accept):
                            if(not '@' in comments[comment].text):
                                self.commentList.emit(comments[comment].text)

                        else:
                            self.commentList.emit(comments[comment].text)
                self.status.emit(True)




                        
                # self.comment_pk = self.instagram.get_comment_pk(comments[commentIndex])
                # print(comment_pk)
                # ins.like_comment(comment_pk)
        except (ChallengeUnknownStep,ChallengeRequired) as e:
            print(e)
            # self.terminal.emit("Hesap dogrulamaya dustu\n",'red')
        except LoginRequired as e:
            print(e)
            self.terminal.emit("Hesapdan cikis yapilmis\n",'red')





