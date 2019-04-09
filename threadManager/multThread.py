# -*- coding: utf-8 -*-

import threading,collections
import config
#全局解释锁，维护线程安全（针对mysql的插入）
MYSQL_LOCK=threading.Lock()


def task_add():
    if config.TASK_LINES>0:
        config.TASK_LINES-=1
        return True
    else:
        return False

def task_finish():
    config.TASK_LINES+=1
