### logging 模块的使用
- scrapy

  - setting中设置LOG_LEVEL="WARING"
  - setting中设置LOG_FILE="./a.log"    #设置日志保存的位置,设置后终端不会显示日志内容
  - import logging,实例化logger的方式在任何文件中使用logger输出内容


- 普通项目中
  - import logging
  - logging.basicConfig(...)   #设置日志输出的样式,格式
  - 实例化一个`logger=logging.gerLogger(__name__)`
  - 在任何Py文件中调用logger即可
  ```
          import logging

          #设置日志的输出样式
          logging.basicConfig(level=logging.INFO,

                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',

                    datefmt='%a, %d %b %Y %H:%M:%S',

                    filename='./myapp.log',

                    filemode='w'
                    )
                    #实例日志管理对象
          logger = logging.getLogger(__name__)

          if __name__ == '__main__':
          logger.info("this is a info log")
          logger.info("this is a info log 1")
  ```
