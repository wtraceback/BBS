import time

from models import Model


class Reply(Model):
    """
    评论类
    """
    def __init__(self, form):
        self.id = form.get('id', None)
        self.content = form.get('content', '')
        self.ct = int(time.time())
        self.ut = self.ct
        self.topic_id = int(form.get('topic_id', -1))

    def user(self):
        from models.user import User
        # 这边使用了隐式添加 user_id ，在添加评论的时候，直接将评论的 user_id 添加到了数据库中
        u = User.get(self.user_id)
        return u