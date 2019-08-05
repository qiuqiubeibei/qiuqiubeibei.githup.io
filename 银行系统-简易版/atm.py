from parse_sql import MysqlHelper
from person import Person
from cardid import CardId
import random
import time


class SqlParse(object):
    """数据库操作封装类"""

    def __init__(self):
        # 对余额查询的sql语句进行封装
        self.search_money = "select prestoreMoney from card where IdCard='%s'"
        # 对余额进行修改的sql语句进行修改
        self.update_money = "update card set prestoreMoney='%d' where IdCard='%s'"

    def sql_search(self, sql):
        """对数据库执行增加操作"""
        # 创建数据库封装对象
        mysqlHelper = MysqlHelper('192.168.204.129', 3306, 'bank_sys', 'root', 'mysql')
        # 获取从数据库得到的信息
        ret = mysqlHelper.get_one(sql)
        return ret

    def sql_update(self, sql):
        """对数据库执行更改操作"""
        # "update students set sname='刘邦' where id=6"
        # 创建数据库封装对象
        mysqlHelper = MysqlHelper('192.168.204.129', 3306, 'bank_sys', 'root', 'mysql')
        # 获取从数据库得到的信息
        ret = mysqlHelper.update(sql)
        return ret

    def sql_delete(self, sql):
        """对数据库执行删除操作"""
        # delete from students where id = 6
        # 创建数据库封装对象
        mysqlHelper = MysqlHelper('192.168.204.129', 3306, 'bank_sys', 'root', 'mysql')
        # 获取从数据库得到的信息
        ret = mysqlHelper.delete(sql)
        return ret

    # 随机产生卡号
    def randomId(self):
        while True:
            IdStr = ""
            for x in range(0, 6):
                randomNum = random.randint(0, 9)
                IdStr += str(randomNum)

            # 对数据库中的信息进行查重
            sql = self.search_money % IdStr
            ret = self.sql_search(sql)
            if not ret:
                return IdStr

    # 验证密码
    def checkPasswd(self, realPasswd):
        tempPasswd = input("请再次输入密码：")
        for i in range(3):
            if tempPasswd == realPasswd:
                return 1
            else:
                tempPasswd = input("密码错误！请再次输入密码：")
        return False

    # 验证卡号及密码信息
    def checkUser(self):

        currNum = input("请输入您的卡号:")
        # 数据库进行交互，查询信息是否匹配

        # 1.1先判断银行卡是否被锁定
        sql = "select locks from card where IdCard='%s'" % currNum
        # 数据库封装对象
        one = self.sql_search(sql)
        # print(type(one[0]))
        # print(one[0])
        # 对用户进行判断
        if one[0] == "True":
            print("访问失败！银行卡已被锁定。。")
            return False

        # 1.2对用户密码进行验证，判断登录信息是否正确
        sql = "select onePasswd from card where IdCard='%s'" % currNum
        # 创建数据库封装对象
        realpwd = self.sql_search(sql)  ## 注意此处得到的是一个元组对象

        if not self.checkPasswd(realpwd[0]):
            print("用户名或者密码输入错误！查询失败")
            return False
        return currNum


