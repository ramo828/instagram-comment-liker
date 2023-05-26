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
    counter_signal = Signal(int)
    statusLike = Signal(bool)
    instagram = Instagram()
    liker_status = False

    def stopLiker(self, status:bool):
        self.liker_status = status
        print(status)

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
        except Exception as e:
            print(e)
            self.terminal.emit(f"\n{e}",'red')


    def get_pk_from_index(self, index = 0):
        return self.data_comments[index].pk


    def get_comment_pk_from_url(self, link:str):
        link = link.replace("https://www.instagram.com/p/","")
        begin = link.find("/c/")
        end = link.rindex("/")
        return link[begin+3:end]
    
    def run_command_liker(self, pk, limit, filename="accounts.txt", sep=':'):
        try:
            self.file = open(filename, "r")
            self.userlist = self.file.read().splitlines()
        except FileNotFoundError:
            self.terminal.emit(f"\nHata oluşdu: Kullanıcı adı ve şifrelerin kayıtlıolduğu dosya seçilmedi", "red")

        counter = 0
        self.statusLike.emit(False)
        for user in self.userlist:
            if(self.liker_status):
                print("stop ok")
                self.terminal.emit(f"\nBeğenme durduruldu", "green")
                break
            try:
                if counter == limit:
                    self.terminal.emit(f"\nBeğenme sona erdi", "green")
                    break
                elif len(self.userlist) == counter:
                    break
                like_ins = Instagram()
                user = user.split(sep)
                self.userName = user[0]
                self.userPass = user[1]
                like_ins.set_account(self.userName, self.userPass)
                status = like_ins.like_comment(int(pk))
                if(self.liker_status):
                    self.terminal.emit(f"\nBeğenme durduruldu", "green")
                    break
                if status:
                    self.terminal.emit(f"\n{self.userName} Begendi", 'green')
                else:
                    self.terminal.emit(f"\n{self.userName} Begenmedi", 'red')
                counter += 1
                if(self.liker_status):
                    self.terminal.emit("\nBeğenme durduruldu", "green")
                    break
            except (ChallengeUnknownStep, ChallengeRequired) as e:
                print(e)
                self.terminal.emit(f"Hesap doğrulama hatası: {user} \n Kullanıcı: {self.userName}","red")
                self.counter_signal.emit(0)  # err_count sayacını diğer kodlara ilet
                continue
            except UnknownError as e:
                self.terminal.emit(f"\nHata oluşdu: {e}\n Kullanıcı: {self.userName}", "red")
                self.counter_signal.emit(0)  # err_count sayacını diğer kodlara ilet
                continue
            except Exception as e:
                self.terminal.emit(f"\nHata oluşdu: {e}\n Kullanıcı: {self.userName}", "red")
                self.counter_signal.emit(0)  # err_count sayacını diğer kodlara ilet
                continue
            else:
                self.counter_signal.emit(1)  # success_count sayacını diğer kodlara ilet
            if(self.liker_status):
                self.terminal.emit(f"\nBeğenme durduruldu", "green")
                break
        self.statusLike.emit(True)







