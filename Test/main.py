# -*- coding: utf-8 -*-
__author__ = 'lizhen'
import time
from Model import jsonToMysql

if __name__=="__main__":
    while True:
        # word_keywords.keywords()
        # word_keywords.keywords()
        # jsonToMysql.dzdpbusinessreviewsToSql()
        #获取新浪微博数据测试
        # jsonToMysql.weibojsontomysql()
        #获取大众点评数据测试
        jsonToMysql.dzdptosql()
        time.sleep(60)
        #获取大众点评商户id
        # jsonToMysql.dzdpbusinessidjsontosql()