import time

from models.mongomodel import MongoBase


class Board(MongoBase):
    """
    板块类
    """
    def __init__(self, form):
        self.id = form.get('id', None)
        self.name = form.get('name', '')
        self.ct = int(time.time())
        self.ut = self.ct

    def str_id(self):
        return str(self.id)


# import time
#
# from models import Model
#
#
# class Board(Model):
#     """
#     板块类
#     """
#     def __init__(self, form):
#         self.id = form.get('id', None)
#         self.name = form.get('name', '')
#         self.ct = int(time.time())
#         self.ut = self.ct
#
#     def str_id(self):
#         return str(self.id)