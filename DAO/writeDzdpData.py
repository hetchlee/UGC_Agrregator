# -*- coding: utf-8 -*-
__author__ = 'lizhen'
import conMySql


#大众点评评论写入sql
def dzdpwriteToSql(reviewsid,business_id,created_time,text_excerpt,review_rating,product_rating,decoration_rating,service_rating):
    conn = conMySql.openSQL()
    cursor = conn.cursor()

    cursor.execute("insert into dzdpreview values(%s,%s,%s,%s,%s,%s,%s,%s)"
                   ,(reviewsid,business_id,created_time,text_excerpt,review_rating,product_rating,decoration_rating,service_rating))
    conn.commit()
    cursor.close()

    return True