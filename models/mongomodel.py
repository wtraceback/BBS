from pymongo import MongoClient

client = MongoClient()


class MongoBase(object):
    '''
    操作 mongodb 的驱动类，orm
    '''
    def generate_id(self):
        models = self.all()

        if len(models) > 0:
            self.id = models[-1].id + 1
        else:
            self.id = 1

    @classmethod
    def new(cls, form=None, **kwargs):
        """
        子类用来生成新的实例
        """
        m = cls(form)

        # 额外设置 m 的属性
        for k, v in kwargs.items():
            setattr(m, k, v)

        m.generate_id()
        m.save()
        return m

    @classmethod
    def _new_from_dict(cls, d):
        """
        从 MongoDB 读取的数据，使用 setattr 来写入实例中
        """
        m = cls({})
        for k, v in d.items():
            setattr(m, k, v)

        return m

    @classmethod
    def all(cls):
        """
        :return: 返回一个集合中所有的文档
        """
        classname = cls.__name__
        ds = client.db[classname].find()
        ms = [cls._new_from_dict(d) for d in ds]
        return ms

    @classmethod
    def _find(cls, **kwargs):
        """
        mongo 数据查询
        返回所有匹配的文档
        """
        classname = cls.__name__
        ds = client.db[classname].find(kwargs)
        ms = [cls._new_from_dict(d) for d in ds]
        return ms

    @classmethod
    def find_all(cls, **kwargs):
        """
        mongo 数据查询
        返回所有匹配的文档(类的实例)
        """
        return cls._find(**kwargs)

    @classmethod
    def find_by(cls, **kwargs):
        """
        mongo 数据查询
        返回匹配的第一条文档(类的实例)
        """
        ms = cls._find(**kwargs)
        if len(ms) > 0:
            return ms[0]
        else:
            return None

    @classmethod
    def get(cls, id):
        return cls.find_by(id=id)

    @classmethod
    def delete(cls, id):
        """
        :param id: 根据 id 查找到类中的数据
        :return: 返回删除的元素或 None
        """
        classname = cls.__name__
        r = client.db[classname].delete_one({"id":id})
        if r.deleted_count == 0:
            return None
        else:
            return True

    def save(self):
        classname = self.__class__.__name__
        client.db[classname].save(self.__dict__)

    def __repr__(self):
        classname = self.__class__.__name__
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)

        return '< {}\n {} \n>\n'.format(classname, s)