class ATM(SqlParse):
    # 行为方法：开户、查询、存储、改密、锁定、解锁、补卡、销户

    def addUser(self):
        '''开户'''
        # 获取用户信息
        Name = input("请输入您的姓名：")
        infoCard = input("请输入您的身份信息：")
        teleNum = input("请输入您的电话号码:")
        prestoreMoney = int(input("请输入您的预存金额："))

        if prestoreMoney < 0:
            print("输入有误请重新开户！")
            return -1
        onePasswd = input("请输入密码：")
        # 验证密码
        if not self.checkPasswd(onePasswd):
            print("密码输入错误,开户失败！")
            return -1
        # 随机产生卡号
        IdCard = self.randomId()

        # 创建银行卡信息类，对银行卡信息进行保存
        card = CardId(IdCard, onePasswd, prestoreMoney)
        card.save_data()

        # 创建用户信息类，对用户信息进行保存
        userStr = Person(Name, infoCard, teleNum, IdCard)
        userStr.save_data()

        # 创建用户登录权限信息
        authority = '0'
        # insert into login(username, password, isdelete, authority)VALUES('laowang', '12345', 1, '0')
        self.addLoginInfo(Name, onePasswd, authority)

        print("恭喜您开户成功,您的卡号为(%s),系统登录名为(%s),密码和卡号密码一致.请牢记！" % (IdCard, Name))
        time.sleep(2)

    def searchMessage(self):
        '''查询'''
        # 先进行验证
        currNum = self.checkUser()
        if not currNum:
            return -1
        # 从数据库中查找出余额信息
        sql = self.search_money % currNum
        # 对数据库执行相关操作
        leftMoney = self.sql_search(sql)
        print("您的卡号为：%s,您的余额为:%d" % (currNum, leftMoney[0]))

    def saveMoney(self):
        '''存储'''
        currNum = self.checkUser()
        if not currNum:
            return -1
        # 对数据库执行的操作
        # 1.1 用户money
        sql = self.search_money % currNum
        nowMoney = self.sql_search(sql)
        # 1.2 对用户Money进行改变
        addMoney = int(input("请输入您要存储的金额："))
        totalMoney = nowMoney[0] + addMoney
        sql = self.update_money % (totalMoney, currNum)
        self.sql_update(sql)

        print("恭喜您存款成功，银行余额为：%d" % totalMoney)

    def fetchMoney(self):
        '''取款'''
        currNum = self.checkUser()
        if not currNum:
            return -1
        # 对数据库执行的操作
        # 1.1 用户money
        sql = self.search_money % currNum
        nowMoney = self.sql_search(sql)
        # 1.2 对用户Money进行改变
        subMoney = int(input("请输入您要取款的金额："))
        if subMoney > nowMoney[0]:
            print("您的操作有误！！")
            return -1
        totalMoney = nowMoney[0] - subMoney
        sql = self.update_money % (totalMoney, currNum)
        self.sql_update(sql)

        print("恭喜您取款成功，银行余额为：%d" % totalMoney)

    def shiftMoney(self):
        """转账"""
        currNum = self.checkUser()
        if not currNum:
            return -1
        # 对当前用户执行的操作
        # 1.1 用户money
        sql = self.search_money % currNum
        nowMoney = self.sql_search(sql)
        # 1.2 获取要转到的用户
        shiftNum = input("请输入您要转到的卡号:")
        # 1.3 对用户Money进行改变
        subMoney = int(input("请输入您要转款的金额："))
        if subMoney > nowMoney[0]:
            print("您的操作有误！！")
            return -1
        totalMoney = nowMoney[0] - subMoney
        # 当前账户的余额信息
        sql = self.update_money % (totalMoney, currNum)
        self.sql_update(sql)

        # 到账卡号的用户进行操作
        # 1.1 到账用户money
        sql = self.search_money % shiftNum
        nowMoney = self.sql_search(sql)
        totalMoney = nowMoney[0] + subMoney
        # 当前账户的余额信息
        sql = self.update_money % (totalMoney, shiftNum)
        self.sql_update(sql)

        print("恭喜您转款成功!!!")

    def alterPwd(self):
        """改密"""
        # 先进行验证
        currNum = self.checkUser()
        if not currNum:
            return -1
        # 从数据库中查找出余额信息
        newPwd = input("请输入您的新密码：")
        if not self.checkPasswd(newPwd):
            return -1
        sql = "select username from person where bankcard='%s'" % currNum
        ret = self.sql_search(sql)

        # 创建数据库封装对象
        sql = "update card set onePasswd='%s' where IdCard='%s'" % (newPwd, currNum)
        self.sql_update(sql)

        sql = "update login set password='%s' where username='%s'" % (newPwd, ret[0])
        self.sql_update(sql)
        print("恭喜您修改成功")

    def lockUser(self):
        '''锁定'''
        # 先判断
        currNum = self.checkUser()
        if not currNum:
            return -1

        sql = "update card set locks='%s' where IdCard='%s'" % ("True", currNum)
        self.sql_update(sql)
        # 密码如果正确则对卡的属性lockUser进行修改，及锁卡
        print("锁定成功！")

    def unlocking(self):
        '''解锁'''
        # 先判断
        currNum = input("请输入卡号：")
        sql = "update card set locks='%s' where IdCard='%s'" % ("False", currNum)
        ret = self.sql_update(sql)
        if ret:
            print("解锁成功！")
        else:
            print("解锁失败！请重式！")

    def restoreCard(self):
        '''补卡'''
        infoCard = input("请输入您的身份证信息：")
        # 补卡号
        sql = "select bankcard from person where infoCard='%s'" % infoCard
        ret = self.sql_search(sql)
        print("请牢记您的卡号:", ret[0])

    def withdrawCard(self):
        '''销户'''
        currNum = self.checkUser()
        if not currNum:
            return -1
        # 1.消除card表中的信息
        sql = "delete from card where IdCard = '%s'" % currNum
        self.sql_delete(sql)
        # 2.消除person表中的信息
        sql = "select username from person where bankcard='%s'" % currNum
        ret = self.sql_search(sql)
        sql = "delete from login where username = '%s'" % ret[0]
        self.sql_delete(sql)
        # 3.消除login表中的信息
        sql = "delete from person where bankcard = '%s'" % currNum
        self.sql_delete(sql)
        print("销户成功！！")

    def showUserInfo(self):
        '''显示用户信息'''
        # 先进行验证
        currNum = self.checkUser()
        if not currNum:
            return -1
        # 从数据库中查找出余额信息
        sql = "select * from person where bankcard='%s'" % currNum
        ret = self.sql_search(sql)
        print("用户信息如下 姓名: %s, 身份证号:%s, 电话号码:%s, 银行卡号:%s" % ret)

    def alterUserInfo(self):
        '''修改用户信息'''
        currNum = self.checkUser()
        if not currNum:
            return -1
        Name = input("请输入您的姓名：")
        infoCard = input("请输入您的身份信息：")
        teleNum = input("请输入您的电话号码:")
        sql = "select username from person where bankcard='%s'" % currNum
        ret = self.sql_search(sql)

        sql = "update person set username='%s',infoCard='%s',telNum='%s' where bankcard='%s'" % (
        Name, infoCard, teleNum, currNum)
        self.sql_update(sql)

        sql = "update login set username='%s' where username='%s'" % (Name, ret[0])
        self.sql_update(sql)
        print("恭喜您修改信息成功！！")
        time.sleep(1)

    def addLoginInfo(self, name, pwd, auth):
        sql = "insert into login(username, password, isdelete, authority) values ('%s', '%s', 1, '%s')" % (
            name, pwd, auth)
        mysqlHelper = MysqlHelper('192.168.204.129', 3306, 'bank_sys', 'root', 'mysql')
        # 获取从数据库得到的信息
        mysqlHelper.insert(sql)


if __name__ == '__main__':
    users = ATM()
    print(users.randomId())
