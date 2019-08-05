'''
人
类名：Person
属性：姓名 身份证号 电话号 卡
方法：

卡
类名：CardId
属性：卡号，密码，余额, lockuser
行为方法：

提款机
类名：ATM
属性：用户字典
行为方法：开户、查询、存储、改密、锁定、解锁、补卡、销户、退出

管理员
类名：admin
属性：
行为：管理员界面（管理员登录）、系统功能界面

'''
from admin import Admin
from atm import ATM


def main():
    # 管理员（界面对象）
    admin = Admin()
    # 系统开机
    admin.pintAdminView()
    # 对用户进行选择判断
    flag, authority = admin.selectUser()
    # 验证失败,直接返回结束程序！
    if not flag:
        return -1
    # 提款机对象
    atm = ATM()
    if authority == 1:
        while True:
            '''用户菜单，等待用户的操作'''
            admin.sysFunctionView()
            option = input("请输入您的操作：")
            if option == "1":
                # 开户
                atm.addUser()
            elif option == "2":
                # 查询
                atm.searchMessage()
            elif option == "3":
                # 取款
                atm.fetchMoney()
            elif option == "4":
                # 存款
                atm.saveMoney()
            elif option == "5":
                # 转账
                atm.shiftMoney()

            elif option == "6":
                # 改密
                atm.alterPwd()
            elif option == "7":
                # 锁定2
                atm.lockUser()
            elif option == "8":
                # 解锁
                atm.unlocking()
            elif option == "9":
                # 补卡
                atm.restoreCard()
            elif option == "10":
                atm.showUserInfo()
            elif option == "11":
                atm.alterUserInfo()
            elif option == "0":
                # 销户
                atm.withdrawCard()
            elif option == "q":
                break
            else:
                print("请输入正确的操作！")
    else:
        while True:
            '''普通用户菜单，等待用户的操作'''
            admin.normalUserView()
            option = input("请输入您的操作：")
            if option == "1":
                # 查询
                atm.searchMessage()
            elif option == "2":
                # 取款
                atm.fetchMoney()
            elif option == "3":
                # 存款
                atm.saveMoney()
            elif option == "4":
                # 转账
                atm.shiftMoney()
            elif option == "q":
                break
            else:
                print("请输入正确的操作！")


if __name__ == "__main__":
    main()
