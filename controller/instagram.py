from instagrapi import Client


class Instagram:
    def __init__(self):
        self.cl = Client()

    def init_instagram(self):
        self.cl = Client()

    def set_account(self, user, password):
        self.cl.login(user, password)

    def get_media(self, url):
        media = self.cl.media_pk_from_url(url)
        return media


    def get_comment_pk(self, comments):
        return comments.pk

    def get_comments(self, media, limit = 100):
        comments = self.cl.media_comments(media,amount=limit)
        
        return comments
    def get_comments_ch(self, media, limit = 100):
        comments = self.cl.media_comments_chunk(media, limit)
        
        return comments
    
    def like_comment(self, comment_pk):
        if(self.cl.comment_like(int(comment_pk))):
            return True
        else:
            return False
    



