from models import Model


class User(Model):
    """
    User 是一个保存用户数据的 model
    """
    def __init__(self, form):
        self.id = form.get('id', None)
        self.username = form.get('username', '')
        self.password = form.get('password', '')


    def hashed_salt_password(self, password, salt='abc[];,./123'):
        """
        生成一个带盐的密文
        一个 md5 + salt 的哈希密码
        """
        import hashlib
        def sha256(s):
            # 用 ascii 编码转换成 bytes 对象
            ascii_str = s.encode('ascii')
            return  hashlib.sha256(ascii_str).hexdigest()

        h1 = sha256(password)
        # 使用 哈希的密码 + salt
        h2 = sha256(h1 + salt)

        # 返回摘要字符串
        return h2

    def hashed_password(self, password):
        """
        使用 md5 生成哈希密码
        """
        import hashlib

        # 用 ascii 编码转换成 bytes 对象
        p = password.encode('ascii')
        s = hashlib.sha256(p)

        # 返回摘要字符串
        return s.hexdigest()

    @classmethod
    def register(cls, form):
        username = form.get('username', '')
        password = form.get('password', '')
        if len(username) > 2 and User.find_by(username=username) is None:
            u = User.new(form)
            u.password = u.hashed_salt_password(password)
            u.save()
            return u
        else:
            return None

    @classmethod
    def validate_login(cls, form):
        u = User(form)
        user = User.find_by(username=u.username)
        if user is not None and user.password == u.hashed_salt_password(u.password):
            return user
        else:
            return None