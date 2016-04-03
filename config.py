import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    RPICLOUD_MAIL_SUBJECT_PREFIX = '[RASPcloud]'
    RPICLOUD_MAIL_SENDER = 'RPIcloud Admin <RPIcloud@example.com>'
    RPICLOUD_ADMIN = 'admin'    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # MAIL_SERVER = 'localhost'
    # MAIL_PORT = '25'
    # MAIL_USE_TLS = 	True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'data_dev.sqlite')


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'data_test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'data.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_DATABASE_URL') or \
        'mysql://rpi:raspberry@localhost/rpidb'


config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'production': ProductionConfig,
    'default' = DevelopmentConfig
}