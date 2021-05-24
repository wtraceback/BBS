from models.mongomodel import MongoBase


class About(MongoBase):
    """
    网站简介类
    """
    def __init__(self, form):
        self.id = form.get('id', None)
        self.content = form.get('content', '')


# from models import Model
#
#
# class About(Model):
#     """
#     网站简介类
#     """
#     def __init__(self, form):
#         self.id = form.get('id', None)
#         self.content = form.get('content', '')