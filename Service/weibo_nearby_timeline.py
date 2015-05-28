# -*- coding: utf-8 -*-
__author__ = 'lizhen'
from weibo import APIClient
import json
from DAO import conMySql
def nearbytline():
    db = conMySql.openSQL()
    #微博账号获取
    weiboacount = conMySql.getweiboacount(db)
    app_key=weiboacount[1]
    app_secret=weiboacount[2]
    token=weiboacount[3]
    #poiinfo获取
    poiinfo = conMySql.getPoiInfo(db)
    lat = poiinfo[2]
    lon = poiinfo[3]

    client = APIClient(app_key, app_secret, redirect_uri='')
    client.set_access_token(token, 0)

    data =client.place.nearby_timeline.get(lat=lat,long=lon,starttime='1422720000',range=3000,count=50)
    # print data["statuses"][0]["url_objects"][0]["object"]["object"]["address"]["fax"]
    # print data
    return data