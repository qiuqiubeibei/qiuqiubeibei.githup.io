import time
from parse_sql import MysqlHelper


class Admin(object):

    def pintAdminView(self):
        print("**************************************************************")
        print("*                                                            *")
        print("*                                                            *")
        print("*                        欢迎登录XX银行                        *")
        print("*                                                            *")
        print("*                                                            *")
        print("**************************************************************")

    def printSelectView(self):
        print("      普通用户（1）                            管理员用户(2)     ")

    def sysFunctionView(self):
        print("**************************************************************")
        print("*            开户（1）                   查询（2）           *")
        print("*            取款（3）                   存款（4）           *")
        print("*            转账（5）                   改密（6）           *")
        print("*            锁定（7）                   解锁（8）           *")
        print("*            补卡（9）                   用户信息（10）       *")
        print("*            修改用户信息（11）           销户（0）           *")
        print("*                          退出（q）                        *")
        print("**************************************************************")

    def normalUserView(self):
        print("**************************************************************")
        print("*            查询（1）                   取款（2）           *")
        print("*            存款（3）                   转账（4）           *")
        print("*                          退出（q）                        *")
        print("**************************************************************")

    def AdminOption(self, flag):
        """实现登录操作"""
        Iputadmin = input("请输入账号：")
        pwd = input("请输入密码：")

        # 根据数据库操作的返回值进行操作
        if self.sql_conn(Iputadmin, pwd, flag):
            print("登录成功!")
            time.sleep(2)
            return True, flag
        else:
            print("登录失败！请重新确认用户名和密码")
            return False, flag

    def selectUser(self):
        '''对用户进行管理,选择不同的用户'''
        authority = 0  # 标志位,普通用户为0，管理员用户为1
        self.printSelectView()
        userKey = input("请输入您的选择:")
        if userKey == '1':
            flag, authority = self.AdminOption(authority)
        else:
            authority = 1
            flag, authority = self.AdminOption(authority)
        return flag, authority

    def sql_conn(self, username, password, flag):
        '''与数据库实现交互，实现相关操作'''
        flag = str(flag)
        # 执行数据库相关操作
        sql = "select * from login where username='%s' and password='%s' and authority='%s'" % (
            username, password, flag)
        # 创建数据库封装对象
        mysqlHelper = MysqlHelper('192.168.204.129', 3306, 'bank_sys', 'root', 'mysql')
        one = mysqlHelper.get_one(sql)
        # 对用户进行判断
        if one:
            return 1
        else:
            return 0


if __name__ == "__main__":
    pass
