# -*- coding: utf-8 -*-
__author__ = 'lizhen'
from Service import weibo_nearby_timeline, dzdp_FindBusiness, dzdp_GetRecentReviews
from DAO import writeWeiboData
from DAO import conMySql
from DAO import writeDzdpData

#将解析数据写入mysql
def weibojsontomysql():
    data= weibo_nearby_timeline.nearbytline()
    weibonumber = len(data["statuses"])
    for i in range(0,weibonumber):
        #取微博ID
        weiboid=data[ "statuses"][i]["id"].encode('utf-8')
        #取text
        try:
            if text.startswith('http'):
                text=''
            else:
                text = data["statuses"][i]["text"].encode('utf-8')
        except:
            text = "unknown"
        #取经纬度
        # try:
        if "annotations" in data["statuses"][i]:
            if "place" in data["statuses"][i]["annotations"]:
                lat = data["statuses"][i]["annotations"]["place"]["lat"]
                lon = data["statuses"][i]["annotations"]["place"]["lon"]
            else:
                lat=data["statuses"][i]["geo"]["coordinates"][0]
                lon=data["statuses"][i]["geo"]["coordinates"][1]
        else:
            lat=data["statuses"][i]["geo"]["coordinates"][0]
            lon=data["statuses"][i]["geo"]["coordinates"][1]

        #取title
        if "annotations" in data["statuses"][i]:
            if "title" in data["statuses"][i]["annotations"]:
                title = data["statuses"][i]["annotations"]["place"]["title"]
            else:
                title='unknow'.encode('utf-8')
        else:
            title='unknow'.encode('utf-8')

        # 取userid
        userid=data["statuses"][i]["user"]["id"].encode('utf-8')
        #取location
        location = data["statuses"][i]["user"]["location"]
        #取userdescription
        decription = data["statuses"][i]["user"]["description"].encode('utf-8')
        #取gender

        gender = data["statuses"][i]["user"]["gender"]

        #取时间
        created_at=data["statuses"][i]["user"]["created_at"]
        monthdict = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
        timelist = created_at.split()
        timestrnew = '%s-%s-%s %s' %(timelist[-1] ,monthdict[timelist[1]], timelist[2] ,timelist[3])
        timestrnew = timestrnew.encode('utf-8')
        #取地点类型
        try:
            if "object" in data["statuses"][i]["url_objects"][i]:
                if "object" in data["statuses"][i]["url_objects"][i]["object"]:
                    if "address" in data["statuses"][i]["url_objects"][i]["object"]["object"]:
                        if "fax" in data["statuses"][i]["url_objects"][i]["object"]["object"]["address"]:
                            fax = data["statuses"][i]["url_objects"][i]["object"]["object"]["address"]["fax"]
            else:
                fax='unknow'.encode('utf-8')
        except IndexError:
            fax='unknow'.encode('utf-8')
        #取城市名
        try:
            if "object" in data["statuses"][i]["url_objects"][i]:
                if "object" in data["statuses"][i]["url_objects"][i]["object"]:
                    if "address" in data["statuses"][i]["url_objects"][i]["object"]["object"]:
                        if "locality" in data["statuses"][i]["url_objects"][i]["object"]["object"]["address"]:
                            locality = data["statuses"][i]["url_objects"][i]["object"]["object"]["address"]["locality"]
            else:
                locality='unknow'
        except IndexError:
            locality='unknow'.encode('utf-8')

        #取街道名
        try:
            if "object" in data["statuses"][i]["url_objects"][i]:
                if "object" in data["statuses"][i]["url_objects"][i]["object"]:
                    if "address" in data["statuses"][i]["url_objects"][i]["object"]["object"]:
                        if "formatted" in data["statuses"][i]["url_objects"][i]["object"]["object"]["address"]:
                            formatted = data["statuses"][i]["url_objects"][i]["object"]["object"]["address"]["formatted"]
            else:
                formatted='unknow'.encode('utf-8')
        except IndexError:
            formatted='unknow'.encode('utf-8')

        #写入mysql,因特殊字符写入问题，将text和description中含有特殊字符按unknown处理
        try:
            writeWeiboData.weibowriteToSql(weiboid,text,lat,lon,title,userid,location,decription,gender,timestrnew,fax,locality,formatted)
        except Exception:
            decription="unknown"
            text = "unknown"
            writeWeiboData.weibowriteToSql(weiboid,text,lat,lon,title,userid,location,decription,gender,timestrnew,fax,locality,formatted)



#将大众点评返回json解析
def dzdptosql():
    data = dzdp_FindBusiness.find_business()
    dznumber = data["count"]
    for i in range(0,dznumber):
        business_id = data["businesses"][i]["business_id"]
        business_name = data["businesses"][i]["name"]
        address = data["businesses"][i]["address"]
        telephone = data["businesses"][i]["telephone"].encode('utf8')
        categories = data["businesses"][i]["categories"][0]
        lat = data["businesses"][i]["latitude"]
        lon = data["businesses"][i]["longitude"]
        avg_rating = data["businesses"][i]["avg_rating"]
        product_grade = data["businesses"][i]["product_grade"]
        decoration_grade = data["businesses"][i]["decoration_grade"]
        service_grade = data["businesses"][i]["service_grade"]
        product_score = data["businesses"][i]["product_score"]
        decoration_score = data["businesses"][i]["decoration_score"]
        service_score = data["businesses"][i]["service_score"]

        writeDzdpData.dzdpwriteToSql(business_id,business_name,address,telephone,categories,lat,lon,avg_rating,product_grade,decoration_grade,service_grade,product_score,decoration_score,service_score)

#获取大众点评商户评论

def dzdpbusinessreviewsToSql():
    data,businessid = dzdp_GetRecentReviews.get_recent_reviews()
    reviewsnumber = data["count"]
    for i in range(0,reviewsnumber):
        reviewsid = data["reviews"][i]["review_id"]
        business_id = businessid
        created_time = data["reviews"][i]["created_time"]
        text_excerpt = data["reviews"][i]["text_excerpt"]
        review_rating = data["reviews"][i]["review_rating"]
        product_rating = data["reviews"][i]["product_rating"]
        decoration_rating = data["reviews"][i]["decoration_rating"]
        service_rating = data["reviews"][i]["service_rating"]

        writeDzdpData.dzdpwriteToSql(reviewsid,business_id,created_time,text_excerpt
                                ,review_rating,product_rating,decoration_rating,service_rating)