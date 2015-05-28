# -*- coding: utf-8 -*-
__author__ = 'lizhen'
import MySQLdb
import conMySql

#抽取微博数据写入MYSQL
def weibowriteToSql(weiboid,text,lat,lon,title,userid,location,userdecription,gender,created_at,fax,localcity,formatted):
    conn = conMySql.openSQL()
    cursor = conn.cursor()

    cursor.execute("insert into wuhu(weiboid,text,lat,lon,title,userid,location,userdescription,gender,created_at,fax,locality,formatted)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                   ,(weiboid,text,lat,lon,title,userid,location,userdecription,gender,created_at,fax,localcity,formatted))
    conn.commit()
    cursor.close()
    conn.close()
    return True
