from parse_sql import MysqlHelper


class Person(object):
    '''账户（人）对象'''
    __slots__ = ["name", "infoCard", "teleNum", "idCard"]  # 添加指定用户信息

    def __init__(self, name, infoCard, teleNum, idCard):
        self.name = name
        self.infoCard = infoCard
        self.teleNum = teleNum
        self.idCard = idCard

    def save_data(self):
        # 插入sql语句
        sql = "insert into person(username,infoCard,telNum,bankcard) values ('%s','%s','%s','%s')" % (
            self.name, self.infoCard, self.teleNum, self.idCard)
        # 创建数据库操作对象
        mysqlHelper = MysqlHelper('192.168.204.129', 3306, 'bank_sys', 'root', 'mysql')
        one = mysqlHelper.insert(sql)
        if one == 1:
            print("操作成功")
        else:
            print("操作失败")


if __name__ == '__main__':
    person = Person("laowang", "12346", "123354", "12425")
    person.save_data()
