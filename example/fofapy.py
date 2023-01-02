import pyfofa


def welcome():
    t = ''' ____  _____  ____  __    ____  _  _ 
( ___)(  _  )( ___)/__\  (  _ \( \/ )
 )__)  )(_)(  )__)/(__)\  )___/ \  / 
(__)  (_____)(__)(__)(__)(__)   (__) 
        '''
    print(t)

def menu():
    menu = '''
    1.检查你的配置信息和用户信息
    2.使用FOFA查询信息
    3.统计聚合查询
    4.Host聚合查询
    ...
    99.退出
    '''
    print(menu)
    x = input('输入你需要的操作数 :>')
    if x == '1':
        pass
    elif x == '2':
        pass
    elif x == '3':
        pass
    elif x == '4':
        pass
    elif x == '99':
        return 0
    else:
        print('Invalid input, please try again.')
        menu()  # recall the menu function to allow the user to try again


def check_user_info():
    handle = pyfofa.Client()
    print("\n下面，会首先输出你的配置信息，随后会进行检查。")
    print(handle.check_user_info())
welcome()
