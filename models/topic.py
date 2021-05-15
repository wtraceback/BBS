import time

from models import Model


class Topic(Model):
    """
    话题类
    """
    def __init__(self, form):
        self.id = form.get('id', None)
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.ct = int(time.time())
        self.ut = self.ct
        self.user_id = form.get('user_id', '')
        self.board_id = int(form.get('board_id', -1))
        self.views = 0

    def replies(self):
        from models.reply import Reply
        rs = Reply.find_all(topic_id=self.id)
        return rs

    def board(self):
        from models.board import Board
        bs = Board.find_by(id=self.board_id)
        return bs

    def user(self):
        from models.user import User
        us = User.find_by(id=self.user_id)
        return us

    @classmethod
    def get(cls, id):
        m = cls.find_by(id=id)
        m.views += 1
        m.save()
        return m