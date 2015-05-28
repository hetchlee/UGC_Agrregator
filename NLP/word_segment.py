# -*- coding: utf-8 -*-
__author__ = 'lizhen'
from DAO import readWeiboData
from DAO import writeWeiboData_ByNLP
from snownlp import SnowNLP
import jieba
#微博文本分词
def textsegment():
    countnumber = readWeiboData.count()[0]
    for i in range(1,countnumber):

        textdata = readWeiboData.getText(i)
        seg_list = jieba.cut_for_search(textdata)
        texttosql = "  ".join(seg_list)
        writeWeiboData_ByNLP.textWriteToSql(texttosql,i)

#用户简介分词
def descriptionsegment():
    countnumber = readWeiboData.count()[0]
    for i in range(1,countnumber):

        textdata = readWeiboData.getdescription(i)
        seg_list = jieba.cut_for_search(textdata)
        texttosql = "  ".join(seg_list)
        writeWeiboData_ByNLP.descriptionWriteToSql(texttosql,i)
