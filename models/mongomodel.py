from pymongo import MongoClient

client = MongoClient()


class MongoBase(object):
    '''
    操作 mongodb 的驱动类，orm
    '''

    @classmethod
    def new(cls, form=None, **kwargs):
        """
        子类用来填完新的实例
        """
        classname = cls.__name__

        # 创建一个空对象
        m = cls(form)
        m.generate_id()
        m.save()
        return m

    def generate_id(self):
        classname = self.__class__.__name__
        models = list(client.db[classname].find({}).sort([('id', 1)]))

        # 用户注册
        if len(models) > 0:
            self.id = models[-1]['id'] + 1
        else:
            self.id = 1

    def save(self):
        classname = self.__class__.__name__
        client.db[classname].save(self.__dict__)

    @classmethod
    def _find(cls, **kwargs):
        """
        mongo 数据查询
        """
        classname = cls.__name__
        ds = client.db[classname].find(kwargs)
        ms = [cls(d) for d in ds]

        return ms

    @classmethod
    def find_by(cls, **kwargs):
        ms = cls._find(**kwargs)
        if len(ms) > 0:
            return ms[0]
        else:
            return None

    def __repr__(self):
        classname = self.__class__.__name__
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)

        return '< {}\n {} \n>\n'.format(classname, s)