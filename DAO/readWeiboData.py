# -*- coding: utf-8 -*-
__author__ = 'lizhen'

import MySQLdb
import conMySql


#从微博数据中取用户发布文本进行分词
def getText(i):

    db = conMySql.openSQL()
    cursor = db.cursor()
    cursor.execute("select text from wuhu where ID=%s"%i)
    textdata = cursor.fetchone()

    cursor.close

    if textdata[0]=='':
        textdata='unknown'
    try:
        textdata = textdata[0].encode('utf8')
    except AttributeError:
        textdata="unknown"
    return textdata

#获取微博数据条数
def count():
    db = conMySql.openSQL()
    cursor = db.cursor()
    cursor.execute("select count(*) from wuhu")
    number = cursor.fetchone()
    return number

#从微博数据中取用户简介文本
def getdescription(i):
    db = conMySql.openSQL()
    cursor = db.cursor()
    cursor.execute("select userdescription from wuhu where ID=%s"%i)
    textdata = cursor.fetchone()

    cursor.close
    if textdata[0]=='':
        textdata='unknown'
    try:
        textdata = textdata[0].encode('utf8')
    except AttributeError:
        textdata="unknown"
    return textdata