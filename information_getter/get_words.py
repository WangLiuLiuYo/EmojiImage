# -*- coding: utf-8 -*-

import aip
import config


client=aip.AipOcr(config.app_id,config.api_key,config.secret_key)

def pic_word_finder(bdata):
    resp=client.basicGeneral(bdata)
    print(resp)
    if 'words_result' in resp:
        words=[]
        for kv in resp.get('words_result'):
            v=kv['words']
            words.append(v)
        r=''.join(words)
        return  r
    else:
        return "纯图片"
