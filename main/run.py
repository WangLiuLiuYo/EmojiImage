# -*- coding: utf-8 -*-
import config
from collector.get_pictures import collect_in_page,enter



if __name__=='__main__':
    for tie_ba_key in config.VISIT_TIEBA_LIST:
        links=enter(tie_ba_key,config.DEFAULT_PAGE_NUMBER)
        for link in links:
            collect_in_page(link)
