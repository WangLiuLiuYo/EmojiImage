# EmojiImage
此工具是是个集自动图片收集（从贴吧）、保存（选择本地或者数据库）、筛选并且下载的小工具，我称之为半自动斗图系统。只要连接itchat就可以实现自动回复固定
文字相关的表情。

使用方法：
--sqlTable里的sql脚本建表
--在config文件按说明完整的配置所有的收集设置
--在download_config里配置所有的下载设置
--运行run.py即可收集图片
--运行run_downlod_to_local.py即可下载相关图片


说明：依赖第三方库为bs4，pymysql，requests，jieba，百度云api接口，除导入必要的库以外还需要拥有百度云账户
