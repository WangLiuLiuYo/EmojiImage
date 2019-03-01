# -*- coding: utf-8 -*-



#访问的贴吧名
VISIT_TIEBA_LIST=['表情包','李毅']

#选择存到本地 or 数据库
IS_STORE_DB=True
IS_STORE_LOCAL=not IS_STORE_DB

#保存到本地时的路径
LOCAL_PATH="F://pics//"


#数据库连接配置
DB_HOST="localhost"
DB_PORT=3306
DB_USER="root"
DB_PASSWORD="wang66"
DB_DATABASE="practice"

#图片前缀
PIC_PRIFIX=""
#默认的搜索页数 ps：搜索一个贴吧生成 页数*50 的帖子
DEFAULT_PAGE_NUMBER=5

#请求头 可自行配置
header={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
#请求超时时间
request_timeout=3


#百度api调用的接口参数
app_id="********"
api_key="**********************"
secret_key="****************************"
