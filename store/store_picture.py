# -*- coding: utf-8 -*-
import pymysql

import config
import requests
from information_getter.get_words import pic_word_finder
import time,random,re
def get_pictrue_data(url):
    r=requests.get(url,headers=config.header)
    return r.content

def get_cur_date():
    return time.strftime("%Y-%m-%d",time.localtime(time.time()))


from threadManager.multThread import MYSQL_LOCK
def store_pictrue_to_mysql(data,info,suffix='jpg'):
    print("storing picture in MySQL database....and have key word --->",info)
    connect = pymysql.connect(config.DB_HOST, config.DB_USER, config.DB_PASSWORD, config.DB_DATABASE, config.DB_PORT)
    cursor=connect.cursor()
    sql="insert into mypics(picdata,picinfo,suffix) VALUES (%s,%s,%s);"
    global MYSQL_LOCK
    if MYSQL_LOCK.acquire():
        cursor.execute(sql, (pymysql.Binary(data), info, suffix))
        connect.commit()
        MYSQL_LOCK.release()




def store_picture_to_local(data,pic_name,suffix):
    pic_name+=str(random.randint(100000,1000000))
    print("storing picture in ",config.LOCAL_PATH," database....and have key word --->",pic_name)
    with open(config.LOCAL_PATH+pic_name+"."+suffix,"wb") as p:
        p.write(data)




def store_pictures(url):
    bdata=get_pictrue_data(url)
    info=pic_word_finder(bdata)
    if 'png'in url or 'PNG' in url:
        suffix='png'
    else:
        suffix='jpg'
    if config.IS_STORE_LOCAL:
        store_picture_to_local(bdata,info,suffix)
    else:
        store_pictrue_to_mysql(bdata,info,suffix)






