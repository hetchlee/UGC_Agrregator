# -*- coding: utf-8 -*-
__author__ = 'lizhen'
import conMySql


#大众点评评论写入sql
def dzdpwriteToSql(business_id,business_name,address,telephone,categories,lat,lon,avg_rating,product_grade,decoration_grade,service_grade,product_score,decoration_score,service_score):
    conn = conMySql.openSQL()
    cursor = conn.cursor()

    cursor.execute("insert into dzdp_wuhu(BusinessId,Name,address,telephone,categories,lat,lon,avg_rating,product_grade,decoration_grade,service_grade,product_score,decoration_score,service_score) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                   ,(business_id,business_name,address,telephone,categories,lat,lon,avg_rating,product_grade,decoration_grade,service_grade,product_score,decoration_score,service_score))
    conn.commit()
    cursor.close()

    return True