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

    def replies(self):
        from models.reply import Reply
        rs = Reply.find_all(topic_id=self.id)
        return rs