# -*- coding: utf-8 -*-
__author__ = 'lizhen'
import MySQLdb
import conMySql

#将提取关键字的文本写入数据库
def keywordsWriteToSql(text,i):
    conn = conMySql.openSQL()
    cursor = conn.cursor()
    cursor.execute("update wuhu set text_keywords = %s WHERE ID = %s",(text,i))
    conn.commit()
    cursor.close()
    return True

#将分过词的文本写入数据库
def textWriteToSql(text,i):
    conn = conMySql.openSQL()
    cursor = conn.cursor()
    cursor.execute("update wuhu set text_segment = %s WHERE ID = %s",(text,i))
    conn.commit()
    cursor.close()
    return True
#将分过词的用户简介写入数据库
def descriptionWriteToSql(text,i):
    conn = conMySql.openSQL()
    cursor = conn.cursor()
    cursor.execute("update wuhu set description_segment = %s WHERE ID = %s",(text,i))
    conn.commit()
    cursor.close()
    return True

#将情感值写入数据库
def sentimentsWriteToSql(sentiments,i):
    conn = conMySql.openSQL()
    cursor = conn.cursor()
    cursor.execute("update wuhu set text_sentiments = %s WHERE ID = %s",(sentiments,i))
    conn.commit()
    cursor.close()
    return True