# -*- coding: utf-8 -*-
import config
from collector.get_pictures import collect_in_page,enter
from wechatListener.wvLogin import download_wx_pic
import time
from threadManager.multThread import task_add,task_finish
import threading
if __name__=='__main__':
    if config.RUN_WeChat_Listener:
        task=threading.Thread(download_wx_pic)
        task.start()
        task.join()
    for tie_ba_key in config.VISIT_TIEBA_LIST:
        links=enter(tie_ba_key,config.DEFAULT_PAGE_NUMBER)
        line_number=config.TASK_LINES
        start=0
        while start<len(links):
            sub_links=links[start:start+line_number]
            tasks=[]
            for link in links:
                t=threading.Thread(collect_in_page,target=(link,))
                t.start()
                tasks.append(t)
            for t in tasks:
                t.join()
            start+=line_number



