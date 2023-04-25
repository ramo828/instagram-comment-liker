from ..controller.instagram import Instagram

def test():
        ins = Instagram()
        user = 'elda.r2372'
        password = 'ramiz123'
        url = 'https://www.instagram.com/p/CrIk5JTqLQ5/'
        # user = 'illegalism666'
        # password = 'Ramizz...1994hack'
        ins.set_account(user, password)
        media = ins.get_media(url)
        comments = ins.get_comments(media)
        comment_pk = ins.get_comment_pk(comments)
        ins.like_comment(comment_pk)

test()