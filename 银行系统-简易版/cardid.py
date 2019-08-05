from parse_sql import MysqlHelper


class CardId(object):
    '''银行卡类'''

    def __init__(self, cardId, cardPasswd, prestoreMoney):
        self.cardId = cardId
        self.cardPasswd = cardPasswd
        self.prestoreMoney = prestoreMoney
        self.lockUser = False

    def save_data(self):
        # 插入sql语句
        sql = "insert into card(IdCard,onePasswd,prestoreMoney,locks) values ('%s','%s','%d','%s')" % (
            self.cardId, self.cardPasswd, self.prestoreMoney, str(self.lockUser))
        # 创建数据库操作对象
        mysqlHelper = MysqlHelper('192.168.204.129', 3306, 'bank_sys', 'root', 'mysql')
        one = mysqlHelper.insert(sql)
        if one == 1:
            print("操作成功")
        else:
            print("操作失败")


if __name__ == '__main__':
    card = CardId("123456", "123456", 123456)
    card.save_data()
