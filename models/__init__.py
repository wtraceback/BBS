import json


def save(data, path):
    """
    将数据序列化为 JSON 字符串，存储到对应的文件中
    :param data: dict 或 list
    :param path: 文件存储的路径
    """
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as f:
        f.write(s)


def load(path):
    """
    用于从 path 中加载数据
    :param path: 要读取的文件的路径
    :return: 返回反序列化后的 dict 或 list
    """
    with open(path, 'r', encoding="utf-8") as f:
        s = f.read()
        return json.loads(s)


class Model(object):
    """
    Model 是一个 ORM
    Model 是所有 model 的基类
    """
    @classmethod
    def db_path(cls):
        """
        :return: 对应类的文件存储路径
        """
        classname = cls.__name__
        path = 'db/{}.json'.format(classname)
        return path

    @classmethod
    def new(cls, form, **kwargs):
        m = cls(form)

        # 额外设置 m 的属性
        for k, v in kwargs.items():
            setattr(m, k, v)

        m.save()

        return m

    @classmethod
    def _new_from_dict(cls, d):
        """
        从文件中读取的数据，使用 setattr 来写入实例中
        """
        m = cls({})
        for k, v in d.items():
            setattr(m, k, v)

        return m

    @classmethod
    def all(cls):
        """
        :return: 返回一个类的所有存储的实例
        """
        path = cls.db_path()
        models = load(path)
        ms = [cls._new_from_dict(m) for m in models]

        return ms

    @classmethod
    def find_all(cls, **kwargs):
        """
        :param kwargs: 要查找的 key 和 value
        :return: 返回所有匹配的类实例
        """
        ms = []
        k, v = '', ''

        for key, value in kwargs.items():
            k, v = key, value

        all = cls.all()
        for m in all:
            if v == m.__dict__[k]:
                ms.append(m)

        return ms

    @classmethod
    def find_by(cls, **kwargs):
        """
        :param kwargs: 传入的参数只有一个
        :return: 返回匹配的第一个实例或者返回 None
        """
        k, v = '', ''

        for key, value in kwargs.items():
            k, v = key, value

        all = cls.all()
        for m in all:
            if v == m.__dict__[k]:
                return m

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
        models = cls.all()
        index = -1

        for i, e in enumerate(models):
            if e.id == id:
                index = i
                break

        if index == -1:
            return None
        else:
            obj = models.pop(index)
            l = [m.__dict__ for m in models]
            path = cls.db_path()
            save(l, path)

            # 返回被删除的元素
            return obj

    def save(self):
        """
        先读取已存在的实例，并生成一个 list
        把 self 添加进去并保存到文件中
        """
        models = self.all()
        if self.__dict__.get('id') is None:
            # 用户注册
            if len(models) > 0:
                self.id = models[-1].id + 1
            else:
                self.id = 1

            models.append(self)
        else:
            # 更改已存在的用户信息
            for i, m in enumerate(models):
                if m.id == self.id:
                    models[i] = self
                    break

        data = [m.__dict__ for m in models]
        path = self.db_path()
        save(data, path)

    def __repr__(self):
        classname = self.__class__.__name__
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)

        return '< {}\n {} \n>\n'.format(classname, s)