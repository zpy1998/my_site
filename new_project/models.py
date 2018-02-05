from django.db import models
from mongoengine import *
from mongoengine import connect
#connect("sell48",host="127.0.0.1",port=27017)
# Create your models here.
class Sell48Simple(Document):
    title=StringField()
    price=StringField()
    area=ListField(StringField())
    look=StringField()
    url=StringField()
    cates=ListField(StringField())
    #look=StringField()
    pub_date=StringField()
    meta={"collection":"simple"}        #连接的表名
'''需要传入表中所有'''
