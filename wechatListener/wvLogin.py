# -*- coding: utf-8 -*-

import itchat
from config import TEMPORARY_PATH,KEEP_LOGIN,IS_STORE_DB
from store.store_picture import store_pictrue_to_mysql,store_picture_to_local
from  information_getter.get_words import pic_word_finder
@itchat.msg_register(itchat.content.PICTURE)
def download_wx_pic(msg):
    print(msg)
    print('picture from user:'+msg['FromUserName'])
    print(msg['Text'](TEMPORARY_PATH))
    store_file_data(TEMPORARY_PATH)

def get_sufix(name):
    if 'jpg' or 'JPG' in name:
        return 'jpg'
    else:
        return 'png'
def store_file_data(path):
    with open(path,'rb') as f:
        fdata=f.read()
        info=pic_word_finder(fdata)
        suffix = get_sufix(path)
        if IS_STORE_DB:
            store_pictrue_to_mysql(fdata,info,suffix)
        if IS_STORE_DB:
            store_picture_to_local(fdata,'',suffix)



def run_wechat_listener():
    itchat.auto_login(KEEP_LOGIN)
    itchat.run()