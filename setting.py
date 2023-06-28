class db_config(object):
    account = 'root'  # 账号
    password = 'root'  # 填入密码
    proname = 'core_developers'  # 填入数据库名
    ip = 'mysql'  # 填入服务器网址
    port = '3306'  # 端口
    SECRET_KEY = "hahahaha"  # session密钥hhhhhhhh
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(account, password, ip, port, proname)
    # print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
