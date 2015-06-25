# -*- coding: utf-8 -*-
__author__ = 'lizhen'
import MySQLdb
import random

dbinfo=[
    'localhost',
    'root',
    '1234',
    'sinaweibo',
    '3306',
    'sinaweiboacount',
    'fangteinfo',
    'weibodatamodel',

]
#打开mysql,返回db
def openSQL():
    db = MySQLdb.connect(dbinfo[0],dbinfo[1],dbinfo[2],dbinfo[3],charset="utf8")
    return db

#获取mysql中微博账号数量
def countweiboaccountnumber():
    db = openSQL()
    cursor = db.cursor()
    cursor.execute("select count(*) from sinaweiboacount")
    data = cursor.fetchone()
    cursor.close()
    db.close()
    return data

#从mysql中获取微博账号,随机获取微博账号
def getweiboacount(db):
    weiboacount = []
    accountnumber = countweiboaccountnumber()[0]
    i = random.randint(0,accountnumber)
    cursor = db.cursor()
    cursor.execute("select * from sinaweiboacount where ID=%s"%i)
    data = cursor.fetchone()
    weiboacount.extend(data)
    cursor.close()
    return weiboacount
#获取fangteinfo中的poi个数
def countpoinumber():
    db = openSQL()
    cursor = db.cursor()
    cursor.execute("select count(*) from fangteinfo")
    data = cursor.fetchone()
    cursor.close()
    db.close()
    return data

#从mysql中获取需抽取新浪微博的poi经纬度
def getPoiInfo(db):
    poiinfolist =[]
    number = countpoinumber()[0]
    i = random.randint(0,number)
    cursor = db.cursor()
    cursor.execute("select * from fangteinfo where ID=%s"%i)
    data = cursor.fetchone()
    poiinfolist.extend(data)
    cursor.close()
    return poiinfolist