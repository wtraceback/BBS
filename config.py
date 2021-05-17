import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
    AVATAR_UPLOAD_PATH = os.path.join(basedir, 'user_avatar')
    ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
