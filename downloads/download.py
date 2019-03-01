# -*- coding: utf-8 -*-
import config,pymysql,jieba
from downloads.download_config import *


def create_pictrue(bdata,suffix):
    import random
    num=random.randint(100000,1000000)
    path=DOWNLOAD_PATH+PREFIX+"_"+str(num)+"."+suffix
    with open(path,"wb") as pic:
        pic.write(bdata)

def download():
    connect = pymysql.connect(config.DB_HOST, config.DB_USER, config.DB_PASSWORD, config.DB_DATABASE, config.DB_PORT)
    cursor = connect.cursor()
    keys="|".join([s for s in jieba.cut(KEYWORDS)])
    cursor.execute("select picdata,suffix from mypics WHERE picinfo regexp %s",(keys,))
    counter=NUMBER_LIMIT
    for pic in cursor.fetchall():
        if counter<=0:
            break
        counter-=1
        create_pictrue(pic[0],pic[1])
    print("Download finish!")





