from database import db, ma

from metrics_config import db_config

###
#   metric table
###
class Test(db.Model):
    __tablename__ = 'test_tb'
    __bind_key__ = db_config.bind_name
    id: int = db.Column(db.Integer, primary_key=True)

class TestSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id",)

Test_schema = TestSchema(many=True)
