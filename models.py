from database import db, ma

class db_config(object):
    bind_name = "models"
    account = 'root'  # 账号
    password = 'root'  # 填入密码
    proname = 'core_developers'  # 填入数据库名
    ip = 'mysql'  # 填入服务器网址
    port = '3306'  # 端口
    SECRET_KEY = "hahahaha"  # session密钥hhhhhhhh
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(account, password, ip, port, proname)
    # print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = True


###
#    developers table
###
class Developers(db.Model):
    __tablename__ = 'developers'
    __bind_key__ = db_config.bind_name
    login:str = db.Column(db.String(255), nullable=False, primary_key=True)
    core:int = db.Column(db.Boolean)

class DevelopersSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("login", "core")

Developers_schema = DevelopersSchema(many=True)

###
#   repos table
###
