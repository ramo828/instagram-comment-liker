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
    data = Signal(object)
    pk = Signal(str)
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
                    self.data_comments = comments
                else:
                    comments = self.instagram.get_comments(media, 1000000)
                    self.data_comments = comments
                length_comments = len(comments)
                # Comment uzunlugu
                self.terminal.emit(f'{length_comments} tane yorum bulundu\n',"blue")
                for comment in range(length_comments):
                    if(comments[comment].user.username == user):
                        if(set_accept):
                            if(not '@' in comments[comment].text):
                                self.image.emit(comments[comment].user.profile_pic_url)
                                self.commentList.emit(comments[comment].text)
                                self.data.emit(comments[comment])
                                self.pk.emit(comments[comment].pk)

                        else:
                                self.image.emit(comments[comment].user.profile_pic_url)
                                self.commentList.emit(comments[comment].text)
                                self.data.emit(comments[comment])
                                self.pk.emit(comments[comment].pk)

                    elif(manual):
                        if(set_accept):
                            if(not '@' in comments[comment].text):
                                self.commentList.emit(comments[comment].text)


                        else:
                            self.commentList.emit(comments[comment].text)

                self.status.emit(True)

        except (ChallengeUnknownStep,ChallengeRequired) as e:
            print(e)
            self.terminal.emit("\nHesap dogrulamaya dustu",'red')
        except LoginRequired as e:
            print(e)
            self.terminal.emit("\nHesapdan cikis yapilmis",'red')
        except UnknownError as e:
            print(e)
            self.terminal.emit("\nHesap bilgileri doğru yazılmamış",'red')


    def get_pk_from_index(self, index = 0):
        return self.data_comments[index].pk


    def get_comment_pk_from_url(self, link:str):
        link = link.replace("https://www.instagram.com/p/","")
        begin = link.find("/c/")
        end = link.rindex("/")
        return link[begin+3:end]
    
    def run_command_liker(self, pk, limit):
        file = open("accounts.txt","r")
        userlist = file.read().splitlines()
        counter = 0
        for user in userlist:
            try:
                if(counter == limit):
                    self.terminal.emit(f"\nBeğenme sona erdi", "green")
                    break
                like_ins = Instagram()
                user = user.split(":")
                userName = user[0]
                userPass = user[1]
                print(userName, userPass)
                like_ins.set_account(userName,userPass)
                status = like_ins.like_comment(int(pk))
                if(status):
                    self.terminal.emit(f"\n{userName} Begendi",'green')
                else:
                    print("Begenmedi\n")
                    self.terminal.emit(f"\n{userName} Begenmedi",'red')
                counter+=1
            except Exception as e:
                self.terminal.emit(f"\nXeta bas verdi: {e}", "red")




