import time

from models.mongomodel import MongoBase


class Message(MongoBase):
    """
    私信类
    """
    def __init__(self, form):
        self.id = form.get('id', None)
        self.title = form.get('title', '')
        self.content = form.get('content', '')

        self.ct = int(time.time())
        self.read = False

        self.sender_id = -1
        self.receiver_id = int(form.get('to', -1))

    def set_sender(self, sender_id):
        self.sender_id = sender_id
        self.save()

    def mark_read(self):
        self.read = True
        self.save()

    def user(self):
        from models.user import User
        u = User.get(self.sender_id)
        return u


# import time
#
# from models import Model
#
#
# class Message(Model):
#     """
#     私信类
#     """
#     def __init__(self, form):
#         self.id = form.get('id', None)
#         self.title = form.get('title', '')
#         self.content = form.get('content', '')
#
#         self.ct = int(time.time())
#         self.read = False
#
#         self.sender_id = -1
#         self.receiver_id = int(form.get('to', -1))
#
#     def set_sender(self, sender_id):
#         self.sender_id = sender_id
#         self.save()
#
#     def mark_read(self):
#         self.read = True
#         self.save()
#
#     def user(self):
#         from models.user import User
#         u = User.get(self.sender_id)
#         return u